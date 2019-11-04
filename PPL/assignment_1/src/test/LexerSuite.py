import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("mns","mns,<EOF>",101))
    def test_identifier_1(self):
        self.assertTrue(TestLexer.checkLexeme("poiKMs","poiKMs,<EOF>",102))
    def test_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("aA?sVN","aA,Error Token ?",103))
    def test_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",104))
    def test_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("123a 123","123,a,123,<EOF>",105))
    def test_integer_1(self):
        self.assertTrue(TestLexer.checkLexeme("8493","8493,<EOF>",106))
    def test_integer_2(self):
        self.assertTrue(TestLexer.checkLexeme("0034","0034,<EOF>",107))
    def test_integer_3(self):
        self.assertTrue(TestLexer.checkLexeme("345?123","345,Error Token ?",108))
    def test_integer_4(self):
        self.assertTrue(TestLexer.checkLexeme("789~","789,Error Token ~",109))
    def test_integer_5(self):
        self.assertTrue(TestLexer.checkLexeme("293_huy","293,_huy,<EOF>",110))
    
    # float
    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme("1.00", "1.00,<EOF>", 131))
    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme("1e-22","1e-22,<EOF>",132))
    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme("1.0e-12","1.0e-12,<EOF>",133))
    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme("0.0000001","0.0000001,<EOF>",134))
    def test_float_5(self):
        self.assertTrue(TestLexer.checkLexeme("0000000001","0000000001,<EOF>",135))
    def test_float_6(self):
        self.assertTrue(TestLexer.checkLexeme("0.00000001e1e","0.00000001e1,e,<EOF>",136))
    def test_float_7(self):
        self.assertTrue(TestLexer.checkLexeme("1.E12","1.E12,<EOF>",137))
    def test_float_8(self):
        self.assertTrue(TestLexer.checkLexeme(".1E2",".1E2,<EOF>",138))
    def test_float_9(self):
        self.assertTrue(TestLexer.checkLexeme("e-15","e,-,15,<EOF>",139))

    #string
    def test_string_1(self):
        input = """\"string\""""
        self.assertTrue(TestLexer.checkLexeme(input, "\"string\",<EOF>", 151))
    def test_string_2(self):
        input = """\"string huy\""""
        self.assertTrue(TestLexer.checkLexeme(input, "\"string huy\",<EOF>", 152))
    def test_string_3(self):
        input = """\"shiva\b\""""
        self.assertTrue(TestLexer.checkLexeme(input, "Illegal Escape In String: shiva\b", 153))
    def test_string_4(self):
        input = """\"string peter\\b\""""
        self.assertTrue(TestLexer.checkLexeme(input, "\"string peter\\b\",<EOF>", 154))
    def test_string_5(self):
        input = """\"string aa\\r\""""
        self.assertTrue(TestLexer.checkLexeme(input, "\"string aa\\r\",<EOF>", 155))
    def test_string_6(self):
        input = """\"string thanh\\"\""""
        self.assertTrue(TestLexer.checkLexeme(input, "\"string thanh\\\"\",<EOF>", 156))
    def test_string_7(self):
        input = """\"\"\""""
        self.assertTrue(TestLexer.checkLexeme(input,"\"\",Error Token \"", 157))
    def test_string_8(self):
        input = """\"\\\"\""""
        self.assertTrue(TestLexer.checkLexeme(input, "\"\\\"\",<EOF>", 158))