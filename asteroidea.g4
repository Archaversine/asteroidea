grammar asteroidea;

prog: stmt* ;

stmt: setTapeOp
    | moveOp
    | modifyCellOp
    | ioOp
    | loopStatement
    | whileStatement
    | conditionalStatement
    | jumpStatement
    | functionStatement
    | debugOp
    | setVarOp
    | modifyVarOp
    | importStatement
    | haltOp
    ;

haltOp: 'H' ;

debugOp: showTapeBytesOp
    | showTapeValsOp
    ;

importStatement: '&&' loc=STRING ;

showTapeBytesOp: '[===]';
showTapeValsOp: '[%%%]';

setTapeOp: setTapeStringOp
    | setTapeCellsOp
    | setTapeLengthOp
    ;

setTapeCellsOp: '#' NUM+ ;
setTapeLengthOp: '##' cells=NUM values=NUM;
setTapeStringOp: '#' string=STRING  ;

setVarOp: name=IDENTIFIER ':=' val=number;
modifyVarOp: incrementVarOp
    | decrementVarOp
    ;

incrementVarOp: name=IDENTIFIER '+=' val=number;
decrementVarOp: name=IDENTIFIER '-=' val=number;

loopStatement: repeatStatement
    | whileStatement
    | untilStatement
    ;

repeatStatement: '[' ('-')? iterations=number ']' block=scope;
whileStatement: '?' block=scope;
untilStatement: '!?' block=scope;

conditionalStatement: ifStatement
    | unlessStatement
    ;

ifStatement: '??' block=scope;
unlessStatement: '!??' block=scope;

functionStatement: functionDefinitionStatement
    | functionCallStatement
    ;

functionDefinitionStatement: '&' name=IDENTIFIER defParams? block=scope;
functionCallStatement: '*' name=IDENTIFIER callParams?;

scope: '(' stmt+ ')' | stmt;

jumpStatement: bookmarkStatement
    | jumpToStatement
    ;

bookmarkStatement: '@' name=IDENTIFIER;
jumpToStatement: '^' name=IDENTIFIER;

moveOp : op=(MOVE_LEFT_OP
    | MOVE_RIGHT_OP
    | MOVE_START_OP
    | MOVE_END_OP
    )
    ;

modifyCellOp: increaseOp
    | decreaseOp
    | setValOp
    ;

increaseOp: op='+' val=number;
decreaseOp: op='-' val=number;
setValOp: op='~' ('-')? val=number;

MOVE_LEFT_OP: '<-';
MOVE_RIGHT_OP: '->';
MOVE_START_OP: '<<';
MOVE_END_OP: '>>';

ioOp: op=(READ_CHAR_OP
    | PRINT_CHAR_OP
    | PRINT_MOVE_CHAR_OP
    | READ_INT_OP
    | PRINT_INT_OP
    | PRINT_MOVE_INT_OP
    )
    ;

READ_CHAR_OP: '=>';
PRINT_CHAR_OP: '<=';
PRINT_MOVE_CHAR_OP: '<>';

READ_INT_OP: '%>';
PRINT_INT_OP: '<%';
PRINT_MOVE_INT_OP: '<%>';

parameterOp: '$' name=IDENTIFIER;

defParams: '<' IDENTIFIER (',' IDENTIFIER)* '>' ;
callParams: '<' (IDENTIFIER | number) (',' (IDENTIFIER | number))* '>' ;
number: NUM | lookupOp | parameterOp | '|' number '|';

lookupOp: '^^' name=IDENTIFIER;

NUM: [0-9]+ ;
STRING : '"' .*? '"' ;
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]* ;

WS: [ \t\n\r\f] -> skip;
COMMENT : '//' .*? '\n' -> skip;
