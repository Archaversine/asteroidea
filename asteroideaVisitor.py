# Generated from asteroidea.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .asteroideaParser import asteroideaParser
else:
    from asteroideaParser import asteroideaParser

# This class defines a complete generic visitor for a parse tree produced by asteroideaParser.

class asteroideaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by asteroideaParser#prog.
    def visitProg(self, ctx:asteroideaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#stmt.
    def visitStmt(self, ctx:asteroideaParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#haltOp.
    def visitHaltOp(self, ctx:asteroideaParser.HaltOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#allocOp.
    def visitAllocOp(self, ctx:asteroideaParser.AllocOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#debugOp.
    def visitDebugOp(self, ctx:asteroideaParser.DebugOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#importStatement.
    def visitImportStatement(self, ctx:asteroideaParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#showTapeBytesOp.
    def visitShowTapeBytesOp(self, ctx:asteroideaParser.ShowTapeBytesOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#showTapeValsOp.
    def visitShowTapeValsOp(self, ctx:asteroideaParser.ShowTapeValsOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#setTapeOp.
    def visitSetTapeOp(self, ctx:asteroideaParser.SetTapeOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#setTapeCellsOp.
    def visitSetTapeCellsOp(self, ctx:asteroideaParser.SetTapeCellsOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#setTapeLengthOp.
    def visitSetTapeLengthOp(self, ctx:asteroideaParser.SetTapeLengthOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#setTapeStringOp.
    def visitSetTapeStringOp(self, ctx:asteroideaParser.SetTapeStringOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#setTapeFileOp.
    def visitSetTapeFileOp(self, ctx:asteroideaParser.SetTapeFileOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#outStringOp.
    def visitOutStringOp(self, ctx:asteroideaParser.OutStringOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#setVarOp.
    def visitSetVarOp(self, ctx:asteroideaParser.SetVarOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#modifyVarOp.
    def visitModifyVarOp(self, ctx:asteroideaParser.ModifyVarOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#incrementVarOp.
    def visitIncrementVarOp(self, ctx:asteroideaParser.IncrementVarOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#decrementVarOp.
    def visitDecrementVarOp(self, ctx:asteroideaParser.DecrementVarOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#loopStatement.
    def visitLoopStatement(self, ctx:asteroideaParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#repeatStatement.
    def visitRepeatStatement(self, ctx:asteroideaParser.RepeatStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#whileStatement.
    def visitWhileStatement(self, ctx:asteroideaParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#untilStatement.
    def visitUntilStatement(self, ctx:asteroideaParser.UntilStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:asteroideaParser.ConditionalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#ifStatement.
    def visitIfStatement(self, ctx:asteroideaParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#unlessStatement.
    def visitUnlessStatement(self, ctx:asteroideaParser.UnlessStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#functionStatement.
    def visitFunctionStatement(self, ctx:asteroideaParser.FunctionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#funcDefNoParams.
    def visitFuncDefNoParams(self, ctx:asteroideaParser.FuncDefNoParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#funcDefWithParams.
    def visitFuncDefWithParams(self, ctx:asteroideaParser.FuncDefWithParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#funcCallNoParams.
    def visitFuncCallNoParams(self, ctx:asteroideaParser.FuncCallNoParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#funcCallWithParams.
    def visitFuncCallWithParams(self, ctx:asteroideaParser.FuncCallWithParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#scope.
    def visitScope(self, ctx:asteroideaParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#jumpStatement.
    def visitJumpStatement(self, ctx:asteroideaParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#bookmarkStatement.
    def visitBookmarkStatement(self, ctx:asteroideaParser.BookmarkStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#jumpToStatement.
    def visitJumpToStatement(self, ctx:asteroideaParser.JumpToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#moveOp.
    def visitMoveOp(self, ctx:asteroideaParser.MoveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#modifyCellOp.
    def visitModifyCellOp(self, ctx:asteroideaParser.ModifyCellOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#increaseOp.
    def visitIncreaseOp(self, ctx:asteroideaParser.IncreaseOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#decreaseOp.
    def visitDecreaseOp(self, ctx:asteroideaParser.DecreaseOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#setValOp.
    def visitSetValOp(self, ctx:asteroideaParser.SetValOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#ioOp.
    def visitIoOp(self, ctx:asteroideaParser.IoOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#parameterOp.
    def visitParameterOp(self, ctx:asteroideaParser.ParameterOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#defParams.
    def visitDefParams(self, ctx:asteroideaParser.DefParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#callParams.
    def visitCallParams(self, ctx:asteroideaParser.CallParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#numLiteral.
    def visitNumLiteral(self, ctx:asteroideaParser.NumLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#numParam.
    def visitNumParam(self, ctx:asteroideaParser.NumParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#numChar.
    def visitNumChar(self, ctx:asteroideaParser.NumCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#numLookup.
    def visitNumLookup(self, ctx:asteroideaParser.NumLookupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#numParen.
    def visitNumParen(self, ctx:asteroideaParser.NumParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#numNormalize.
    def visitNumNormalize(self, ctx:asteroideaParser.NumNormalizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#numExpr.
    def visitNumExpr(self, ctx:asteroideaParser.NumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asteroideaParser#lookupOp.
    def visitLookupOp(self, ctx:asteroideaParser.LookupOpContext):
        return self.visitChildren(ctx)



del asteroideaParser