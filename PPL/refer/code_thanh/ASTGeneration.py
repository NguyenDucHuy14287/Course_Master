from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext): #ok
        return Program(self.visit(ctx.manyDeclarations()))

    def visitManyDeclarations(self, ctx: MCParser.ManyDeclarationsContext): #check
        # return [self.visit(declaration) for declaration in ctx.declaration()]
        return self.visit(ctx.declaration()[0])             

    def visitDeclaration(self, ctx: MCParser.DeclarationContext):   #ok
        if ctx.variableDeclaration():
            declaration = self.visit(ctx.variableDeclaration())
        else:
            declaration = self.visit(ctx.functionDeclaration())

        return declaration

    def visitVariableDeclaration(self, ctx: MCParser.VariableDeclarationContext):   #check
        return [variableList(self.visit(ctx.primitiveType())) for variableList in self.visit(ctx.variableList())]

    def visitVariableList(self, ctx: MCParser.VariableListContext):
        return [self.visit(variable) for variable in ctx.variable()]

    def visitVariable(self, ctx: MCParser.VariableContext):
        if ctx.INT_LIT():
            variableDeclaration = lambda mcType: VarDecl(ctx.ID().getText(), ArrayType(int(ctx.INT_LIT()), mcType))
        else:
            variableDeclaration = lambda mcType: VarDecl(ctx.ID().getText(), mcType)

        return variableDeclaration

    def visitPrimitiveType(self, ctx: MCParser.PrimitiveTypeContext):
        if ctx.BOOLEAN_TYPE():
            mcType = BoolType()
        elif ctx.INT_TYPE():
            mcType = IntType()
        elif ctx.FLOAT_TYPE():
            mcType = FloatType()
        elif ctx.STRING_TYPE():
            mcType = StringType()

        return mcType
        


