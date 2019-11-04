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
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
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
vardecl: PRITYPE idlist SEMI;

idlist : varid idlisttail;
idlisttail : CM varid idlisttail | ;
varid: ID | (ID LSB INTLIT RSB);

//Function declare
funcdecl: functionType ID paramdecl body;

paramdecl: LB listparams RB;

listparams : oneparam listparamstail | ;
listparamstail : CM oneparam listparamstail | ;

oneparam : PRITYPE (ID | (ID LSB RSB));

body: LP bodylist RP;

bodylist : onebody bodytail | ;

bodytail : onebody bodytail | ;

onebody : vardecl | stmt;

stmt: ifStmt
	| forStmt
	| body
	| doWhileStmt
	| breakStmt
	| continueStmt
	| returnStmt
	| expStmt;

ifStmt: matchIf | unmatchIf;

matchIf:
	IF LB exp RB stmt ELSE stmt;

unmatchIf:
	IF LB exp RB stmt
	| IF LB exp RB matchIf ELSE unmatchIf;

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
	| term5 ADD term6
	| term6;
term6: term6 MUL term7
	| term6 DIV term7
	| term6 MOD term7
	| term7;
term7: term8 SUB term7
	| term8 NOT term7
	| term8;
term8: term9 LSB term9 RSB | term9;
term9: BOOLEANLIT 
     | INTLIT 
     | FLOATLIT
	| STRINGLIT
	| ID
	| funcCall
	| LB exp RB;

funcCall: ID LB explist RB;

explist: exp explisttail |;
explisttail: CM exp explisttail |;

PRITYPE: BOOLEAN 
        | INT
        | FLOAT
        | STRING;

functionType: PRITYPE 
        | VOID
        | ARRAY_POINTER_TYPE;

ARRAY_POINTER_TYPE: PRITYPE LSB RSB;

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
TRUE: 'true';
FALSE: 'false';

fragment DOUBLE_QUOTE: '"';
fragment DOT: '.';
fragment NON_ESCAPE_LETTER: ~ [\b\f\r\n\t\\"];
fragment EXPONENT: [eE][-]?[0-9]+;

INTLIT: [0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
BOOLEANLIT: TRUE | FALSE;
FLOATLIT: ([0-9]+ DOT [0-9]*) EXPONENT?
	| ([0-9]* DOT [0-9]+) EXPONENT?
	| [0-9]+ EXPONENT+;
STRINGLIT:
	DOUBLE_QUOTE (('\\' [bfrnt"\\]) | NON_ESCAPE_LETTER)* DOUBLE_QUOTE;

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

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: DOUBLE_QUOTE (('\\' [bfrnt"\\]) | NON_ESCAPE_LETTER)* 
			{raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: DOUBLE_QUOTE (NON_ESCAPE_LETTER | ('\\' [bfrnt"\\]))* 
			([\b\f\r\n\t"] | ('\\' ~[bfrnt"\\])) 
			{
			if (self.text[-1] != '\b' and self.text[-1] != '\f' and self.text[-1] != '\r'
				and self.text[-1] != '\n' and self.text[-1] != '\t' and self.text[-1] != '"'):
				raise IllegalEscape(self.text[1:-2])
			else:
				raise IllegalEscape(self.text[1:])		
			};
