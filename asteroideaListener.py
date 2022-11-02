# Generated from asteroidea.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .asteroideaParser import asteroideaParser
else:
    from asteroideaParser import asteroideaParser

# This class defines a complete listener for a parse tree produced by asteroideaParser.
class asteroideaListener(ParseTreeListener):

    # Enter a parse tree produced by asteroideaParser#prog.
    def enterProg(self, ctx:asteroideaParser.ProgContext):
        pass

    # Exit a parse tree produced by asteroideaParser#prog.
    def exitProg(self, ctx:asteroideaParser.ProgContext):
        pass


    # Enter a parse tree produced by asteroideaParser#stmt.
    def enterStmt(self, ctx:asteroideaParser.StmtContext):
        pass

    # Exit a parse tree produced by asteroideaParser#stmt.
    def exitStmt(self, ctx:asteroideaParser.StmtContext):
        pass


    # Enter a parse tree produced by asteroideaParser#haltOp.
    def enterHaltOp(self, ctx:asteroideaParser.HaltOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#haltOp.
    def exitHaltOp(self, ctx:asteroideaParser.HaltOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#debugOp.
    def enterDebugOp(self, ctx:asteroideaParser.DebugOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#debugOp.
    def exitDebugOp(self, ctx:asteroideaParser.DebugOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#importStatement.
    def enterImportStatement(self, ctx:asteroideaParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#importStatement.
    def exitImportStatement(self, ctx:asteroideaParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#showTapeBytesOp.
    def enterShowTapeBytesOp(self, ctx:asteroideaParser.ShowTapeBytesOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#showTapeBytesOp.
    def exitShowTapeBytesOp(self, ctx:asteroideaParser.ShowTapeBytesOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#showTapeValsOp.
    def enterShowTapeValsOp(self, ctx:asteroideaParser.ShowTapeValsOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#showTapeValsOp.
    def exitShowTapeValsOp(self, ctx:asteroideaParser.ShowTapeValsOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#setTapeOp.
    def enterSetTapeOp(self, ctx:asteroideaParser.SetTapeOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#setTapeOp.
    def exitSetTapeOp(self, ctx:asteroideaParser.SetTapeOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#setTapeCellsOp.
    def enterSetTapeCellsOp(self, ctx:asteroideaParser.SetTapeCellsOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#setTapeCellsOp.
    def exitSetTapeCellsOp(self, ctx:asteroideaParser.SetTapeCellsOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#setTapeLengthOp.
    def enterSetTapeLengthOp(self, ctx:asteroideaParser.SetTapeLengthOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#setTapeLengthOp.
    def exitSetTapeLengthOp(self, ctx:asteroideaParser.SetTapeLengthOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#setTapeStringOp.
    def enterSetTapeStringOp(self, ctx:asteroideaParser.SetTapeStringOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#setTapeStringOp.
    def exitSetTapeStringOp(self, ctx:asteroideaParser.SetTapeStringOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#setVarOp.
    def enterSetVarOp(self, ctx:asteroideaParser.SetVarOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#setVarOp.
    def exitSetVarOp(self, ctx:asteroideaParser.SetVarOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#modifyVarOp.
    def enterModifyVarOp(self, ctx:asteroideaParser.ModifyVarOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#modifyVarOp.
    def exitModifyVarOp(self, ctx:asteroideaParser.ModifyVarOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#incrementVarOp.
    def enterIncrementVarOp(self, ctx:asteroideaParser.IncrementVarOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#incrementVarOp.
    def exitIncrementVarOp(self, ctx:asteroideaParser.IncrementVarOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#decrementVarOp.
    def enterDecrementVarOp(self, ctx:asteroideaParser.DecrementVarOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#decrementVarOp.
    def exitDecrementVarOp(self, ctx:asteroideaParser.DecrementVarOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#loopStatement.
    def enterLoopStatement(self, ctx:asteroideaParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#loopStatement.
    def exitLoopStatement(self, ctx:asteroideaParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#repeatStatement.
    def enterRepeatStatement(self, ctx:asteroideaParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#repeatStatement.
    def exitRepeatStatement(self, ctx:asteroideaParser.RepeatStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#whileStatement.
    def enterWhileStatement(self, ctx:asteroideaParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#whileStatement.
    def exitWhileStatement(self, ctx:asteroideaParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#untilStatement.
    def enterUntilStatement(self, ctx:asteroideaParser.UntilStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#untilStatement.
    def exitUntilStatement(self, ctx:asteroideaParser.UntilStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:asteroideaParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:asteroideaParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#ifStatement.
    def enterIfStatement(self, ctx:asteroideaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#ifStatement.
    def exitIfStatement(self, ctx:asteroideaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#unlessStatement.
    def enterUnlessStatement(self, ctx:asteroideaParser.UnlessStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#unlessStatement.
    def exitUnlessStatement(self, ctx:asteroideaParser.UnlessStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#functionStatement.
    def enterFunctionStatement(self, ctx:asteroideaParser.FunctionStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#functionStatement.
    def exitFunctionStatement(self, ctx:asteroideaParser.FunctionStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#functionDefinitionStatement.
    def enterFunctionDefinitionStatement(self, ctx:asteroideaParser.FunctionDefinitionStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#functionDefinitionStatement.
    def exitFunctionDefinitionStatement(self, ctx:asteroideaParser.FunctionDefinitionStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#functionCallStatement.
    def enterFunctionCallStatement(self, ctx:asteroideaParser.FunctionCallStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#functionCallStatement.
    def exitFunctionCallStatement(self, ctx:asteroideaParser.FunctionCallStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#scope.
    def enterScope(self, ctx:asteroideaParser.ScopeContext):
        pass

    # Exit a parse tree produced by asteroideaParser#scope.
    def exitScope(self, ctx:asteroideaParser.ScopeContext):
        pass


    # Enter a parse tree produced by asteroideaParser#jumpStatement.
    def enterJumpStatement(self, ctx:asteroideaParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#jumpStatement.
    def exitJumpStatement(self, ctx:asteroideaParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#bookmarkStatement.
    def enterBookmarkStatement(self, ctx:asteroideaParser.BookmarkStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#bookmarkStatement.
    def exitBookmarkStatement(self, ctx:asteroideaParser.BookmarkStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#jumpToStatement.
    def enterJumpToStatement(self, ctx:asteroideaParser.JumpToStatementContext):
        pass

    # Exit a parse tree produced by asteroideaParser#jumpToStatement.
    def exitJumpToStatement(self, ctx:asteroideaParser.JumpToStatementContext):
        pass


    # Enter a parse tree produced by asteroideaParser#moveOp.
    def enterMoveOp(self, ctx:asteroideaParser.MoveOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#moveOp.
    def exitMoveOp(self, ctx:asteroideaParser.MoveOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#modifyCellOp.
    def enterModifyCellOp(self, ctx:asteroideaParser.ModifyCellOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#modifyCellOp.
    def exitModifyCellOp(self, ctx:asteroideaParser.ModifyCellOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#increaseOp.
    def enterIncreaseOp(self, ctx:asteroideaParser.IncreaseOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#increaseOp.
    def exitIncreaseOp(self, ctx:asteroideaParser.IncreaseOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#decreaseOp.
    def enterDecreaseOp(self, ctx:asteroideaParser.DecreaseOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#decreaseOp.
    def exitDecreaseOp(self, ctx:asteroideaParser.DecreaseOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#setValOp.
    def enterSetValOp(self, ctx:asteroideaParser.SetValOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#setValOp.
    def exitSetValOp(self, ctx:asteroideaParser.SetValOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#ioOp.
    def enterIoOp(self, ctx:asteroideaParser.IoOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#ioOp.
    def exitIoOp(self, ctx:asteroideaParser.IoOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#parameterOp.
    def enterParameterOp(self, ctx:asteroideaParser.ParameterOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#parameterOp.
    def exitParameterOp(self, ctx:asteroideaParser.ParameterOpContext):
        pass


    # Enter a parse tree produced by asteroideaParser#defParams.
    def enterDefParams(self, ctx:asteroideaParser.DefParamsContext):
        pass

    # Exit a parse tree produced by asteroideaParser#defParams.
    def exitDefParams(self, ctx:asteroideaParser.DefParamsContext):
        pass


    # Enter a parse tree produced by asteroideaParser#callParams.
    def enterCallParams(self, ctx:asteroideaParser.CallParamsContext):
        pass

    # Exit a parse tree produced by asteroideaParser#callParams.
    def exitCallParams(self, ctx:asteroideaParser.CallParamsContext):
        pass


    # Enter a parse tree produced by asteroideaParser#numLiteral.
    def enterNumLiteral(self, ctx:asteroideaParser.NumLiteralContext):
        pass

    # Exit a parse tree produced by asteroideaParser#numLiteral.
    def exitNumLiteral(self, ctx:asteroideaParser.NumLiteralContext):
        pass


    # Enter a parse tree produced by asteroideaParser#numParam.
    def enterNumParam(self, ctx:asteroideaParser.NumParamContext):
        pass

    # Exit a parse tree produced by asteroideaParser#numParam.
    def exitNumParam(self, ctx:asteroideaParser.NumParamContext):
        pass


    # Enter a parse tree produced by asteroideaParser#numLookup.
    def enterNumLookup(self, ctx:asteroideaParser.NumLookupContext):
        pass

    # Exit a parse tree produced by asteroideaParser#numLookup.
    def exitNumLookup(self, ctx:asteroideaParser.NumLookupContext):
        pass


    # Enter a parse tree produced by asteroideaParser#numParen.
    def enterNumParen(self, ctx:asteroideaParser.NumParenContext):
        pass

    # Exit a parse tree produced by asteroideaParser#numParen.
    def exitNumParen(self, ctx:asteroideaParser.NumParenContext):
        pass


    # Enter a parse tree produced by asteroideaParser#numNormalize.
    def enterNumNormalize(self, ctx:asteroideaParser.NumNormalizeContext):
        pass

    # Exit a parse tree produced by asteroideaParser#numNormalize.
    def exitNumNormalize(self, ctx:asteroideaParser.NumNormalizeContext):
        pass


    # Enter a parse tree produced by asteroideaParser#numExpr.
    def enterNumExpr(self, ctx:asteroideaParser.NumExprContext):
        pass

    # Exit a parse tree produced by asteroideaParser#numExpr.
    def exitNumExpr(self, ctx:asteroideaParser.NumExprContext):
        pass


    # Enter a parse tree produced by asteroideaParser#lookupOp.
    def enterLookupOp(self, ctx:asteroideaParser.LookupOpContext):
        pass

    # Exit a parse tree produced by asteroideaParser#lookupOp.
    def exitLookupOp(self, ctx:asteroideaParser.LookupOpContext):
        pass



del asteroideaParser