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

options {
	language = Python3;
}

// program  : mctype 'main' LB RB LP body? RP EOF ;

program: manyDeclarations <EOF>;

manyDeclarations: declaration+;

declaration: variableDeclaration | functionDeclaration;

// variable declaration
variableDeclaration: primitiveType variableList SEMI;

variableList: variable (COMMA variable)*;

variable: ID | (ID LSB INT_LIT RSB);

// function declaration
functionDeclaration:
	functionType ID LB parameterList RB blockStatement;

parameterList:
	(parameterDeclaration (COMMA parameterDeclaration)*)
	|;

parameterDeclaration: primitiveType (ID | (ID LSB RSB));

blockStatement: LP bodyList RP;

bodyList: bodyDeclaration*;

bodyDeclaration: variableDeclaration | statementDeclaration;

statementDeclaration:
	ifStatement
	| forStatement
	| blockStatement
	| doWhileStatement
	| breakStatement
	| continueStatement
	| returnStatement
	| expressionStatement;

ifStatement: matchIfStatement | unmatchIfStatement;

matchIfStatement:
	IF_KEYWORD LB expression RB matchIfStatement ELSE_KEYWORD matchIfStatement | otherStatement;

unmatchIfStatement:
	IF_KEYWORD LB expression RB statementDeclaration
	| IF_KEYWORD LB expression RB matchIfStatement ELSE_KEYWORD unmatchIfStatement;

otherStatement:
	forStatement
	| blockStatement
	| doWhileStatement
	| breakStatement
	| continueStatement
	| returnStatement
	| expressionStatement;

forStatement:
	FOR_KEYWORD LB expression SEMI expression SEMI expression RB statementDeclaration;

doWhileStatement:
	DO_KEYWORD statementDeclaration WHILE_KEYWORD expression SEMI;

breakStatement: BREAK_KEYWORD SEMI;

continueStatement: CONTINUE_KEYWORD SEMI;

returnStatement: RETURN_KEYWORD expression SEMI;

expressionStatement: expression SEMI;

expression:
	firstInferiority ASS_OP expression
	| firstInferiority;
firstInferiority:
	firstInferiority OR_OP secondInferiority
	| secondInferiority;
secondInferiority:
	secondInferiority AND_OP thirdInferiority
	| thirdInferiority;
thirdInferiority:
	fourthInferiority EQ_OP fourthInferiority
	| fourthInferiority NOT_EQ_OP fourthInferiority
	| fourthInferiority;
fourthInferiority:
	fifthInferiority LESS_THAN_OP fifthInferiority
	| fifthInferiority LESS_THAN_OR_EQ_OP fifthInferiority
	| fifthInferiority GREATE_THAN_OP fifthInferiority
	| fifthInferiority GREATE_THAN_EQ_OP fifthInferiority
	| fifthInferiority;

fifthInferiority:
	fifthInferiority ADD_OP sixthInferiority
	| fifthInferiority SUB_OP sixthInferiority
	| sixthInferiority;
sixthInferiority:
	sixthInferiority MUL_OP seventhInferiority
	| sixthInferiority DIV_OP seventhInferiority
	| sixthInferiority MOD_OP seventhInferiority
	| seventhInferiority;
seventhInferiority:
	enghthInferiority SUB_OP seventhInferiority
	| enghthInferiority NOT_OP seventhInferiority
	| enghthInferiority;
enghthInferiority:
	ninthInferiority LSB ninthInferiority RSB
	| ninthInferiority;
ninthInferiority:
	BOOLEAN_LIT
	| INT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| ID
	| funtionCall
	| LB expression RB;

funtionCall: ID LB expressionList RB;

expressionList: expression (COMMA expressionList)* |;

primitiveType:
	BOOLEAN_TYPE
	| INT_TYPE
	| FLOAT_TYPE
	| STRING_TYPE;

functionType:
	primitiveType
	| VOID_TYPE
	| ARRAY_POINTER_OUTPUT_TYPE;

BOOLEAN_TYPE: BOOLEAN_KEYWORD;

INT_TYPE: INT_KEYWORD;

FLOAT_TYPE: FLOAT_KEYWORD;

STRING_TYPE: STRING_KEYWORD;

ARRAY_POINTER_INPUT_TYPE: (
		BOOLEAN_TYPE
		| INT_TYPE
		| FLOAT_TYPE
		| STRING_TYPE
	) ID LSB RSB;

ARRAY_POINTER_OUTPUT_TYPE: (
		BOOLEAN_TYPE
		| INT_TYPE
		| FLOAT_TYPE
		| STRING_TYPE
	) LSB RSB;

VOID_TYPE: VOID_KEYWORD;

fragment DIGIT: [0-9];

fragment EXPONENT: [eE] [-]? DIGIT+;

fragment DOT: '.';

fragment LOWWER_LETTER: [a-z];

fragment UPPER_LETTER: [A-Z];

fragment LETTER: LOWWER_LETTER | UPPER_LETTER;

fragment DOUBLE_QUOTE: '"';

fragment EXCLUDE_ESCAPE_LETTER: ~ [\b\f\r\n\t\\"];

fragment ESCAPE_LETTER: [\b\f\r\n\t\\"];

fragment BACKSLASH: '\\';

INT_LIT: DIGIT+;

BOOLEAN_LIT: TRUE_KEYWORD | FALSE_KEYWORD;

FLOAT_LIT: ([0-9]+ DOT [0-9]*) EXPONENT?
	| ([0-9]* DOT [0-9]+) EXPONENT?
	| [0-9]+ EXPONENT+;

STRING_LIT:
	DOUBLE_QUOTE (('\\' [bfrnt"\\]) | EXCLUDE_ESCAPE_LETTER)* DOUBLE_QUOTE;

LB: '(';

RB: ')';

LSB: '[';

RSB: ']';

LP: '{';

RP: '}';

SEMI: ';';

COMMA: ',';

UNDERSCORE: '_';

BOOLEAN_KEYWORD: 'boolean';
BREAK_KEYWORD: 'break';
CONTINUE_KEYWORD: 'continue';
ELSE_KEYWORD: 'else';
FOR_KEYWORD: 'for';
FLOAT_KEYWORD: 'float';
IF_KEYWORD: 'if';
INT_KEYWORD: 'int';
RETURN_KEYWORD: 'return';
VOID_KEYWORD: 'void';
DO_KEYWORD: 'do';
WHILE_KEYWORD: 'while';
TRUE_KEYWORD: 'true';
FALSE_KEYWORD: 'false';
STRING_KEYWORD: 'string';

ADD_OP: '+';
MUL_OP: '*';
NOT_OP: '!';
OR_OP: '||';
NOT_EQ_OP: '!=';
LESS_THAN_OP: '<';
LESS_THAN_OR_EQ_OP: '<=';
ASS_OP: '=';
SUB_OP: '-';
DIV_OP: '/';
MOD_OP: '%';
AND_OP: '&&';
EQ_OP: '==';
GREATE_THAN_OP: '>';
GREATE_THAN_EQ_OP: '>=';

ID: (LETTER | UNDERSCORE) (LETTER | UNDERSCORE | DIGIT)*;

WS: [ \t\r\n]+ -> skip;
// skip spaces, tabs, newlines
COMMENT: '/*' .*? '*/' -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

ERROR_CHAR:
	. { 
		raise ErrorToken(self.text) 
	};
UNCLOSE_STRING:
	DOUBLE_QUOTE (('\\' [bfrnt"\\]) | EXCLUDE_ESCAPE_LETTER)* {
		raise UncloseString(self.text[1:])
	};

ILLEGAL_ESCAPE:
	DOUBLE_QUOTE (EXCLUDE_ESCAPE_LETTER | ('\\' [bfrnt"\\]))* (
		[\b\f\r\n\t"]
		| ('\\' ~[bfrnt"\\])
	) {

		if (self.text[-1] != '\b' and self.text[-1] != '\f' and self.text[-1] != '\r'
			and self.text[-1] != '\n' and self.text[-1] != '\t' and self.text[-1] != '"'):
			raise IllegalEscape(self.text[1:-2])
		else:
			raise IllegalEscape(self.text[1:])
		
	};
