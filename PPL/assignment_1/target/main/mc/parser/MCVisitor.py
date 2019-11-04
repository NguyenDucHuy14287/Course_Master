# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#manydecls.
    def visitManydecls(self, ctx:MCParser.ManydeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#tail.
    def visitTail(self, ctx:MCParser.TailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardecl.
    def visitVardecl(self, ctx:MCParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idlist.
    def visitIdlist(self, ctx:MCParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idlisttail.
    def visitIdlisttail(self, ctx:MCParser.IdlisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#varid.
    def visitVarid(self, ctx:MCParser.VaridContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcdecl.
    def visitFuncdecl(self, ctx:MCParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paramdecl.
    def visitParamdecl(self, ctx:MCParser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#listparams.
    def visitListparams(self, ctx:MCParser.ListparamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#listparamstail.
    def visitListparamstail(self, ctx:MCParser.ListparamstailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#oneparam.
    def visitOneparam(self, ctx:MCParser.OneparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#body.
    def visitBody(self, ctx:MCParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#bodylist.
    def visitBodylist(self, ctx:MCParser.BodylistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#bodytail.
    def visitBodytail(self, ctx:MCParser.BodytailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#onebody.
    def visitOnebody(self, ctx:MCParser.OnebodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifStmt.
    def visitIfStmt(self, ctx:MCParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#matchIf.
    def visitMatchIf(self, ctx:MCParser.MatchIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#unmatchIf.
    def visitUnmatchIf(self, ctx:MCParser.UnmatchIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forStmt.
    def visitForStmt(self, ctx:MCParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:MCParser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakStmt.
    def visitBreakStmt(self, ctx:MCParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continueStmt.
    def visitContinueStmt(self, ctx:MCParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnStmt.
    def visitReturnStmt(self, ctx:MCParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expStmt.
    def visitExpStmt(self, ctx:MCParser.ExpStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term1.
    def visitTerm1(self, ctx:MCParser.Term1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term2.
    def visitTerm2(self, ctx:MCParser.Term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term3.
    def visitTerm3(self, ctx:MCParser.Term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term4.
    def visitTerm4(self, ctx:MCParser.Term4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term5.
    def visitTerm5(self, ctx:MCParser.Term5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term6.
    def visitTerm6(self, ctx:MCParser.Term6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term7.
    def visitTerm7(self, ctx:MCParser.Term7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term8.
    def visitTerm8(self, ctx:MCParser.Term8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term9.
    def visitTerm9(self, ctx:MCParser.Term9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcCall.
    def visitFuncCall(self, ctx:MCParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#explist.
    def visitExplist(self, ctx:MCParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#explisttail.
    def visitExplisttail(self, ctx:MCParser.ExplisttailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#functionType.
    def visitFunctionType(self, ctx:MCParser.FunctionTypeContext):
        return self.visitChildren(ctx)



del MCParser