from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
import functools

def flatten(lst):
    ret = []
    for x in lst:
        ret += flatten(x) if isinstance(x,list) else [x]
    return ret
def tobool(str):
    return str == 'true'

class ASTGeneration(MCVisitor):
    def visitProgram(self, ctx:MCParser.ProgramContext):
        mnDecls = self.visit(ctx.manydecls())
        # print('mnDecls =>', mnDecls)
        return Program(mnDecls)

    def visitManydecls(self, ctx:MCParser.ManydeclsContext):
        currentDecl = self.visit(ctx.decl())
        # print(' visitManydecls => ', currentDecl)
        # return [self.visit(ctx.decl())] + self.visit(ctx.mdTail())
        return flatten([currentDecl] + self.visit(ctx.mdTail()))

    def visitMdTail(self, ctx:MCParser.MdTailContext):
        return [self.visit(ctx.decl())] + self.visit(ctx.mdTail()) if ctx.decl() else []
        
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visit(ctx.getChild(0))

    def visitVarDecl(self, ctx:MCParser.VarDeclContext):
        mcType = self.visit(ctx.primitiveType())
        fIdList = self.visit(ctx.varList())
        return [ f(mcType) for f in fIdList ]

    def visitVarList(self, ctx:MCParser.VarListContext):
        return map( lambda x: self.visit(x), ctx.variable())

    def visitPrimitiveType(self, ctx:MCParser.PrimitiveTypeContext):
        if ctx.INTTYPE(): return IntType
        elif ctx.FLOATTYPE(): return FloatType
        elif ctx.BOOLTYPE(): return BoolType
        else: return StringType

    def visitVariable(self, ctx:MCParser.VariableContext):
        return (lambda x: VarDecl(Id(ctx.ID().getText()), x)) if ctx.getChildCount() == 1 else  (lambda x: VarDecl(Id(ctx.ID().getText()), ArrayType(IntLiteral(int(ctx.INTLIT().getText())),x) )  )

    def visitFuncDecl(self, ctx:MCParser.FuncDeclContext):
        funcType = self.visit(ctx.funcType())
        # print('returnType : funcType', funcType)
        funcName = Id(ctx.ID().getText())
        paraList = self.visit(ctx.paraList())
        blockStmt = self.visit(ctx.blockStmt())
        return FuncDecl(funcName, paraList, funcType, blockStmt)

    def visitFuncType(self, ctx:MCParser.FuncTypeContext):
        if ctx.VOIDTYPE():
            return VoidType
        else:
            funcType = ctx.getChild(0)
            # print('PrimitiveTypeContext => ',  funcType.getChildCount())
            if (funcType.getChildCount() == 1):
                # print('PrimitiveTypeContext => ',  self.visit(ctx.getChild(0)))
                return self.visit(ctx.getChild(0))
            else:
                return ArrayPointerType(self.visit(funcType.getChild(0)))

    def visitParaList(self, ctx:MCParser.ParaListContext):
        return [self.visit(ctx.paraDecl())] + self.visit(ctx.paralistTail()) if ctx.paraDecl() else []
    def visitParalistTail(self, ctx:MCParser.ParalistTailContext):
        return [self.visit(ctx.paraDecl())] + self.visit(ctx.paralistTail()) if ctx.paraDecl() else []

    def visitParaDecl(self, ctx:MCParser.ParaDeclContext):
        primitiveType = self.visit(ctx.primitiveType())
        idParam = self.visit(ctx.idParam())
        return idParam(primitiveType)
    
    def visitIdParam(self, ctx:MCParser.IdParamContext):
        if ctx.getChildCount() == 1:
            return (lambda fType: VarDecl(Id(ctx.ID().getText()), fType))
        else:
            return (lambda fType: VarDecl(Id(ctx.ID().getText()), ArrayPointerType(fType)))
    
    def visitBlockStmt(self, ctx:MCParser.BlockStmtContext):
        return self.visit(ctx.blockStmtBody())

    def visitBlockStmtBody(self, ctx:MCParser.BlockStmtBodyContext):
        # flatten Vardecl
        # stmtBlock
        declStmt = self.visit(ctx.declStmt())
        bodyStmt = self.visit(ctx.bodyStmt())
        blockMembers = flatten(declStmt)
        blockMembers += flatten(bodyStmt)

        # print('93 => declStmt', declStmt)
        # print('95 => bodyStmt', bodyStmt)
        return Block(blockMembers)

    def visitDeclStmt(self, ctx:MCParser.DeclStmtContext):
        return [self.visit(x) for x in ctx.varDecl()]
        
    def visitBodyStmt(self, ctx:MCParser.BodyStmtContext):
        return [self.visit(x) for x in ctx.stmt()]

    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visit(ctx.getChild(0))
    
    def visitIfStmt(self, ctx:MCParser.IfStmtContext):
        return self.visit(ctx.getChild(0))

    def visitIfmatch(self, ctx:MCParser.IfmatchContext):
        exp = self.visit(ctx.exp(0))
        thenStmt = self.visit(ctx.stmtmatch(0))
        elseStmt = self.visit(ctx.stmtmatch(1))
        return If(exp, thenStmt, elseStmt)

    def visitStmtmatch(self, ctx:MCParser.StmtmatchContext):
        return self.visit(ctx.getChild(0))

    def visitIfunmatch(self, ctx:MCParser.IfunmatchContext):
        exp = self.visit(ctx.exp(0))
        if ctx.ELSE():
            return If(exp, self.visit(ctx.stmt()), None) 
        else:
            return If(exp, self.visit(ctx.stmtmatch()), self.visit(ctx.stmtunmatch())) 

    def visitStmtunmatch(self, ctx:MCParser.StmtunmatchContext): 
        return self.visit(ctx.getChild(0))

    def visitOtherStmt(self, ctx:MCParser.OtherStmtContext):
        return self.visit(ctx.getChild(0))

    def visitDowhileStmt(self, ctx:MCParser.DowhileStmtContext):
        stmtList = [self.visit(x) for x in ctx.stmt()]
        exp = self.visit(ctx.exp())
        return Dowhile(stmtList,exp)

    def visitForStmt(self, ctx:MCParser.ForStmtContext):
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2))
        loop = [self.visit(x) for x in ctx.stmt()]
        return For(expr1, expr2, expr3, loop)
    
    def visitBreakStmt(self, ctx:MCParser.BreakStmtContext):
        return Break
    
    def visitContinueStmt(self, ctx:MCParser.ContinueStmtContext):
        return Continue
    
    def visitReturnStmt(self, ctx:MCParser.ReturnStmtContext):
        return self.visit(ctx.getChild(0))
    def visitNoExpReturn(self, ctx:MCParser.NoExpReturnContext):
        return Return(None)
    def visitNormalExpReturn(self, ctx:MCParser.NormalExpReturnContext):
        return Return(self.visit(ctx.exp()))
    
    def visitExpStmt(self, ctx:MCParser.ExpStmtContext):
        return self.visit(ctx.exp())
    
    def visitExp(self, ctx:MCParser.ExpContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.OP_ASSIGN().getText(), self.visit(ctx.term1()), self.visit(ctx.exp()))
        else:
            self.visit(ctx.getChild(0))
    
    def visitTerm1(self, ctx:MCParser.Term1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.OP_OR().getText(), self.visit(ctx.term1()), self.visit(ctx.term2()))
        else:
            self.visit(ctx.getChild(0))
    
    def visitTerm2(self, ctx:MCParser.Term2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.OP_AND().getText(), self.visit(ctx.term2()), self.visit(ctx.term3()))
        else:
            self.visit(ctx.getChild(0))
    
    def visitTerm3(self, ctx:MCParser.Term3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.term4(0)), self.visit(ctx.term4(1)))
        else:
            self.visit(ctx.getChild(0))

    def visitTerm4(self, ctx:MCParser.Term4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.term5(0)), self.visit(ctx.term5(1)))
        else:
            self.visit(ctx.getChild(0))

    def visitTerm5(self, ctx:MCParser.Term5Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.term5()), self.visit(ctx.term6()))
        else:
            self.visit(ctx.getChild(0))

    def visitTerm6(self, ctx:MCParser.Term6Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.term6()), self.visit(ctx.term7()))
        else:
            self.visit(ctx.getChild(0))
  
    def visitTerm7(self, ctx:MCParser.Term7Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.term7()))
        else:
            self.visit(ctx.getChild(0))  

    def visitTerm8(self, ctx:MCParser.Term8Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.term7()))
        else:
            self.visit(ctx.getChild(0))  

    def visitExp9(self, ctx:MCParser.Exp9Context):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(tobool(ctx.BOOLLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(tobool(ctx.STRINGLIT().getText()))
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.getChild(0))
    
    def visitIndexExp(self, ctx:MCParser.IndexExpContext):
        indexFirstExp = self.visit(ctx.indexFirstExp())
        exp = self.visit(ctx.exp())
        return ArrayCell(indexFirstExp, exp)
    
    def visitIndexFirstExp(self, ctx:MCParser.IndexFirstExpContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.funcCall())
    
    def visitFuncCall(self, ctx:MCParser.FuncCallContext):
        id = Id(ctx.ID().getText())
        argList = self.visit(ctx.argList())
        return CallExpr(id, argList)

    def visitArgList(self, ctx:MCParser.ArgListContext):
        return [self.visit(ctx.exp())] + self.visit(ctx.argListTail()) if ctx.exp() else []
    def visitArgListTail(self, ctx:MCParser.ArgListTailContext):
        return [self.visit(ctx.exp())] + self.visit(ctx.argListTail()) if ctx.exp() else []
    
    
        