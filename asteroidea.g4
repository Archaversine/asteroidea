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
    | allocOp
    ;

haltOp: 'H' ;
allocOp: '-->';

debugOp: showTapeBytesOp
    | showTapeValsOp
    ;

importStatement: '&&' loc=STRING ;

showTapeBytesOp: '[===]';
showTapeValsOp: '[%%%]';

setTapeOp: setTapeStringOp
    | setTapeCellsOp
    | setTapeLengthOp
    | setTapeFileOp
    ;

setTapeCellsOp: '#' NUM+ ;
setTapeLengthOp: '##' cells=NUM values=NUM;
setTapeStringOp: '#' string=STRING ;
setTapeFileOp: '#f' string=STRING ;

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

functionDefinitionStatement: '&' name=IDENTIFIER block=scope # funcDefNoParams
    | '&' name=IDENTIFIER params=defParams block=scope       # funcDefWithParams
    ;
functionCallStatement: '*' name=IDENTIFIER  # funcCallNoParams
    | '*' name=IDENTIFIER params=callParams # funcCallWithParams
    ;

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

number: '(' val=number ')'                          # numParen
    | val=NUM                                       # numLiteral
    | val=lookupOp                                  # numLookup
    | val=parameterOp                               # numParam
    | '|' val=number '|'                            # numNormalize
    | left=number op=('++' | '--') right=number     # numExpr
    ;

lookupOp: '^^' name=IDENTIFIER;

NUM: [0-9]+ ;
STRING : '"' .*? '"' ;
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]* ;

WS: [ \t\n\r\f] -> skip;
COMMENT : '//' .*? '\n' -> skip;
