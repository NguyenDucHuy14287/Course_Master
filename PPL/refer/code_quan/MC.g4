/**
 * My Student ID: 1870575
 * My Name: Tran Quan
 */
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
// An MC program consists of many declarations which include variable declarations and function declarations.
program  : manydecls EOF;
manydecls: decl mdTail;
mdTail: decl mdTail | ;

decl: varDecl | funcDecl;
// decl: varDecl;

// <primitive type> <variable> ’;’
// <primitive type> <many-variables> ’;’
varDecl: primitiveType varList SM;
// varDecl: primitiveType variable SM;

varList: variable (CM variable)*;

// varList: variable varTail;
// varTail: CM variable varTail | ;

// boolean b;
// int i;
// float f; boolean ba[5]; int ia[3]; float fa[100];
// varList: variable (CM variable)*;
variable: ID | ID LS INTLIT RS;
// variable: ID;

// Primitive TYPE
primitiveType: BOOLTYPE | INTTYPE | FLOATTYPE | STRINGTYPE;

// Function Declare
// <type> <function-name> ’(’ <parameter-list> ’)’ <block-statement>
funcDecl: funcType ID LB paraList RB blockStmt;
funcType: primitiveType | VOIDTYPE | outputArrPointerType;

// <parameter-list> is a nullable comma-separated list of <parameter-declaration>’s
//paraList: paraListNonNull?;
//paraListNonNull: paraDecl (CM paraDecl)*;
paraList: paraDecl paralistTail | ;
paralistTail: CM paraDecl paralistTail | ;

paraDecl: primitiveType idParam;
// <primitive type> <identifier> or <primitive type> <identifier> ’[’ ’]’.
idParam: ID | ID LS RS ;

// Array pointer TYPE
// Array pointer type is used to declare the input or output parameter type in a function declaration. The value passed to this type must be in an array type or an array pointer type.
// • Input parameter: <primitive type> <identifier> ’[’ ’]’.
// • Output parameter: <primitive type> ’[”]’
// arrayPointerType: inputArrPointerType
//     | outputArrPointerType;
// inputArrPointerType: primitiveType ID LS RS;

outputArrPointerType: primitiveType LS RS;


// blockStmt: LP declPart stmtPart RP;
// declPart: varDeclListNonNull?;
// varDeclListNonNull: varDecl+;
// stmtPart: stmt*;

// Block statement
// A block statement starts with a ‘{‘, followed by a nullable list of variable declaration and statement,
// and ends up with a ‘}’.
blockStmt: LP blockStmtBody RP;

blockStmtBody: declStmt bodyStmt;

declStmt: varDecl*;
bodyStmt: stmt*;

// MC supports these statements: if, for, do. . . while, break, continue, return, expression, and block. All statements except if, for and the block one must be followed by a semi-colon.
stmt: ifStmt
    | otherStmt;

// If statement
// MC language suffers from the so-called dangling-else prob- lem. MC solve this by decreeing that an else must belong to the innermost if.
ifStmt: ifmatch | ifunmatch;
ifmatch: IF LB exp RB stmtmatch ELSE stmtmatch;
stmtmatch: ifmatch
    | otherStmt;

ifunmatch: IF LB exp RB stmt
         | IF LB exp RB stmtmatch ELSE stmtunmatch;
stmtunmatch: ifunmatch
    | otherStmt;

// MC supports these statements: if, for, do. . . while, break, continue, return, expression, and block. All statements except if, for and the block one must be followed by a semi-colon.
otherStmt: dowhileStmt 
    | forStmt
    | breakStmt
    | continueStmt 
    | returnStmt 
    | expStmt
    | blockStmt;

// Do while statement
// do <statement1> <statement2> ... <statementn> while <expression> ’;’ where n ≥ 1.
dowhileStmt: DO stmt+ WHILE exp SM;

// For statement
// for ’(’ <expression1> ’;’ <expression2> ’;’ <expression3> ’)’ <statement>
forStmt: FOR LB exp SM exp SM exp RB stmt;

// break ’;’
breakStmt: BREAK SM;

// continue ’;’
continueStmt: CONTINUE SM;

// Return Statement
returnStmt: noExpReturn | normalExpReturn;
// A return statement with no expression must be contained within a function whose return type is void
noExpReturn: RETURN SM;
// A return statement with an expression must be contained within a non-void function
normalExpReturn: RETURN exp SM;

// Expression statement
// An expression becomes a statement if it is followed by a semicolon
// // An expression is a finite combination of operands and operators. 
expStmt: exp SM;

// Precedence and Associativity
exp: term1 OP_ASSIGN exp
    | term1;
term1: term1 OP_OR term2
    | term2;
term2: term2 OP_AND term3
    | term3;
term3: term4 OP_EQUAL term4
    | term4 OP_NEQUAL term4
    | term4;
term4: term5 OP_LT term5
    | term5 OP_GT term5
    | term5 OP_LTE term5
    | term5 OP_GTE term5
    | term5;
term5: term5 OP_ADD term6
    | term5 OP_SUB term6
    | term6;
term6: term6 OP_MUL term7
    | term6 OP_DIV term7
    | term6 OP_MOD term7
    | term7;
term7: OP_SUB term7
    | OP_NEV term7
    | term8;

// An expression which is in ‘(‘ and ‘)’ has highest precedence.
term8: LB exp RB
    | exp9;

// An operand of an expres- sion can be a literal, an identifier, an element of an array or a function call.
exp9: indexExp
    | funcCall
    | INTLIT
    | FLOATLIT
    | STRINGLIT
    | BOOLLIT
    | ID;

// <expression> ’[’ expression ’]’
indexExp: indexFirstExp LS exp RS;
// The type of the first <expression> must be an array or array pointer type
// foo(2)[3+x] = a[b[2]] +3;
indexFirstExp: funcCall | ID;

// Function call
// function call which starts with an identifier followed by "(" and ")"
funcCall: ID LB argList RB;
// A nullable comma-separated list of expressions might be appeared between “(“ and “)” as a list of arguments
// argList: argListNotNull?;
// argListNotNull: exp (CM exp)*;
argList: exp argListTail |;
argListTail: CM exp argListTail | ;

// Lexer
// Comments
BLOCKCMT: '/*'.*?'*/' -> skip;
LINECMT: '//'(~[\n\r])* -> skip;

// Data types
INTTYPE: 'int' ;
BOOLTYPE: 'boolean';
FLOATTYPE: 'float';
STRINGTYPE: 'string';
VOIDTYPE: 'void' ;

// Keywords
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
WHILE: 'while';
DO: 'do';

// Literals
// -- Boolean literal: contain 2 keywords
BOOLLIT: TRUE | FALSE;
// Boolean Keywords
TRUE: 'true';
FALSE: 'false';
fragment DIGITS: [0-9];
// -- Float literal
fragment EXP: [eE]('-')?DIGITS+;
fragment FRACTION: (DIGITS+'.'DIGITS*) | (DIGITS*'.'DIGITS+);
FLOATLIT: (FRACTION)(EXP)? | (DIGITS+EXP);
// -- Int literal
INTLIT: DIGITS+;

// -- String literal
// A string literal consists of zero or more characters enclosed in double quotes ’"’. The quotes are not part of the string, but serve to delimit it.

// It is a compile-time error for a backspace, newline, formfeed, carriage return, tab, double quote or a backslash to appear inside a string literal. The following escape sequences are used instead:

fragment ESCAPE_SEQUENCE: '\\' [btnfr"'\\]; 
fragment LEGAL_SEQUENCE: ~["\t\r\n\b\f\\];
fragment ILLEGAL_SEQUENCE: ["\t\r\n\b\f\\];

STRINGLIT: '"'(LEGAL_SEQUENCE | ESCAPE_SEQUENCE)*'"' {
        s = self.text
        self.text = s[1:len(s)-1] 
    };

// ID: catch after keywords, literal
ID: [a-zA-Z_][a-zA-Z0-9_]* ;

LB: '(' ;

RB: ')' ;

LP: '{' ;

RP: '}' ;

LS: '[' ;

RS: ']' ;

SM: ';' ;

CM: ',' ;


// Operator
OP_NEV: '!' ;

OP_DIV: '/' ;

OP_MUL: '*' ;

OP_MOD: '%' ;

OP_ADD: '+' ;

OP_SUB: '-' ;

OP_LT: '<' ;

OP_LTE: '<=' ;

OP_GT: '>' ;

OP_GTE: '>=' ;

OP_EQUAL: '==' ;

OP_NEQUAL: '!=' ;

OP_AND: '&&' ;

OP_OR: '||' ;

OP_ASSIGN: '=' ;

// skip 
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

fragment NO_DOUBLE_QUOTE_UNTIL_EOF: ('"' ~( ["\r\n] )* EOF) ;
fragment NO_DOUBLE_QUOTE_UNTIL_FIRST_NEWLINE: ('"' ~('"')*  [\r\n]+) ;
fragment NO_DOUBLE_QUOTE_BUT_ESCAPEQUOTE_UNTIL_EOF: ('"' ~(["\r\n])* ('\\"') ~( ["\r\n] )* EOF)  ;
fragment NO_DOUBLE_QUOTE_BUT_ESCAPEQUOTE_UNTIL_NEWLINE: ('"' ~('"')* ('\\"') ~('"')*   [\r\n]+) ;

UNCLOSE_STRING: NO_DOUBLE_QUOTE_UNTIL_EOF
| NO_DOUBLE_QUOTE_UNTIL_FIRST_NEWLINE
| NO_DOUBLE_QUOTE_BUT_ESCAPEQUOTE_UNTIL_EOF
| NO_DOUBLE_QUOTE_BUT_ESCAPEQUOTE_UNTIL_NEWLINE;


ILLEGAL_ESCAPE: '"' (LEGAL_SEQUENCE | ESCAPE_SEQUENCE)* (ILLEGAL_SEQUENCE)+;

ERROR_CHAR: .;