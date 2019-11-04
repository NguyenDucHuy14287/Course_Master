/* Nguyen Duc Huy - 1870567 */
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        txtToken = result.text[1: len(result.text)]
        if (result.text[len(result.text) - 1] == "\n" or result.text[len(result.text) - 1] == "\r"):
            txtToken = result.text[1: len(result.text) - 1]
        raise UncloseString(txtToken);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        txtToken = result.text[1: len(result.text)]
        raise IllegalEscape(txtToken);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

//Parser
//Program
program  : manydecls EOF;

manydecls : decl tail;

tail : decl tail | ;

decl : vardecl | funcdecl;

//Variable declare
vardecl: pritype idlist SEMI;

idlist : varid idlisttail;
idlisttail : CM varid idlisttail | ;
varid: ID | (ID LSB INTLIT RSB);

//Function declare
funcdecl: functionType ID paramdecl body;

paramdecl: LB listparams RB;

listparams : oneparam listparamstail | ;
listparamstail : CM oneparam listparamstail | ;

oneparam : pritype (ID | (ID LSB RSB));

body: LP bodylist RP;

bodylist : onebody bodytail | ;

bodytail : onebody bodytail | ;

onebody : vardecl | stmt;

stmt: ifStmt | other_stmt;

ifStmt: matchIf | unmatchIf;	

matchIf:
	IF LB exp RB match_stmt ELSE match_stmt;	

match_stmt: matchIf
    | other_stmt;			

unmatchIf:
	IF LB exp RB stmt
	| IF LB exp RB match_stmt ELSE unmatch_stmt;

unmatch_stmt: unmatchIf
    | other_stmt;

other_stmt: forStmt
	| body
	| doWhileStmt
	| breakStmt
	| continueStmt
	| returnStmt
	| expStmt;

forStmt:
	FOR LB exp SEMI exp SEMI exp RB stmt;

doWhileStmt:
	DO stmt WHILE exp SEMI;

breakStmt: BREAK SEMI;

continueStmt: CONTINUE SEMI;

returnStmt: RETURN exp SEMI;

expStmt: exp SEMI;

exp: term1 ASSIGN exp | term1;
term1: term1 OR term2 | term2;
term2: term2 AND term3 | term3;
term3: term4 EQUAL term4 
    | term4 NOT_EQUAL term4 
    | term4;
term4: term5 LESS term5
	| term5 LESS_OR_EQUAL term5
	| term5 GREATER term5
	| term5 GREATER_OR_EQUAL term5 
     | term5;
term5: term5 ADD term6
	| term5 SUB term6
	| term6;
term6: term6 MUL term7
	| term6 DIV term7
	| term6 MOD term7
	| term7;
term7: SUB term7
	| NOT term7
	| term8;
term8: LB exp RB 
	| term9;
term9: indexExp
	| funcCall
	| BOOLEANLIT 
     | INTLIT 
     | FLOATLIT
	| STRINGLIT
	| ID;

indexExp: indexFirstExp LSB exp RSB;
indexFirstExp: funcCall | ID;

funcCall: ID LB explist RB;

explist: exp explisttail |;
explisttail: CM exp explisttail |;

pritype: BOOLEAN 
        | INT
        | FLOAT
        | STRING;

functionType: pritype 
        | VOID
        | array_pointer_type;

array_pointer_type: pritype LSB RSB;

//Lexer
BOOLEAN: 'boolean';
INT: 'int' ;
FLOAT: 'float';
STRING: 'string';
VOID: 'void' ;
IF: 'if';
ELSE: 'else';
FOR: 'for';
DO: 'do';
WHILE: 'while';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';

fragment DOUBLE_QUOTE: '"';
fragment DOT: '.';
fragment NON_ESCAPE_LETTER: ~ [\b\f\r\n\t\\"];
fragment EXPONENT: [eE][-]?[0-9]+;

INTLIT: [0-9]+;
BOOLEANLIT: TRUE | FALSE;
TRUE: 'true';
FALSE: 'false';

FLOATLIT: ([0-9]+ DOT [0-9]*) EXPONENT?
	| ([0-9]* DOT [0-9]+) EXPONENT?
	| [0-9]+ EXPONENT+;

fragment ESCAPE_SEQUENCE: '\\' [btnfr"'\\]; 
fragment LEGAL_SEQUENCE: ~["\t\r\n\b\f\\];
fragment ILLEGAL_SEQUENCE: ["\t\r\n\b\f\\];

STRINGLIT:'"'(LEGAL_SEQUENCE | ESCAPE_SEQUENCE)*'"' {
        s = self.text
        self.text = s[1:len(s)-1] 
    };

ID: [a-zA-Z_][a-zA-Z0-9_]*;

LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';
SEMI: ';' ;
CM: ',';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
ASSIGN: '=';
NOT: '!';
OR: '||';
AND: '&&';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
LESS_OR_EQUAL: '<=';
GREATER: '>';
GREATER_OR_EQUAL: '>=';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
COMMENT_BLOCK: '/*' .*? '*/' -> skip; 
COMMENT_LINE:  '//' ~[\r\n]* -> skip;

fragment NO_DOUBLE_QUOTE_UNTIL_EOF: ('"' ~( ["\r\n] )* EOF) ;
fragment NO_DOUBLE_QUOTE_UNTIL_FIRST_NEWLINE: ('"' ~('"')*  [\r\n]+) ;
fragment NO_DOUBLE_QUOTE_BUT_ESCAPEQUOTE_UNTIL_EOF: ('"' ~(["\r\n])* ('\\"') ~( ["\r\n] )* EOF)  ;
fragment NO_DOUBLE_QUOTE_BUT_ESCAPEQUOTE_UNTIL_NEWLINE: ('"' ~('"')* ('\\"') ~('"')*   [\r\n]+) ;

ERROR_CHAR: .;
UNCLOSE_STRING: NO_DOUBLE_QUOTE_UNTIL_EOF
			| NO_DOUBLE_QUOTE_UNTIL_FIRST_NEWLINE
			| NO_DOUBLE_QUOTE_BUT_ESCAPEQUOTE_UNTIL_EOF
			| NO_DOUBLE_QUOTE_BUT_ESCAPEQUOTE_UNTIL_NEWLINE;
ILLEGAL_ESCAPE: '"' (LEGAL_SEQUENCE | ESCAPE_SEQUENCE)* (ILLEGAL_SEQUENCE)+;
