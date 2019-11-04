import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_declare_1(self):
        input = """int a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_declare_2(self):
        input = """float a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_declare_3(self):
        input = """boolean a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_declare_4(self):
        input = """string a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_declare_5(self):
        input = """string a,b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_declare_6(self):
        input = """string a,b,c[3];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_function_1(self):
        input = """int main (int a) {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_function_2(self):
        input = """int main (int a, int b) {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_function_3(self):
        input = """int main (int a, int b) {
            putIntLn(4);
            a = 10;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_if_1(self):
        input = """int main(){
        if (a==b) {
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_if_2(self):
        input = """int main(){
        if (a==b) {
            a = 23;
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_if_3(self):
        input = """int main(){
        if (a==b) {
            a = 23;
        }
        else {

        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_if_4(self):
        input = """int main(){
        if (a==b) {
            a = 23;
        }
        else {
            b = 109;
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_if_5(self):
        input = """int main(){
        if (a==b) {
             if (c==d){
                 a = 0;
             }
        }
        else if (c==d) {
            b = 0;
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_if_6(self):
        input = """int main(){
        if (a==b) {
             if (c==d){
                 a = 0;
             }
        }
        else if (c==d) {
            if (c==d){
                 a = 0;
             }
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_if_7(self):
        input = """int main(){
        if (a==b) {
             if (c==d){
                 a = 0;
             }
             else {

             }
        }
        else if (c==d) {
            if (c==d){
                 a = 0;
             }
             else if (a>=c){

             }
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_if_8(self):
        input = """int main(){
        if (a==b) {
             if (c==d){
                 a = 0;
             }
             else if (0!=2){
                d = a + b;
             }
        }
        else if (c==d) {
            if (e==d){
                 a = 0;
             }
             else if (a>=c){
                 if (c==2){
                     
                 }
             }
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_if_9(self):
        input = """int main(){
        if (a==b)
            if (c==d)
                a = a + 3;
        else 
            a = 4;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_if_10(self):
        input = """int main(){
        if (a==b)
            if (c==e[4])
                a = a + 3;
        else 
            a = 4;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_fail_1(self):
        input = """void main(int){
            putlin(1);
        }"""
        expect = "Error on line 1 col 13: )"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_fail_2(self):
        input = """main(int x){
            
        }"""
        expect = "Error on line 1 col 0: main"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_fail_3(self):
        input = """void main(int x,y){
            
        }"""
        expect = "Error on line 1 col 16: y"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_fail_4(self):
        input = """void main(int x, int y){
            void a;
        }"""
        expect = "Error on line 2 col 12: void"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_fail_5(self):
        input = """void main(int x, int y){
            if {

            }
            else
        }"""
        expect = "Error on line 2 col 15: {"
        self.assertTrue(TestParser.checkParser(input,expect,227))