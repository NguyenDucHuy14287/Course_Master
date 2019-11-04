from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import *

def flatten(l):
    return reduce((lambda x, y: x + y if (isinstance(y,list)) else x + [y]), l, [])

class ASTGeneration(MCVisitor):

    def visitProgram(self,ctx:MCParser.ProgramContext): 
        return Program(self.visit(ctx.manydecls()))

    def visitManydecls(self, ctx: MCParser.ManydeclsContext):   
        return flatten(self.visit(ctx.decl()) + self.visit(ctx.tail()))

    def visitTail(self, ctx: MCParser.TailContext): 
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.decl())] + self.visit(ctx.tail())

    def visitDecl(self,ctx:MCParser.DeclContext):
        return self.visit(ctx.getChild(0))

    def visitVardecl(self, ctx: MCParser.VardeclContext):   
        return [varlist(self.visit(ctx.pritype())) for varlist in self.visit(ctx.idlist())]

    def visitIdlist(self, ctx: MCParser.IdlistContext):
        return [self.visit(ctx.varid())] + self.visit(ctx.idlisttail())

    def visitIdlisttail(self, ctx: MCParser.IdlisttailContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.varid())] + self.visit(ctx.idlisttail())

    def visitVarid(self, ctx: MCParser.VaridContext):
        if ctx.getChildCount() == 1:
            var = lambda mcType: VarDecl(ctx.ID().getText(), mcType)
        else:
            var = lambda mcType: VarDecl(ctx.ID().getText(),  ArrayType(IntLiteral(int(ctx.INTLIT().getText())), mcType))

        return var

    def visitPritype(self, ctx: MCParser.PritypeContext):
        if ctx.BOOLEAN():
            priType = BoolType
        elif ctx.INT():
            priType = IntType
        elif ctx.FLOAT():
            priType = FloatType
        elif ctx.STRING():
            priType = StringType

        return priType

    def visitFuncdecl(self, ctx: MCParser.FuncdeclContext): 
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.paramdecl())
        returnType = self.visit(ctx.functionType())
        body = self.visit(ctx.body())

        return [FuncDecl(name,param,returnType,body)]

    def visitFunctionType(self, ctx: MCParser.FunctionTypeContext):
        if ctx.pritype():
            functype = self.visit(ctx.pritype())
        elif ctx.VOID():
            functype = VoidType
        else:
            functype = self.visit(ctx.array_pointer_type())

        return functype

    def visitArray_pointer_type(self, ctx: MCParser.Array_pointer_typeContext):
        eleType = self.visit(ctx.pritype())
        return ArrayPointerType(eleType)

    def visitParamdecl(self, ctx: MCParser.ParamdeclContext): 
        return self.visit(ctx.listparams())

    def visitListparams(self, ctx: MCParser.ListparamsContext): 
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.oneparam())] + self.visit(ctx.listparamstail())

    def visitListparamstail(self, ctx: MCParser.ListparamstailContext): 
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.oneparam())] + self.visit(ctx.listparamstail())

    def visitOneparam(self, ctx: MCParser.OneparamContext):
        if ctx.RSB():
            varType = ArrayPointerType(self.visit(ctx.pritype()))
        else:
            varType = self.visit(ctx.pritype())

        variable = Id(ctx.ID().getText())
        return VarDecl(variable,varType)    

    def visitBody(self, ctx: MCParser.BodyContext): 
        return Block(flatten(self.visit(ctx.bodylist())))

    def visitBodylist(self, ctx: MCParser.BodylistContext): 
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.onebody())] + self.visit(ctx.bodytail())

    def visitBodytail(self, ctx: MCParser.BodytailContext): 
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.onebody())] + self.visit(ctx.bodytail())

    def visitOnebody(self, ctx: MCParser.OnebodyContext): 
        return self.visit(ctx.getChild(0))

    def visitStmt(self, ctx: MCParser.StmtContext): 
        return self.visit(ctx.getChild(0))

    def visitIfStmt(self, ctx: MCParser.IfStmtContext): 
        return self.visit(ctx.getChild(0))

    def visitMatchIf(self, ctx: MCParser.MatchIfContext): 
        expr = self.visit(ctx.exp())
        thenStmt = self.visit(ctx.match_stmt(0))
        elseStmt = self.visit(ctx.match_stmt(1))

        return If(expr,thenStmt,elseStmt)

    def visitMatch_stmt(self, ctx: MCParser.Match_stmtContext): 
        return self.visit(ctx.getChild(0))

    def visitUnmatchIf(self, ctx: MCParser.UnmatchIfContext): 
        if ctx.ELSE():
            expr = self.visit(ctx.exp())
            thenStmt = self.visit(ctx.match_stmt())
            elseStmt = self.visit(ctx.unmatch_stmt())
        else:
            expr = self.visit(ctx.exp())
            thenStmt = self.visit(ctx.stmt())
            elseStmt = None

        return If(expr,thenStmt,elseStmt)

    def visitUnmatch_stmt(self, ctx: MCParser.Unmatch_stmtContext): 
        return self.visit(ctx.getChild(0))

    def visitOther_stmt(self, ctx: MCParser.Other_stmtContext): 
        return self.visit(ctx.getChild(0))

    def visitForStmt(self, ctx: MCParser.ForStmtContext): 
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2))
        loop = self.visit(ctx.stmt())

        return For(expr1,expr2,expr3,loop)

    def visitDoWhileStmt(self, ctx: MCParser.DoWhileStmtContext): 
        sl = [self.visit(ctx.stmt())]
        exp = self.visit(ctx.exp())

        return Dowhile(flatten(sl),exp)

    def visitBreakStmt(self, ctx: MCParser.BreakStmtContext): 
        return Break()

    def visitContinueStmt(self, ctx: MCParser.ContinueStmtContext): 
        return Continue()

    def visitReturnStmt(self, ctx: MCParser.ReturnStmtContext): 
        expr = self.visit(ctx.exp())

        return Return(expr)

    def visitExpStmt(self, ctx: MCParser.ExpStmtContext): 
        return self.visit(ctx.exp())

    def visitExp(self, ctx: MCParser.ExpContext): 
        if ctx.ASSIGN():
            op = ctx.ASSIGN().getText()
            left = self.visit(ctx.term1())
            right = self.visit(ctx.exp())
            exp = BinaryOp(op,left,right)
        else:
            exp = self.visit(ctx.getChild(0))

        return exp

    def visitTerm1(self, ctx: MCParser.Term1Context): 
        if ctx.OR():
            op = ctx.OR().getText()
            left = self.visit(ctx.term1())
            right = self.visit(ctx.term2())
            term1 = BinaryOp(op,left,right)
        else:
            term1 = self.visit(ctx.getChild(0))

        return term1

    def visitTerm2(self, ctx: MCParser.Term2Context): 
        if ctx.AND():
            op = ctx.AND().getText()
            left = self.visit(ctx.term2())
            right = self.visit(ctx.term3())
            term2 = BinaryOp(op,left,right)
        else:
            term2 = self.visit(ctx.getChild(0))

        return term2

    def visitTerm3(self, ctx: MCParser.Term3Context): 
        if ctx.EQUAL():
            op = ctx.EQUAL().getText()
            left = self.visit(ctx.term4(0))
            right = self.visit(ctx.term4(1))
            term3 = BinaryOp(op,left,right)
        elif ctx.NOT_EQUAL():
            op = ctx.NOT_EQUAL().getText()
            left = self.visit(ctx.term4(0))
            right = self.visit(ctx.term4(1))
            term3 = BinaryOp(op,left,right)
        else:
            term3 = self.visit(ctx.getChild(0))

        return term3

    def visitTerm4(self, ctx: MCParser.Term4Context): 
        if ctx.LESS():
            op = ctx.LESS().getText()
            left = self.visit(ctx.term5(0))
            right = self.visit(ctx.term5(1))
            term4 = BinaryOp(op,left,right)
        elif ctx.LESS_OR_EQUAL():
            op = ctx.LESS_OR_EQUAL().getText()
            left = self.visit(ctx.term5(0))
            right = self.visit(ctx.term5(1))
            term4 = BinaryOp(op,left,right)
        elif ctx.GREATER():
            op = ctx.GREATER().getText()
            left = self.visit(ctx.term5(0))
            right = self.visit(ctx.term5(1))
            term4 = BinaryOp(op,left,right)
        elif ctx.GREATER_OR_EQUAL():
            op = ctx.GREATER_OR_EQUAL().getText()
            left = self.visit(ctx.term5(0))
            right = self.visit(ctx.term5(1))
            term4 = BinaryOp(op,left,right)
        else:
            term4 = self.visit(ctx.getChild(0))

        return term4

    def visitTerm5(self, ctx: MCParser.Term5Context):
        if ctx.ADD():
            op = ctx.ADD().getText()
            left = self.visit(ctx.term5())
            right = self.visit(ctx.term6())
            term5 = BinaryOp(op,left,right)
        elif ctx.SUB():
            op = ctx.SUB().getText()
            left = self.visit(ctx.term5())
            right = self.visit(ctx.term6())
            term5 = BinaryOp(op,left,right)
        else:
            term5 = self.visit(ctx.getChild(0))

        return term5

    def visitTerm6(self, ctx: MCParser.Term6Context): 
        if ctx.MUL():
            op = ctx.MUL().getText()
            left = self.visit(ctx.term6())
            right = self.visit(ctx.term7())
            term6 = BinaryOp(op,left,right)
        elif ctx.DIV():
            op = ctx.DIV().getText()
            left = self.visit(ctx.term6())
            right = self.visit(ctx.term7())
            term6 = BinaryOp(op,left,right)
        elif ctx.MOD():
            op = ctx.MOD().getText()
            left = self.visit(ctx.term6())
            right = self.visit(ctx.term7())
            term6 = BinaryOp(op,left,right)
        else:
            term6 = self.visit(ctx.getChild(0))

        return term6

    def visitTerm7(self, ctx: MCParser.Term7Context): 
        if ctx.SUB():
            op = ctx.SUB().getText()
            body = self.visit(ctx.term7())
            term7 = UnaryOp(op,body)
        elif ctx.NOT():
            op = ctx.NOT().getText()
            body = self.visit(ctx.term7())
            term7 = UnaryOp(op,body)
        else:
            term7 = self.visit(ctx.getChild(0))
        return term7

    def visitTerm8(self, ctx: MCParser.Term8Context): 
        if ctx.exp():
            term8 = self.visit(ctx.exp())
        else:
            term8 = self.visit(ctx.getChild(0))

        return term8

    def visitTerm9(self, ctx: MCParser.Term9Context): 
        if ctx.indexExp():
            term9 = self.visit(ctx.indexExp())
        elif ctx.funcCall():
            term9 = self.visit(ctx.funcCall())
        elif ctx.BOOLEANLIT():
            term9 = BooleanLiteral(ctx.BOOLEANLIT().getText() == "true")
        elif ctx.INTLIT():
            term9 = IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            term9 = FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            term9 = StringLiteral(ctx.STRINGLIT().getText())
        else:
            term9 = Id(ctx.ID().getText())

        return term9

    def visitIndexExp(self, ctx: MCParser.IndexExpContext): 
        arr = self.visit(ctx.indexFirstExp())
        idx = self.visit(ctx.exp())
        return ArrayCell(arr,idx)

    def visitIndexFirstExp(self, ctx: MCParser.IndexFirstExpContext): 
        if ctx.funcCall():
            firstexp = self.visit(ctx.funcCall())
        else:
            firstexp = Id(ctx.ID().getText())

        return firstexp

    def visitFuncCall(self, ctx: MCParser.FuncCallContext): 
        method = Id(ctx.ID().getText())
        param = flatten(self.visit(ctx.explist()))

        return CallExpr(method,param)

    def visitExplist(self, ctx: MCParser.ExplistContext): 
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.exp())] + self.visit(ctx.explisttail())

    def visitExplisttail(self, ctx: MCParser.ExplisttailContext): 
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.exp())] + self.visit(ctx.explisttail())
    
    