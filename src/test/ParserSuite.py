import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))
    #vardecl
    def test_vardecl(self):
        """var dec"""
        input = """
        x: integer = 65;
        main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_vardecl2(self):
        """many var dec
        """
        input = """x: void; y: float = 6.42; z: auto; k: boolean = false;"""
        expect = "Error on line 1 col 3: void"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_var3(self):
        input = """ z: string = "bool" ; z: integer = 123_3_3;
        main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_var4(self):
        input = """0_h: string = "boll";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, "Error on line 1 col 0: 0", 204)) 
    def test_var5(self):
        input = """main: function void() {
            x:integer = 21;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_var6(self):
        input = """main: function void() {
            x:integer = "hung;"}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,"Error on line 2 col 31: }", 206))
    
    def test_var7(self):
        """unclose string"""
        input = """main: function void() {x:string = "huk  ;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,"huk  ;}", 207))
    
    #function test
    
    def test_func1(self):
        """function
        """
        input = """
        x: integer = 65;
        fact: function integer (n: integer){
            if (n==0) return 1;
            else return n * fact(n-1);
        }
        main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_func2(self):
        """function
        """
        input = """
        x: integer = 65;
        fact: function integer (n: integer){
            if (n==0) return 1;
            else return n * fact(n-1);
        }
        inc: function void (out n : integer, delta: integer){
            n = n +delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x,delta);
            printInteger(x);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_func3(self):
        input = """main: function void() {
            r, s: integer;
            r = 2.0;
            a, b: array [5] of integer;
            s = r * r * myPI;
            a[0] = s;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_var8(self):
        """count number of id and exp """
        input = """main: function void() {
            x,y,z: integer = 1,2;}"""
        expect = "Error on line 2 col 32: ;"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_rand(self):
        input = """x,f_2: integer = 3,2; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212)) 
    #expression
    def test_exp1(self):
        input = """main: function void() {
            x,y: float = 1.334, 1_342.2e+4;
            n: float = x+y*y;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_exp2(self):
        input = """main: function void() {
            x,y: float = 1.334, 1_342.2e+4;
            n: float = x+y*y-2/x +y%7;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_exp3(self):
        input = """main: function void() {
            y= zda[0];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    #statement
    def test_stmt(self):
        input = """main: function void() {
            x= epando(x) *5;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_stmt2(self):
        input = """main: function auto() {
            z= "hello" + "world";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_stmt3(self):
        input = """main: function void() {
            if(z==y) return sum(0);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_stmt4(self):
        input = """main: function auto() {
            z[1,3]= "hello" + "world";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test_stmt5(self):
        input = """main: function auto() {
            z[1,3]= y[z];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test_stmt6(self):
        input = """main: function auto() {
            z[1,3]= {1,3,3};
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_stmt7(self):
        input = """main: function void() {
            for(i=0, i<10, i+1){ writeInt(i);}
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_stmt8(self):
        input = """main: function void() {
            for(i=1+3, i<10, i+1){ writeInt(i);}
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_stmt8_2(self):
        input = """main: function void() {
            for(i=11+4, (i<8) && (i>6), i+2-0.5){ writeInt(i);}
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_stmt9_1(self):
        input = """main: function void() {
            while(hung3 == 1000){
                writeln("Hello mother fker");
                hung3= hung3 +100;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_stmt9(self):
        input = """main: function void() {
            while(funcz(5)!=3){
                writeln("Hello mother fker");
                hung3= hung3 +100;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_stmt10(self):
        input = """main: function void() {
            while(funcz(5)!=3){
                writeln("Hello mother fker");
                hung3= [1];
                continue;
            }
            }"""
        expect = "Error on line 4 col 23: ["
        self.assertTrue(TestParser.test(input, expect, 227))
    
    def test_stmt11(self):
        input = """main: function void() {
            while(funcz(5)!=3){
                writeln("Hello mother fker");
                hung3= hung3 +100;
                continue;break;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_stmt12(self):
        input = """main: function void() {
            do { write("hello");}
            while (n<11);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test_stmt13(self):
        input = """main: function void() {
            do  write("hello");
            while (n<11);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, "Error on line 2 col 16: write", 230))
    def test_stmt13_2(self):
        input = """main: function void() {
           do { write("hello");}
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, "Error on line 4 col 12: }", 231))
    def test_stmt14(self):
        input = """main: function void() {while (n<11); }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, "Error on line 1 col 35: ;", 232))
    def test_stmt15(self):
        input = """main: function void() { goo(); }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_stmt16(self):
        input = """main: function void() { foo(3+x, 4.0/y); }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_stmt17(self):
        input = """main: function void() { foo(3+x, 4.0/y) }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, "Error on line 1 col 40: }", 235))
    
    def test_rand2(self):
        input = """main: function void() {
            x: array [2,3] of string = {1,2 ,3};
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_rand3(self):
        input = """main: function void() {
            x: array [2,3] of string = {1___3.e3,"2" ,"3",33_3};
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    
    # WTF is this testcase
    # def test_rand4(self):
    #     input = """main: function void() {
    #         x: array [2,3] of string = {1,"h ,3};
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, "h ,3};", 238))
    def test_rand5(self):
        input = """main: function void() {
            x: array [2,3] of string = {1,"\h ",3};
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, "\h", 239))
    def test_rand6(self):
        input = """main: function void() {
            x;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, "Error on line 2 col 13: ;", 240))
    def test_rand7(self):
        input = """main: function void() {
            a[1+2]=b[3-3];
            : integer;
            }"""
        expect = "Error on line 3 col 12: :"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_rand8(self):
        input = """main: function void() {
            "I run out of idea";}"""
        expect = "Error on line 2 col 12: I run out of idea"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_rand9(self):
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_rand10(self):
        input = """main: function void() {
            readInteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_rand11(self):
        input = """main: function void() {
            printInteger(1234);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_rand12(self):
        input = """main: function void() {
            readFloat();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
   
    def test_case_247(self):
        input = """main: function void() {
        var a: real;
        a = 3.14159265359;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, "Error on line 2 col 12: a", 247))
    def test_case_248(self):
        input = """main: function void() {
        for i:=1 to 10 do {
        if i = 3 then break;
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, "Error on line 2 col 12: i", 248))
    def test_function_declaration(self):
        input = """add: function integer (a: integer, b: integer)"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, "Error on line 1 col 46: <EOF>", 249))
    def test_function_declaration_with_inheritance(self):
        input = """sub: function integer (a: integer, b: integer) inherit add {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_function_declaration_missing_colon(self):
        input = """add function integer (a: integer, b: integer)"""
        expect = "Error on line 1 col 4: function"
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_function_declaration_missing_parameter_list(self):
        input = """add: function integer"""
        expect = "Error on line 1 col 21: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_function_declaration_missing_return_type(self):
        input = """add: function (a: integer, b: integer)"""
        expect = "Error on line 1 col 14: ("
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_function_declaration_missing_round_brackets(self):
        input = """add: function integer a: integer, b: integer"""
        expect = "Error on line 1 col 22: a"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_function_declaration_missing_function_keyword(self):
        """it will think it is a var dec"""
        input = """addz : integer (a: integer, b: integer)"""
        expect = "Error on line 1 col 15: ("
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_index_operator_3(self):
        input = """main: function void() {
            a[21];}"""
        expect = "Error on line 2 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 256))


    # def test_index_operator_4(self):
    #     input = "arr[3"
    #     expect = "Error on line 1 col 3: ["
    #     self.assertTrue(TestParser.test(input, expect, 257))
    def test_function_call_4(self):
        input = """main: function void() {
            q(,);}"""
        expect = "Error on line 2 col 14: ,"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_rand59(self):
        input = """main: function void() {
            a > b || c < d && e >= f}"""
        expect = "Error on line 2 col 14: >"
        self.assertTrue(TestParser.test(input, expect, 259))
    #! change
    def test_rand60(self):
        input = """main: function void() { a= a > b || c < d && e >= f;}"""
        expect = "Error on line 1 col 38: <"
        self.assertTrue(TestParser.test(input, expect, 260))
    def test_rand61(self):
        input = """main: function void() {a= a && ;}"""
        expect = "Error on line 1 col 31: ;"
        self.assertTrue(TestParser.test(input, expect, 261))
    def test_rand63(self):
        input = """main: function integer() {
        a = 5;
        b = 7;
        return a + b;
    }"""
        # Hung successfully
        expect = "Error on line 1 col 15: integer"
        self.assertTrue(TestParser.test(input, expect, 262))
    def test_r1(self):
        input = """foo: function boolean(x: integer, y: array [2] of float) {
        for (i = 0, i < x,  i + 1) {
            y[i] = i * 2.0;
        }
        return true;
    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    def test_ran4(self):
        input = """bar: function void() {
            if (x > y) {
                print("x is greater than y");
            }
            else if (y > x) {
                print("y is greater than x");
            }
            else {
                print("x and y are equal");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
    def test_rad5(self):
        input = """baz: function float(x: float, y: float) {
            if (x > y) {
                return x;
            }
            else {
                return y;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
    def test_rand266(self):
        input = """foo: function void() { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
    # Function call?
    # def test_rand267(self):
    #     input = """foo(): int { return 1; }"""
    #     expect = "Error on line 1 col 3: ("
    #     self.assertTrue(TestParser.test(input, expect, 267))
    # def test_rand268(self):
    #     input = """foo() { }"""
    #     expect = "Error on line 1 col 3: ("
    #     self.assertTrue(TestParser.test(input, expect, 268))
    def test_ra1nd(self):
        input = """foo: function integer() {
             x: integer = 1;
            y: integer = 2;
            return x + y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_ran2(self):
        input = """foo: function void() {
            x: integer = 1;
            if (x == 1) {
                putInt(x);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
    # def test_ra3(self):
    #     input = """foo: function boolean() {
    #          x: boolean = true;
    #          y: boolean = false;
    #         return x && y || !x && !y;
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 271))
    def test_ra4(self):
        input = """foo: function string() {
             x: string = "hello";
             y: string = "world";
            return x + " " + y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test_ran5(self):
        input = """foo: function float() {
             x: float = 1.0;
             y: float = 2.0;
            return x / y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    def test_ran6(self):
        input = """foo: function boolean(x: boolean) {
            return !x;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test_ran7(self):
        input = """foo: function integer(x: integer, y: integer) {
            if (x > y) {
                return x - y;
            }
            else {
                return y - x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    def test_ran9(self):
        input = """foo: function boolean(x: integer, y: integer) {
            return x == y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_ran10_3(self):
        input = """foo: function boolean(x: integer, y: integer) {
            id= break;
        }"""
        expect = "Error on line 2 col 16: break"
        self.assertTrue(TestParser.test(input, expect, 276))
        
    def test_ran10(self):
        input = """foo: function integer(x: integer) {
            return x * x;
        }

        bar: function integer(x: integer) {
            return foo(x) + foo(x + 1);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    def test_ran11(self):
        input = """foo: function void() {

            for (i = 0, i < x, i = i + 1) {
                putInt(i);
            }
        }"""
        expect = "Error on line 3 col 33: ="
        self.assertTrue(TestParser.test(input, expect, 279))
    
    def test_case_280(self):
        input = """
             x: array [2] of integer ;
            function main(): integer;
            begin
                writeln(x[0][1]);
                writeln(x[1][2]);
                return 0;
            end
        """
        expect = "Error on line 3 col 12: function"
        self.assertTrue(TestParser.test(input, expect, 280))
    def test_case_281(self):
        input = """
             x: array [2] of integer ;
            function main(): integer{;
                writeln(x[0]);
                writeln(x[x[0]]);
                return 0;
            }
        """
        expect = "Error on line 3 col 12: function"
        self.assertTrue(TestParser.test(input, expect, 281))
    def test_case282(self):
        input = """main: function void() {
            x= z::y;
            z= a[1] + a[2];}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
    def test_case283(self):
        input = """main: function void() {
            x= z::y;
            preventDefault() = x;
            }"""
        expect = "Error on line 3 col 29: ="
        self.assertTrue(TestParser.test(input, expect, 283))
    def test_case284(self):
        input = """main: function void() {
            x= z::y;
            hello(funtion());
            z: array[2] of integer = {};}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test_case285(self):
        input = """main: function void() {
            x= z::y;
            a[1]= 27[1];}"""
        expect = "Error on line 3 col 20: ["
        self.assertTrue(TestParser.test(input, expect, 285))
    def test_case_286(self):
        input = "x: integer;\nbegin\nx := -5;\nend."
        expect = "Error on line 3 col 0: x"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_case_287(self):
        input = "x, y: integer;\n\nx : 10;\ny : x + 20;"
        expect = "Error on line 3 col 4: 10"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_case_288(self):
        input = "x: integer;\nfunction foo(a, b: integer): integer;\nbegin\nreturn a + b;\nend\nbegin\nx := foo(10, 20);\nend."
        expect = "Error on line 2 col 0: function"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_289(self):
        input = """main: function void() {
            x,y,z,1: integer = 1,2,3,4;
            }"""
        expect = "Error on line 2 col 18: 1"
        self.assertTrue(TestParser.test(input, expect, 289))
    def test_290(self):
        input = """main: function void() {
            x,y,z,foo(): integer = 1,2,3,4;
            }"""
        expect = "Error on line 2 col 21: ("
        self.assertTrue(TestParser.test(input, expect, 290))
    def test_291(self):
        input = """main: function void() {
            x,y,z: integer = 1,2,{1,2,2};
            {a=3;}
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
    def test_292(self):
        input = """main: function void() {
            x,y,z: integer = 1,2;
            }"""
        expect = "Error on line 2 col 32: ;"
        self.assertTrue(TestParser.test(input, expect, 292))
    def test_293(self):
        input = """main: function void() {
            x,y,z,t: integer = 1,2,3,4,5;
            }"""
        expect = "Error on line 2 col 38: ,"
        self.assertTrue(TestParser.test(input, expect, 293))
    def test_294(self):
        input = """main: function void() {
            x: array [3.3] of float;
            }"""
        expect = "Error on line 2 col 22: 3.3"
        self.assertTrue(TestParser.test(input, expect, 294))
    def test_295(self):
        input = """main: function void() {
            x: array [3] of float = a[1];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))
    def test_296(self):
        input = """main: function void() inherit 3 {
            }"""
        expect = "Error on line 1 col 30: 3"
        self.assertTrue(TestParser.test(input, expect, 296))
    def test_297(self):
        input = """main: function void() inherit func {
            a = a c;
            }"""
        expect = "Error on line 2 col 18: c"
        self.assertTrue(TestParser.test(input, expect, 297))
    def test_298(self):
        input = """main: function void() inherit funck {
            a=1 a[2];
            }"""
        expect = "Error on line 2 col 16: a"
        self.assertTrue(TestParser.test(input, expect, 298))
    def test_299(self):
        input = """main: function void() {
            string: string = "\t hello moi nguoi \\\ ";
            }"""
        expect = "Error on line 2 col 12: string"
        self.assertTrue(TestParser.test(input, expect, 299))

    
    
            

