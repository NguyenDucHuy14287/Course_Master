import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType,Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,300))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType,Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    # def test_call_without_parameter(self):
    #     """More complex program"""
    #     input = """int main () {
    #         getIntLn();
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType,Block([CallExpr(Id("getIntLn"),[])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,302))

    # def test_simple_variable_declaration(self):
    #     """Simple program: int main() {} """
    #     input = """int a;"""
    #     expect = str(Program([VarDecl("a",IntType)]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,303))

    # def test_simple_variable_declaration_have_multiple_var(self):
    #     """Simple program: int main() {} """
    #     input = """int a,b,c;"""
    #     expect = str(Program([VarDecl(str("a"),IntType),VarDecl(str("b"),IntType),VarDecl(str("c"),IntType)]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,304))

    # def test_simple_multiple_variable_declaration(self):
    #     """Simple program: int main() {} """
    #     input = """int a;int b;"""
    #     expect = str(Program([VarDecl("a",IntType),VarDecl("b",IntType)]))
    #     # expect = """Program([VarDecl(a,IntType),VarDecl(b,IntType)])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,305))

    # def test_simple_multiple_variable_declaration_have_multiple_var(self):
    #     """Simple program: int main() {} """
    #     input = """int a,b,c;int d,e;"""
    #     expect = str(Program([VarDecl("a",IntType),VarDecl("b",IntType),VarDecl("c",IntType),VarDecl("d",IntType),VarDecl("e",IntType)]))
    #     # expect = """Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),VarDecl(d,IntType),VarDecl(e,IntType)])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,306))

    # def test_simple_array_variable_declaration(self):
    #     """Simple program: int main() {} """
    #     input = """int a[5];"""
    #     expect = str(Program([VarDecl("a",ArrayType(5, IntType))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,307))

    # def test_simple_array_variable_declaration_have_multiple_var(self):
    #     """Simple program: int main() {} """
    #     input = """int a,b,c[3];"""
    #     expect = str(Program([VarDecl("a",IntType),VarDecl("b",IntType),VarDecl("c",ArrayType(3,IntType))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,308))

    # def test_simple_array_multiple_variable_declaration(self):
    #     """Simple program: int main() {} """
    #     input = """int a[2];int b[4];"""
    #     expect = str(Program([VarDecl("a",ArrayType(2, IntType)),VarDecl("b",ArrayType(4, IntType))]))
    #     # expect = """Program([VarDecl(a,ArrayType(IntType,2)),VarDecl(b,ArrayType(IntType,4))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,309))

    # def test_simple_array_multiple_variable_declaration_have_multiple_var(self):
    #     """Simple program: int main() {} """
    #     input = """int a,b[2],c;int d,e[2];"""
    #     expect = str(Program([VarDecl("a",IntType),VarDecl("b",ArrayType(2, IntType)),VarDecl("c",IntType),VarDecl("d",IntType),VarDecl("e",ArrayType(2, IntType))]))
    #     # expect = """Program([VarDecl(a,IntType),VarDecl(b,ArrayType(IntType,2)),VarDecl(c,IntType),VarDecl(d,IntType),VarDecl(e,ArrayType(IntType,2))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,310))

    # def test_simple_int_function_declaration(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType,Block([]))]))
    #     # expect = """Program([FuncDecl(Id(main),[],IntType,Block([]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,311))

    # def test_simple_bool_function_declaration(self):
    #     """Simple program: boolean main() {} """
    #     input = """boolean main() {}"""
    #     expect = str(Program([FuncDecl(Id("main"),[],BoolType,Block([]))]))
    #     # expect = """Program([FuncDecl(Id(main),[],BoolType,Block([]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,312))

    # def test_simple_float_function_declaration(self):
    #     """Simple program: float main() {} """
    #     input = """float main() {}"""
    #     expect = str(Program([FuncDecl(Id("main"),[],FloatType,Block([]))]))
    #     # expect = """Program([FuncDecl(Id(main),[],FloatType,Block([]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,313))

    # def test_simple_string_function_declaration(self):
    #     """Simple program: string main() {} """
    #     input = """string main() {}"""
    #     expect = str(Program([FuncDecl(Id("main"),[],StringType,Block([]))]))
    #     # expect = """Program([FuncDecl(Id(main),[],StringType,Block([]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,314))

    # def test_simple_array_int_function_declaration(self):
    #     """Simple program: int[] main() {} """
    #     input = """int[] main() {}"""
    #     expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(IntType),Block([]))]))
    #     # expect = """Program([FuncDecl(Id(main),[],ArrayPointerType(IntType),Block([]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,315))

    # def test_simple_array_float_function_declaration(self):
    #     """Simple program: float[] main() {} """
    #     input = """float[] main() {}"""
    #     expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(FloatType),Block([]))]))
    #     # expect = """Program([FuncDecl(Id(main),[],ArrayPointerType(IntType),Block([]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,316))

    # def test_simple_array_string_function_declaration(self):
    #     """Simple program: string[] main() {} """
    #     input = """string[] main() {}"""
    #     expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(StringType),Block([]))]))
    #     # expect = """Program([FuncDecl(Id(main),[],ArrayPointerType(IntType),Block([]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,317))

    # def test_simple_array_bool_function_declaration(self):
    #     """Simple program: int[] main() {} """
    #     input = """boolean[] main() {}"""
    #     expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(BoolType),Block([]))]))
    #     # expect = """Program([FuncDecl(Id(main),[],ArrayPointerType(IntType),Block([]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,318))

    # def test_simple_int_function_declaration_assign_bool(self):
    #     """Simple program: int[] main() {} """
    #     input = """int main() {a=true;}"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType,Block([BinaryOp("=",Id("a"),BooleanLiteral(True))]))]))
    #     # expect = """Program([FuncDecl(Id(main),[],ArrayPointerType(IntType),Block([]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,319))

    # def test_simple_if_statment(self):
    #     input = """
    #     void main() {
    #         if (a == b) {
    #             print(a);
    #         }
    #     }
    #     """
    #     expect = str(Program(
    #       [FuncDecl(
    #         Id("main"),
    #         [],
    #         VoidType,
    #         Block(
    #             [If(
    #               BinaryOp("==",Id("a"),Id("b")),
    #               Block(
    #                 [CallExpr(Id("print"), [Id("a")])]
    #               ),
    #               None
    #             )]
    #         )
    #       )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    # def test_expression_associativity_unary_right(self):
    #     input = """
    #     void main() {
    #         a = -!a;
    #     }
    #     """
    #     expect = str(Program(
    #       [FuncDecl(
    #         Id("main"),
    #         [],
    #         VoidType,
    #         Block(
    #             [BinaryOp(
    #               "=",
    #               Id("a"),
    #               UnaryOp(
    #                 "-",
    #                 UnaryOp(
    #                 "!",
    #                 Id("a")
    #                 )
    #               )
    #             )]
    #         )
    #       )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    # def test_expression_associativity_mul_left(self):
    #     input = """
    #     void main() {
    #         a = a * b / c % d * f;
    #     }
    #     """
    #     expect = str(Program(
    #       [FuncDecl(
    #         Id("main"),
    #         [],
    #         VoidType,
    #         Block(
    #             [BinaryOp(
    #               "=",
    #               Id("a"),
    #               BinaryOp(
    #                 "*",
    #                 BinaryOp(
    #                   "%",
    #                   BinaryOp(
    #                     "/",
    #                     BinaryOp("*", Id("a"), Id("b")),
    #                     Id("c")
    #                   ),
    #                   Id("d")
    #                 ),
    #                 Id("f")
    #               )
    #             )]
    #         )
    #       )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    # def test_expression_associativity_add_left(self):
    #     input = """
    #     void main() {
    #         a = a + b - c - d + f;
    #     }
    #     """
    #     expect = str(Program(
    #       [FuncDecl(
    #         Id("main"),
    #         [],
    #         VoidType,
    #         Block(
    #             [BinaryOp(
    #               "=",
    #               Id("a"),
    #               BinaryOp(
    #                 "+",
    #                 BinaryOp(
    #                   "-",
    #                   BinaryOp(
    #                     "-",
    #                     BinaryOp("+", Id("a"), Id("b")),
    #                     Id("c")
    #                   ),
    #                   Id("d")
    #                 ),
    #                 Id("f")
    #               )
    #             )]
    #         )
    #       )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    # def test_expression_associativity_and_left(self):
    #     input = """
    #     void main() {
    #         a = a && b && c;
    #     }
    #     """
    #     expect = str(Program(
    #       [FuncDecl(
    #         Id("main"),
    #         [],
    #         VoidType,
    #         Block(
    #             [BinaryOp(
    #               "=",
    #               Id("a"),
    #               BinaryOp(
    #                 "&&",
    #                 BinaryOp("&&",Id("a"),Id("b")),
    #                 Id("c")
    #               )
    #             )]
    #         )
    #       )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    # def test_expression_associativity_or_left(self):
    #     input = """
    #     void main() {
    #         a = a || b || c;
    #     }
    #     """
    #     expect = str(Program(
    #       [FuncDecl(
    #         Id("main"),
    #         [],
    #         VoidType,
    #         Block(
    #             [BinaryOp(
    #               "=",
    #               Id("a"),
    #               BinaryOp(
    #                 "||",
    #                 BinaryOp(
    #                   "||",
    #                   Id("a"),
    #                   Id("b")
    #                 ),
    #                 Id("c")
    #               )
    #             )]
    #         )
    #       )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    # def test_expression_associativity_assign_right(self):
    #     input = """
    #     void main() {
    #         a = b = c;
    #     }
    #     """
    #     expect = str(Program(
    #       [FuncDecl(
    #         Id("main"),
    #         [],
    #         VoidType,
    #         Block(
    #             [BinaryOp(
    #               "=",
    #               Id("a"),
    #               BinaryOp("=",Id("b"),Id("c"))
    #             )]
    #         )
    #       )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    # def test_expression_associativity_assign_with_another_op_right(self):
    #     input = """
    #     void main() {
    #         a = b + c = d;
    #     }
    #     """
    #     expect = str(Program(
    #       [FuncDecl(
    #         Id("main"),
    #         [],
    #         VoidType,
    #         Block(
    #             [BinaryOp(
    #               "=",
    #               Id("a"),
    #               BinaryOp(
    #                 "=",
    #                 BinaryOp("+", Id("b"), Id("c")),
    #                 Id("d")
    #               )
    #             )]
    #         )
    #       )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    # def test_expression_associativity_more_assign_right(self):
    #     input = """
    #     void main() {
    #         a = b = c = d;
    #     }  
    #     """
    #     expect = str(Program(
    #       [FuncDecl(
    #         Id("main"),
    #         [],
    #         VoidType,
    #         Block(
    #             [BinaryOp(
    #               "=",
    #               Id("a"),
    #               BinaryOp(
    #                 "=",
    #                 Id("b"),
    #                 BinaryOp("=", Id("c"), Id("d"))
    #               )
    #             )]
    #         )
    #       )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    # def test_boolean_literal_simple(self):
    #     input = """
    #     void main() {
    #         a = true;
    #     }
    #     """
    #     expect = str(Program(
    #             [FuncDecl(
    #                 Id("main"),
    #                 [],
    #                 VoidType,
    #                 Block(
    #                     [BinaryOp(
    #                         "=",
    #                         Id("a"),
    #                         BooleanLiteral(True)
    #                     )]
    #                 )
    #             )]
    #         ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    # def test_assign_string_literal_simple(self):
    #     """Simple program: int main() {} """
    #     input = """int main(){
    #         a = "a";
    #     }"""
    #     expect = str(Program
    #         ([FuncDecl(
    #             Id("main"),
    #             [],
    #             IntType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     StringLiteral("a"))
    #                 ]
    #             )
    #         )
    #     ]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,330))

    # def test_simple_function_declaration(self):
    #     input = """void print(string s){}"""
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("print"),
    #             [VarDecl(
    #                 "s",
    #                 StringType
    #             )],
    #             VoidType,
    #             Block([])
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    # def test_global_var_and_function_declaration(self):
    #     input = """int a; void print(string s){}"""
    #     expect = str(Program(
    #         [VarDecl(
    #             "a",
    #             IntType
    #         ),
    #         FuncDecl(
    #             Id("print"),
    #             [VarDecl(
    #                 "s",
    #                 StringType
    #             )],
    #             VoidType,
    #             Block([])
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    # def test_global_var_and_function_declaration_more_complex(self):
    #     input = """int a, b[1]; void print(float f[], string s){} string s;"""
    #     expect = str(Program(
    #         [VarDecl(
    #             "a",
    #             IntType
    #         ),
    #         VarDecl(
    #             "b",
    #             ArrayType(1, IntType)
    #         ),
    #         FuncDecl(
    #             Id("print"),
    #             [VarDecl(
    #                 "f",
    #                 ArrayPointerType(FloatType)
    #             ),
    #             VarDecl(
    #                 "s",
    #                 StringType
    #             )],
    #             VoidType,
    #             Block([])
    #         ),
    #         VarDecl(
    #             "s",
    #             StringType
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    # def test_function_definition_only_funcall(self):
    #     input = """void print(string s) {putLine(s);}"""
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("print"),
    #             [VarDecl(
    #                 "s",
    #                 StringType
    #             )],
    #             VoidType,
    #             Block([
    #                 CallExpr(
    #                 Id("putLine"),
    #                 [Id("s")])
    #             ])
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    # def test_function_definition_only_var_declaration(self):
    #     input = """void main() {float a[1]; int b, c[1];}"""
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block([
    #                 VarDecl("a", ArrayType(1, FloatType)),
    #                 VarDecl("b", IntType),
    #                 VarDecl("c", ArrayType(1, IntType))
    #             ])
    #         )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    # def test_function_definition_var_declaration_and_funcall(self):
    #     input = """void main() {float a[1]; int b, c[1]; print(a);}"""
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block([
    #                 VarDecl("a", ArrayType(1, FloatType)),
    #                 VarDecl("b", IntType),
    #                 VarDecl("c", ArrayType(1, IntType)),
    #                 CallExpr(
    #                     Id("print"),
    #                     [Id("a")]
    #                 )
    #             ])
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    # def test_simple_BinaryOp(self):
    #     input = """void main() {a + b;}"""
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp("+", Id("a"), Id("b"))]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    # def test_simple_UnaryOp(self):
    #     input = """void main() {-b;}"""
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [UnaryOp("-", Id("b"))]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    # def test_simple_if_else_statment(self):
    #     input = """
    #     void main() {
    #         if (a > b) {print(a);} else {print(b);}
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [If(
    #                     BinaryOp(">",Id("a"),Id("b")),
    #                     Block(
    #                         [CallExpr(Id("print"), [Id("a")])]
    #                     ),
    #                     Block(
    #                         [CallExpr(Id("print"), [Id("b")])]
    #                     )
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    # def test_simple_do_while_statment(self):
    #     input = """
    #     void main() {
    #         do {
    #             print(a);
    #             a = a + 1;
    #         } while (a > b);
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [Dowhile(
    #                 [Block(
    #                     [CallExpr(Id("print"), [Id("a")]),
    #                     BinaryOp(
    #                         "=",
    #                         Id("a"),
    #                         BinaryOp("+", Id("a"), IntLiteral(1))
    #                     )]
    #                 )],
    #                 BinaryOp(">",Id("a"),Id("b"))
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    # def test_nested_if_else(self):
    #     input = """
    #     void main() {
    #         if (a > b)
    #             if (b > c)
    #                 print(a);
    #             else
    #                 print(b);
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [If(
    #                     BinaryOp(">", Id("a"), Id("b")),
    #                     If(
    #                         BinaryOp(">", Id("b"), Id("c")),
    #                         CallExpr(Id("print"), [Id("a")]),
    #                         CallExpr(Id("print"), [Id("b")])
    #                     ),
    #                     None
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    # def test_nested_if_else_with_square_bracket(self):
    #     input = """
    #     void main() {
    #         if (a > b) {
    #             if (b > c)
    #                 print(a);
    #         }
    #         else
    #             print(b);
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [If(
    #                     BinaryOp(">", Id("a"), Id("b")),
    #                     Block(
    #                         [If(
    #                             BinaryOp(">", Id("b"), Id("c")),
    #                             CallExpr(Id("print"), [Id("a")]),
    #                             None
    #                         )]
    #                     ),
    #                     CallExpr(Id("print"), [Id("b")])
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    # def test_simple_expression_statement(self):
    #     input = """
    #     void main() {
    #         a = a + b + c;
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     BinaryOp(
    #                         "+",
    #                         BinaryOp(
    #                             "+",
    #                             Id("a"),
    #                             Id("b")
    #                         ),
    #                         Id("c")
    #                     )
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    # def test_expression_precedence_addop_and_mulop(self):
    #     input = """
    #     void main() {
    #         a = a + b * c;
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     BinaryOp(
    #                         "+",
    #                         Id("a"),
    #                         BinaryOp(
    #                             "*",
    #                             Id("b"),
    #                             Id("c")
    #                         )
    #                     )
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    # def test_expression_precedence_addop_mulop_addop(self):
    #     input = """
    #     void main() {
    #         a = a + b * c - d;
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     BinaryOp(
    #                         "-",
    #                         BinaryOp(
    #                             "+",
    #                             Id("a"),
    #                             BinaryOp(
    #                                 "*",
    #                                 Id("b"),
    #                                 Id("c")
    #                             )
    #                         ),
    #                         Id("d")
    #                     )
    #                 )]
    #             )
    #         )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    # def test_expression_precedence_and_or_and(self):
    #     input = """
    #     void main() {
    #         a = a && b || c && d;
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     BinaryOp(
    #                         "||",
    #                         BinaryOp(
    #                             "&&",
    #                             Id("a"),
    #                             Id("b")
    #                         ),
    #                         BinaryOp(
    #                             "&&",
    #                             Id("c"),
    #                             Id("d")
    #                         )
    #                     )
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    # def test_expression_precedence_equal_and_equal(self):
    #     input = """
    #     void main() {
    #         a = a == b && c != d;
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     BinaryOp(
    #                         "&&",
    #                         BinaryOp(
    #                         "==",
    #                         Id("a"),
    #                         Id("b")
    #                         ),
    #                         BinaryOp(
    #                         "!=",
    #                         Id("c"),
    #                         Id("d")
    #                         )
    #                     )
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    # def test_expression_precedence_compare_equal_compare(self):
    #     input = """
    #     void main() {
    #         a = a >= b == c <= d;
    #     }
    #     """
    #     expect =  str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     BinaryOp(
    #                         "==",
    #                         BinaryOp(
    #                             ">=",
    #                             Id("a"),
    #                             Id("b")
    #                         ),
    #                         BinaryOp(
    #                             "<=",
    #                             Id("c"),
    #                             Id("d")
    #                         )
    #                     )
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    # def test_expression_precedence_add_compare_add(self):
    #     input = """
    #     void main() {
    #         a = a + b < c - d;
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     BinaryOp(
    #                         "<",
    #                         BinaryOp(
    #                             "+",
    #                             Id("a"),
    #                             Id("b")
    #                         ),
    #                         BinaryOp(
    #                             "-",
    #                             Id("c"),
    #                             Id("d")
    #                         )
    #                     )
    #                 )]
    #             )
    #         )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    # def test_expression_precedence_mul_add_mul(self):
    #     input = """
    #     void main() {
    #         a = a / b - c % d;
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     BinaryOp(
    #                         "-",
    #                         BinaryOp(
    #                             "/",
    #                             Id("a"),
    #                             Id("b")
    #                         ),
    #                         BinaryOp(
    #                             "%",
    #                             Id("c"),
    #                             Id("d")
    #                         )
    #                     )
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    # def test_expression_precedence_unary_mul_unary(self):
    #     input = """
    #     void main() {
    #         a = !b * -c;
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     BinaryOp(
    #                         "*",
    #                         UnaryOp(
    #                             "!",
    #                             Id("b")
    #                         ),
    #                         UnaryOp(
    #                             "-",
    #                             Id("c")
    #                         )
    #                     )
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    # def test_expression_precedence_unary_exp_in_bracket(self):
    #     input = """
    #     void main() {
    #         a = !(b * -c);
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     UnaryOp(
    #                         "!",
    #                         BinaryOp(
    #                             "*",
    #                             Id("b"),
    #                             UnaryOp(
    #                                 "-",
    #                                 Id("c")
    #                             )
    #                         )
    #                     )
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    # def test_expression_precedence_unary_funcall(self):
    #     input = """
    #     void main() {
    #         a = -putInLine(s);
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     UnaryOp(
    #                         "-",
    #                         CallExpr(
    #                         Id("putInLine"),
    #                         [Id("s")]
    #                         )
    #                     )
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    # def test_expression_precedence_unary_array_cell(self):
    #     input = """
    #     void main() {
    #         a = -putInLine(s)[a+b];
    #     }
    #     """
    #     expect = str(Program(
    #         [FuncDecl(
    #             Id("main"),
    #             [],
    #             VoidType,
    #             Block(
    #                 [BinaryOp(
    #                     "=",
    #                     Id("a"),
    #                     UnaryOp(
    #                         "-",
    #                         ArrayCell(
    #                             CallExpr(
    #                                 Id("putInLine"),
    #                                 [Id("s")]
    #                             ),
    #                             UnaryOp(
    #                                 "[]",
    #                                 BinaryOp(
    #                                     "+",
    #                                     Id("a"),
    #                                     Id("b")
    #                                 )
    #                             )
    #                         )
    #                     )
    #                 )]
    #             )
    #         )]
    #     ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    # def test_expression_precedence_unary_literal(self):
    #     input = """
    #     void main() {
    #         a = -"putInLine(s)[a+b]";
    #     }
    #     """
    #     expect = str(Program(
    #       [FuncDecl(
    #         Id("main"),
    #         [],
    #         VoidType,
    #         Block(
    #             [BinaryOp(
    #               "=",
    #               Id("a"),
    #               UnaryOp(
    #                 "-",
    #                 StringLiteral("putInLine(s)[a+b]")
    #               )
    #             )]
    #         )
    #       )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_expression_precedence_binary_arraycell(self):
        input = """
        void main() {
            a = a - b[a+b];
        }
        """
        expect = str(Program(
          [FuncDecl(
            Id("main"),
            [],
            VoidType,
            Block(
                [BinaryOp(
                  "=",
                  Id("a"),
                  BinaryOp(
                    "-",
                    Id("a"),
                    ArrayCell(
                      Id("b"),
                      UnaryOp(
                          "[]",
                        BinaryOp("+", Id("a"), Id("b"))
                      )
                    )
                  )
                )]
            )
          )]
      ))
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    # def test_expression_precedence_binary_arraycell_with_bracket(self):
    #     input = """
    #     void main() {
    #         a = a - (b / c)[a+b];
    #     }
    #     """
    #     expect = str(Program(
    #       [FuncDecl(
    #         Id("main"),
    #         [],
    #         VoidType,
    #         Block(
    #             [BinaryOp(
    #               "=",
    #               Id("a"),
    #               BinaryOp(
    #                 "-",
    #                 Id("a"),
    #                 ArrayCell(
    #                   BinaryOp("/", Id("b"), Id("c")),
    #                   UnaryOp(
    #                     "[]",
    #                     BinaryOp("+", Id("a"), Id("b"))
    #                   )
    #                 )
    #               )
    #             )]
    #         )
    #       )]
    #   ))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    
   