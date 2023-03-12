grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

// main function is unique => mean appear only once or none
program: decl* mainfunction? decl* EOF;

// ! --------------PARSER RULE--------------

vartype: AUTO| STRING | BOOLEAN | FLOAT | INTEGER | arraytype ;
arithmetricop: MINU | PLUS | MUTI | DIVI | MODU;
booleanop: NOT | AND | OR;
stringop: SCOPE;
relationalop: EQUL | NEQ | LESS | GREA | LOEQ | GOEQ;
demention: INT COMA demention | INT;

// ?testing expression
operator: arithmetricop| booleanop | stringop | relationalop | indexop;
// *Two operation type
// *Two expression (condition expression & typical expression)
operand: constant | ID | operator | functioncall | subexpression ;
condeoperand:constant | ID | operator | functioncall | subcondexpression;


subcondexpression: LB condexpression RB ;
condexpression: condeoperand relationalop condeoperand
		|condexpression (AND|OR) condeoperand
		|NOT condeoperand
		|condeoperand
		;


subexpression:LB expression RB ;
expression: operand stringop operand
		|operand relationalop operand
		|expression (AND|OR) operand
		|expression (PLUS|MINU) operand 
		|expression (MUTI|DIVI|MODU) operand
		|NOT operand
		|MINU operand 
		|indexexpression
		|operand
		;

// ?constant not clear in ass1 
// ?Add ARR
constant: STR | BOOL | FLO | INT | ARR;
functioncall: ID LB arguementlist? RB;

indexop: ID indexexpression;

// ?testing expression


// *--------part of things--------
parameter: INHERIT? OUT? ID COL vartype;

// indexop[]
indexexpression:LSB expressionlist RSB;

//? arguement add-on
arguement: expression; //TODO arguement
functionmainprot:MAIN COL FUNCTION VOID LB parameterlist? RB;
functionprot: ID COL FUNCTION (VOID|vartype) LB parameterlist? RB (INHERIT ID)?;
// ?add-on not found in mt22
functionbody: blockstatement;

// *Statement
scalarvar: ID;
lhs: scalarvar | indexop;

statement: assignstatement 
| ifstatement 
| forstatement 
| whilestatement
| dowhilestatement
| breakstatement
| continuestatement
| returnstatement
| callstatement
| blockstatement
;

assignstatement: lhs EQU expression SEM;

ifstatement: IF LB expression RB statement (ELSE statement)? ;
// ?I put expression for init-express and condition-express
// ? statement should be statement list


forhead:FOR LB scalarvar EQU expression COMA condexpression COMA expression RB;
// modified
forstatement: forhead blockstatement;

whilecondition:WHILE LB condexpression RB;
whilestatement:whilecondition statement;

dowhilestatement: DO blockstatement whilecondition SEM;

breakstatement: BREAK SEM;


continuestatement: CONTINUE SEM;

returnstatement: RETURN expression SEM;

callstatement: functioncall SEM;

blockstatement: LCB (statementlist|variabledecl)*? RCB;

// *--------List of ...--------
idlist: ID  COMA idlist | ID;
expressionlist: expression COMA expressionlist| expression SEM?;
parameterlist: parameter COMA parameterlist| parameter;
arguementlist: arguement COMA arguementlist | arguement;
statementlist: statement SEM statementlist | statement SEM?;
// *--------Declare--------
variabledecl: variabledecls SEM;
variabledecls: (ID COMA variabledecls COMA expression
| ID COL vartype EQU expression
| idlist COL vartype);
functiondecl: functionprot functionbody;

// ?unique function, whose name is main without any parameter and return nothing (type void).
mainfunction: functionmainprot functionbody;
// ?Is arrray type here?
arraytype:ARRAY (LSB demention RSB OF vartype)?;

// * MAIN PROGRAM
decl: functiondecl |variabledecls SEM | expressionlist | statementlist ;
// decl:arraydecl;
// !--------------LEXER RULE----------------

// * --------Comment--------
COMMENT_C : '/*' .*? '*/' -> skip ;
COMMENT_CPP : '//' ~[\r\n]* -> skip ;

// * --------String--------
fragment ESCAPE: '\\' ( 'b' | 'f' | 'n' | 'r' | 't' | '\'' | DB | '\\'| '"' );
fragment STR_CHAR: ESCAPE|~[\\'"\r\n];
STR: (DB STR_CHAR*  DB) {self.text = self.text[1:-1]};
fragment STRTYP: SCOPE;

// * --------Keyword--------
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';
MAIN:'main';

// *--------Boolean--------
BOOL: FALSE | TRUE;
FALSE: 'false';
TRUE: 'true';

// *--------Float--------
fragment DECIMAL:  DIGIT+;
fragment EXPONENT: ('e'|'E') ('+'|'-')? DIGIT+;
FLO:  ((POSINT | ZERO)+ DOT DECIMAL EXPONENT?
		| (POSINT | ZERO)+ DOT? EXPONENT
		| DOT DECIMAL EXPONENT){self.text = self.text.replace('_','')};

// *--------Integer--------
fragment POSINT: [1-9] (UNDE DIGIT | DIGIT)*;
INT: (POSINT | ZERO){self.text = self.text.replace('_','')} ;

// *--------Identifier--------
fragment DIGIT: [0-9];
fragment LETTER: ([a-z] | [A-Z]);
ID: (LETTER | UNDE) (LETTER | UNDE | DIGIT)*;


// *--------Array--------
fragment ARRTYPE: STR|FLO|INT|BOOL|ID;
fragment ARRTYPES: ARRTYPE (' ')* COMA (' ')* ARRTYPES | ARRTYPE ;
ARR: LCB ARRTYPES  RCB;

//*--------Seprator--------
COMA: ',';
COL: ':';
SEM: ';';
DOT: '.';
LSB: '[';
RSB: ']';
LB: '(';
RB: ')';
LCB: '{';
RCB: '}';
EQU:'=';

// *--------Tokens--------
DB: '"';
ZERO: '0';
UNDE: '_';
PLUS: '+';
MINU: '-';
MUTI: '*';
DIVI: '/';
MODU: '%';
NOT: '!'; 
// *--------Operator--------
AND: '&&';
OR: '||';
EQUL: '==';
NEQ: '!=';
LESS: '<';
LOEQ: '<=';
GREA: '>';
GOEQ: '>=';
SCOPE: '::';


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .{raise ErrorToken(self.text)};

fragment ESCAPE_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;
UNCLOSE_STRING: DB STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF ) {raise UncloseString(self.text[1:])};

ILLEGAL_ESCAPE: DB STR_CHAR* ESCAPE_ILLEGAL{raise IllegalEscape(self.text[1:])};