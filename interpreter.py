#!/usr/bin/env python3

import os
import sys
import antlr4 as antlr

import TapeVisualizer

from asteroideaLexer import asteroideaLexer
from asteroideaParser import asteroideaParser
from asteroideaVisitor import asteroideaVisitor

MAX_TAPE_DISPLAY_WIDTH = 9

class _ProgramFunction:
    def __init__(self, params, code):
        self.params = params
        self.code = code
    def __repr__(self) -> str:
        return f"ProgramFunction({self.params}, {self.code})"

class AsteroideaVisitor(asteroideaVisitor):

    MOVE_LEFT_OP = '<-';
    MOVE_RIGHT_OP = '->';
    MOVE_START_OP = '<<';
    MOVE_END_OP = '>>';

    READ_CHAR_OP = '=>'
    PRINT_CHAR_OP = '<='
    PRINT_MOVE_CHAR_OP = '<>'
    READ_INT_OP = '%>'
    PRINT_INT_OP = '<%'
    PRINT_MOVE_INT_OP = '<%>'

    functions = {}
    function_vars = [{}]

    def __init__(self):

        self.tape = [0] * 8
        self.tape_pos = 0

        self.move_ops = {
            AsteroideaVisitor.MOVE_LEFT_OP: lambda: self.shift_tape_pos(-1),
            AsteroideaVisitor.MOVE_RIGHT_OP: lambda: self.shift_tape_pos(1),
            AsteroideaVisitor.MOVE_START_OP: lambda: self.set_tape_pos(0),
            AsteroideaVisitor.MOVE_END_OP: lambda: self.set_tape_pos(len(self.tape) - 1)
        }

        self.io_ops = {
            AsteroideaVisitor.READ_CHAR_OP: lambda: ord(input()),
            AsteroideaVisitor.PRINT_CHAR_OP: lambda: print(chr(self.current_cell_value()), end=''),
            AsteroideaVisitor.PRINT_MOVE_CHAR_OP: lambda: self.print_move(AsteroideaVisitor.PRINT_CHAR_OP, AsteroideaVisitor.MOVE_RIGHT_OP),
            AsteroideaVisitor.READ_INT_OP: lambda: int(input()),
            AsteroideaVisitor.PRINT_INT_OP: lambda: print(self.current_cell_value(), end=''),
            AsteroideaVisitor.PRINT_MOVE_INT_OP: lambda: self.print_move(AsteroideaVisitor.PRINT_INT_OP, AsteroideaVisitor.MOVE_RIGHT_OP)
        }

        self.bookmarks = {}

        self.reset_tape_vars()

    def reset_tape_vars(self) -> None:
        self.tape_pos = 0

        self.bookmarks = {}
        AsteroideaVisitor.functions = {}
        AsteroideaVisitor.function_vars = [{}]

        self.update_tape_vars()

    def update_tape_vars(self) -> None:
        self.bookmarks['__current'] = self.tape_pos
        self.bookmarks['__first'] = 0
        self.bookmarks['__last'] = len(self.tape) - 1

    def shift_tape_pos(self, amount: int) -> None:
        if (self.tape_pos + amount < 0) or (self.tape_pos + amount >= len(self.tape)):
            print(f"ERROR: Moved to invalid cell {self.tape_pos + amount}")
            sys.exit(1)

        self.tape_pos += amount

    def set_tape_pos(self, pos: int) -> None:

        if pos < 0 or pos >= len(self.tape):
            print(f"ERROR: Invalid cell {pos}")
            sys.exit(1)

        self.tape_pos = pos

    def shift_cell_value(self, amount: int) -> None:
        self.tape[self.tape_pos] += amount
        self.tape[self.tape_pos] %= 0x100

    def current_cell_value(self) -> int:
        return self.tape[self.tape_pos]

    def print_move(self, print_op: str, move_op: str) -> None:
        self.io_ops[print_op]()
        self.move_ops[move_op]()

        return None

    # Params is the names of the parameters
    # args are the values for each parameter
    def set_function_scope(self, params: list = None, args: list = None) -> None:

        if params is None and args is None:
            self.function_vars.append({})
            return

        new_scope = {}
        arg_list = [child for child in args.children[1:-1:2]]

        if len(params) != len(arg_list):
            print("ERROR! Length of parameters must equal length of arguments")
            sys.exit(1)

        for i, param in enumerate(params):
            new_scope['$' + param] = self.visit(arg_list[i])

        self.function_vars.append(new_scope)

    # Visit a parse tree produced by asteroideaParser#repeatStatement.
    def visitRepeatStatement(self, ctx:asteroideaParser.RepeatStatementContext):

        iterations = self.visit(ctx.iterations)

        if ctx.children[1].getText() == '-':
            iterations = len(self.tape) - iterations

        for _ in range(iterations):
            self.visitChildren(ctx.block)

    # Visit a parse tree produced by asteroideaParser#whileStatement.
    def visitWhileStatement(self, ctx:asteroideaParser.WhileStatementContext):
        while self.current_cell_value() != 0:
            self.visitChildren(ctx.block)

        return None

    # Visit a parse tree produced by asteroideaParser#untilStatement.
    def visitUntilStatement(self, ctx:asteroideaParser.UntilStatementContext):
        while self.current_cell_value() == 0:
            self.visitChildren(ctx.block)

        return None

    # Visit a parse tree produced by asteroideaParser#ifStatement.
    def visitIfStatement(self, ctx:asteroideaParser.IfStatementContext):
        if self.current_cell_value() != 0:
            self.visitChildren(ctx.block)

        return None

    # Vsit a parse tree produced by asteroideaParser#unlessStatement.
    def visitUnlessStatement(self, ctx:asteroideaParser.UnlessStatementContext):
        if self.current_cell_value() == 0:
            self.visitChildren(ctx.block)

        return None

    # Visit a parse tree produced by asteroideaParser#functionDefinitionStatement.
    def visitFunctionDefinitionStatement(self, ctx:asteroideaParser.FunctionDefinitionStatementContext):

        params = []

        if ctx.children[2].getText()[0] == '<':
            params = self.visit(ctx.children[2])

        AsteroideaVisitor.functions[ctx.name.text] = _ProgramFunction(params, ctx.block)

        #print(self.functions)

        return None


    # Visit a parse tree produced by asteroideaParser#functionCallStatement.
    def visitFunctionCallStatement(self, ctx:asteroideaParser.FunctionCallStatementContext):
        func_name = ctx.name.text

        if not func_name in AsteroideaVisitor.functions.keys():
            print(f"ERROR! Function {func_name} doesn't exist!")
            sys.exit(1)

        if ctx.children[-1].getText()[0] == '<':
            self.set_function_scope(AsteroideaVisitor.functions[func_name].params, ctx.children[-1])
        else:
            self.set_function_scope()

        self.visitChildren(AsteroideaVisitor.functions[func_name].code)
        self.function_vars.pop()

        #return self.visitChildren(self.functions[func_name])

    # Visit a parse tree produced by asteroideaParser#scope.
    def visitScope(self, ctx:asteroideaParser.ScopeContext):
        return self.visitChildren(ctx)[1:-1]


    # Visit a parse tree produced by asteroideaParser#jumpStatement.
    def visitJumpStatement(self, ctx:asteroideaParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#bookmarkStatement.
    def visitBookmarkStatement(self, ctx:asteroideaParser.BookmarkStatementContext):
        self.bookmarks[ctx.name.text] = self.tape_pos
        return None


    # Visit a parse tree produced by asteroideaParser#jumpToStatement.
    def visitJumpToStatement(self, ctx:asteroideaParser.JumpToStatementContext):
        bookmark = ctx.name.text

        if not bookmark in self.bookmarks.keys():
            print(f"ERROR! Invalid bookmark {bookmark}")
            sys.exit(1)

        self.set_tape_pos(self.bookmarks[bookmark])

    # Visit a parse tree produced by asteroideaParser#moveOp.
    def visitMoveOp(self, ctx:asteroideaParser.MoveOpContext):

        # Call the appropriate function based off of the given operator
        self.move_ops[ctx.op.text]()
        self.update_tape_vars()

        return None

    # Visit a parse tree produced by asteroideaParser#modifyCellOp.
    def visitModifyCellOp(self, ctx:asteroideaParser.ModifyCellOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#increaseOp.
    def visitIncreaseOp(self, ctx:asteroideaParser.IncreaseOpContext):
        val = self.visit(ctx.val)
        self.shift_cell_value(val)

        return None

    # Visit a parse tree produced by asteroideaParser#decreaseOp.
    def visitDecreaseOp(self, ctx:asteroideaParser.DecreaseOpContext):
        val = self.visit(ctx.val)
        self.shift_cell_value(-val)

        return None

    # Visit a parse tree produced by asteroideaParser#setValOp.
    def visitSetValOp(self, ctx:asteroideaParser.SetValOpContext):
        val = self.visit(ctx.val)

        if ctx.children[1].getText() == '-':
            val *= -1

        self.tape[self.tape_pos] = val % 0x100
        return None


    # Visit a parse tree produced by asteroideaParser#ioOp.
    def visitIoOp(self, ctx:asteroideaParser.IoOpContext):
        self.tape[self.tape_pos] = self.io_ops[ctx.op.text]() or self.current_cell_value()
        return None

    # Visit a parse tree produced by asteroideaParser#number.
    def visitNumber(self, ctx:asteroideaParser.NumberContext):

        if ctx.children[0].getText()[0] != '|':
            val = self.visitChildren(ctx)
        else:
            val = 1 if self.visit(ctx.children[1]) else 0

        #print(f"DEBUG: {val}")
        return val if val is not None else int(ctx.getText())

    # Visit a parse tree produced by asteroideaParser#parameterOp.
    def visitParameterOp(self, ctx:asteroideaParser.ParameterOpContext):

        for scope in self.function_vars[::-1]:
            if not '$' + ctx.name.text in scope:
                continue

            return scope['$' + ctx.name.text]

        print(f"ERROR! Invalid argument ${ctx.name.text}")
        sys.exit(1)

    # Visit a parse tree produced by asteroideaParser#defParams.
    def visitDefParams(self, ctx:asteroideaParser.DefParamsContext):
        return [child.getText() for child in ctx.children[1:-1:2]]

    # Visit a parse tree produced by asteroideaParser#callParams.
    def visitCallParams(self, ctx:asteroideaParser.CallParamsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by asteroideaParser#lookupOp.
    def visitLookupOp(self, ctx:asteroideaParser.LookupOpContext):
        bookmark = ctx.name.text

        if not bookmark in self.bookmarks.keys():
            print(f"ERROR! Bookmark {bookmark} does not exist")
            sys.exit(1)

        return self.tape[self.bookmarks[bookmark]]

    # Visit a parse tree produced by asteroideaParser#setTapeCellsOp.
    def visitSetTapeCellsOp(self, ctx:asteroideaParser.SetTapeCellsOpContext):
        self.tape = []
        self.reset_tape_vars()

        for child in ctx.children[1:]:
            self.tape.append(int(child.getText()) % 0x100)

        return None

    # Visit a parse tree produced by asteroideaParser#setTapeLengthOp.
    def visitSetTapeLengthOp(self, ctx:asteroideaParser.SetTapeLengthOpContext):
        self.tape = [int(ctx.values.text) % 0x100] * int(ctx.cells.text)

        return None

    # Visit a parse tree produced by asteroideaParser#setTapeStringOp.
    def visitSetTapeStringOp(self, ctx:asteroideaParser.SetTapeStringOpContext):
        self.tape = [ord(x) for x in ctx.string.text[1:-1]]
        self.reset_tape_vars()

        return None

    # Visit a parse tree produced by asteroideaParser#showTapeBytesOp.
    def visitShowTapeBytesOp(self, ctx:asteroideaParser.ShowTapeBytesOpContext):
        tape = [chr(x) if 31 < x < 127 else f'{hex(x)[1:] :0<3}' for x in self.tape]

        if len(tape) <= MAX_TAPE_DISPLAY_WIDTH:
            TapeVisualizer.visualize(tape, selected_pos=self.tape_pos)
        elif self.tape_pos <= MAX_TAPE_DISPLAY_WIDTH // 2:
            TapeVisualizer.visualize(tape, selected_pos=self.tape_pos, cells=MAX_TAPE_DISPLAY_WIDTH)
        elif self.tape_pos < len(tape) - MAX_TAPE_DISPLAY_WIDTH // 2:
            TapeVisualizer.visualize(tape, selected_pos=self.tape_pos, start=self.tape_pos - MAX_TAPE_DISPLAY_WIDTH // 2, cells=MAX_TAPE_DISPLAY_WIDTH)
        else:
            TapeVisualizer.visualize(tape, selected_pos=self.tape_pos, start=len(self.tape) - MAX_TAPE_DISPLAY_WIDTH)

    # Visit a parse tree produced by asteroideaParser#showTapeValsOp.
    def visitShowTapeValsOp(self, ctx:asteroideaParser.ShowTapeValsOpContext):
        if len(self.tape) <= MAX_TAPE_DISPLAY_WIDTH:
            TapeVisualizer.visualize(self.tape, selected_pos=self.tape_pos)
        elif self.tape_pos <= MAX_TAPE_DISPLAY_WIDTH // 2:
            TapeVisualizer.visualize(self.tape, selected_pos=self.tape_pos, cells=MAX_TAPE_DISPLAY_WIDTH)
        elif self.tape_pos < len(self.tape) - MAX_TAPE_DISPLAY_WIDTH // 2:
            TapeVisualizer.visualize(self.tape, selected_pos=self.tape_pos, start=self.tape_pos - MAX_TAPE_DISPLAY_WIDTH // 2, cells=MAX_TAPE_DISPLAY_WIDTH)
        else:
            TapeVisualizer.visualize(self.tape, selected_pos=self.tape_pos, start=len(self.tape) - MAX_TAPE_DISPLAY_WIDTH)

    # Visit a parse tree produced by asteroideaParser#setVarOp.
    def visitSetVarOp(self, ctx:asteroideaParser.SetVarOpContext):
        self.function_vars[-1]['$' + ctx.name.text] = self.visit(ctx.val)

    # Visit a parse tree produced by asteroideaParser#importStatement.
    def visitImportStatement(self, ctx:asteroideaParser.ImportStatementContext):
        filename = ctx.loc.text[1:-1] # move quotation marks

        if not os.path.exists(filename):
            print(f"ERROR! Invalid importable {filename}")
            sys.exit(1)

        istream = antlr.FileStream(filename)
        lexer = asteroideaLexer(istream)
        stream = antlr.CommonTokenStream(lexer)
        parser = asteroideaParser(stream)
        tree = parser.prog()
        visitor = AsteroideaVisitor()
        visitor.visit(tree)

        self.update_tape_vars()

def run(filename: str) -> None:
    input_stream = antlr.FileStream(filename)
    lexer = asteroideaLexer(input_stream)
    stream = antlr.CommonTokenStream(lexer)
    parser = asteroideaParser(stream)
    tree = parser.prog()

    visitor = AsteroideaVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    run("hello.csr")
