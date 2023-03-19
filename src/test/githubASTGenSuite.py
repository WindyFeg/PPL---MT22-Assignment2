import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_program(self):
        input = "f : integer ;"
        expect = """Program([
	VarDecl(f, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 801))

    def test_program_2(self):
        input = "f : integer = foo(5+2-6*1) ;"
        expect = """Program([
	VarDecl(f, IntegerType, FuncCall(foo, [BinExpr(-, BinExpr(+, IntegerLit(5), IntegerLit(2)), BinExpr(*, IntegerLit(6), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 802))

    def test_program_3(self):
        input = "f,y : integer = foo(5+2-6*1), abc(6 == 6) ;"
        expect = """Program([
	VarDecl(f, IntegerType, FuncCall(foo, [BinExpr(-, BinExpr(+, IntegerLit(5), IntegerLit(2)), BinExpr(*, IntegerLit(6), IntegerLit(1)))]))
	VarDecl(y, IntegerType, FuncCall(abc, [BinExpr(==, IntegerLit(6), IntegerLit(6))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 803))

    def test_program_4(self):
        input = "f : array [4,5] of integer;"
        expect = """Program([
	VarDecl(f, ArrayType([4, 5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 804))

    def test_program_5(self):
        input = """x: array [2] of integer = {"hello" + 1 , 1};"""
        expect = """Program([
	VarDecl(x, ArrayType([2], IntegerType), ArrayLit([BinExpr(+, StringLit(hello), IntegerLit(1)), IntegerLit(1)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 805))

    def test_program_6(self):
        input = "f,x,t : integer = 3,4, 5 ;"
        expect = """Program([
	VarDecl(f, IntegerType, IntegerLit(3))
	VarDecl(x, IntegerType, IntegerLit(4))
	VarDecl(t, IntegerType, IntegerLit(5))
])"""
        self.assertTrue(TestAST.test(input, expect, 806))

    def test_program_7(self):
        input = """f : array [1] of integer = {1214, 123};"""
        expect = """Program([
	VarDecl(f, ArrayType([1], IntegerType), ArrayLit([IntegerLit(1214), IntegerLit(123)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 807))

    def test_program_8(self):
        input = """ f,y : integer = {"abc", "xyz"}, 1==1 ; """
        expect = """Program([
	VarDecl(f, IntegerType, ArrayLit([StringLit(abc), StringLit(xyz)]))
	VarDecl(y, IntegerType, BinExpr(==, IntegerLit(1), IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input, expect, 808))

    def test_program_9(self):
        input = "fa : array [4,5] of integer = {};"
        expect = """Program([
	VarDecl(fa, ArrayType([4, 5], IntegerType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 809))

    def test_program_10(self):
        input = """fac: array [4] of string = {"tokyo", "newyork", "london"};"""
        expect = """Program([
	VarDecl(fac, ArrayType([4], StringType), ArrayLit([StringLit(tokyo), StringLit(newyork), StringLit(london)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 810))

    def test_program_11(self):
        input = "f : auto = 1 + 2 -3 * 5 /10 + foo(x,z,t) ;"
        expect = """Program([
	VarDecl(f, AutoType, BinExpr(+, BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(/, BinExpr(*, IntegerLit(3), IntegerLit(5)), IntegerLit(10))), FuncCall(foo, [Id(x), Id(z), Id(t)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 811))

    def test_program_12(self):
        """CASE : #2 202.txt"""
        input = "f : float = 124.41124e-10 ;"
        expect = """Program([
	VarDecl(f, FloatType, FloatLit(1.2441124e-08))
])"""
        self.assertTrue(TestAST.test(input, expect, 812))

    def test_program_13(self):
        input = """
            var : string = "hello world";
            main : function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
            }
        """
        expect = """Program([
	VarDecl(var, StringType, StringLit(hello world))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), AssignStmt(Id(var), BinExpr(::, StringLit(Lau Dai Tinh Ai), Id(var)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 813))

    def test_program_14(self):
        input = """
            var : string = "hello world";
            foo : function auto () {}
            main: function void(){
                var = "Lau Dai Tinh Ai" :: var;
                return foo(123);
            }
        """
        expect = """Program([
	VarDecl(var, StringType, StringLit(hello world))
	FuncDecl(foo, AutoType, [], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(var), BinExpr(::, StringLit(Lau Dai Tinh Ai), Id(var))), ReturnStmt(FuncCall(foo, [IntegerLit(123)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 814))

    def test_program_15(self):
        input = """
            main: function void(){
                var = "Bac" :: "uuu";
                for(i = 0 , i < n + 1,  i + 1){
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(var), BinExpr(::, StringLit(Bac), StringLit(uuu))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(+, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 815))

    def test_program_16(self):
        input = """
            var : string = "hello world";
            sub : function boolean(var : string, delta : boolean) {
                str = "wtf r u doing here !!!";
            }
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                if (n == 0) {}
                else {}
            }
        """
        expect = """Program([
	VarDecl(var, StringType, StringLit(hello world))
	FuncDecl(sub, BooleanType, [Param(var, StringType), Param(delta, BooleanType)], None, BlockStmt([AssignStmt(Id(str), StringLit(wtf r u doing here !!!))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), AssignStmt(Id(var), BinExpr(::, StringLit(Lau Dai Tinh Ai), Id(var))), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 816))

    def test_program_17(self):
        input = """
            var : string = "hello world";
            main: function void(){
                var : integer = 1;
                if (a > 0) var2 : integer = 2;
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(i = 0, i < n, i + 1) {}
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = """Program([
	VarDecl(var, StringType, StringLit(hello world))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(var, IntegerType, IntegerLit(1)), IfStmt(BinExpr(>, Id(a), IntegerLit(0)), VarDecl(var2, IntegerType, IntegerLit(2))), DoWhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), AssignStmt(Id(var), BinExpr(::, StringLit(Lau Dai Tinh Ai), Id(var))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([])), CallStmt(test, IntegerLit(123), Id(ytx), BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(2)), IntegerLit(5)), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 817))

    def test_program_18(self):
        input = """
            var : string = "hello world";
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(i = 0, i < n, i + 1) continue;
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = """Program([
	VarDecl(var, StringType, StringLit(hello world))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), AssignStmt(Id(var), BinExpr(::, StringLit(Lau Dai Tinh Ai), Id(var))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), ContinueStmt()), CallStmt(test, IntegerLit(123), Id(ytx), BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(2)), IntegerLit(5)), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 818))

    def test_program_19(self):
        input = """
            var : string = "hello world";
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(i = 0, i < n, i + 1) break;
                if ( i < 1) return 1 + foo(2);
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = """Program([
	VarDecl(var, StringType, StringLit(hello world))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), AssignStmt(Id(var), BinExpr(::, StringLit(Lau Dai Tinh Ai), Id(var))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), IfStmt(BinExpr(<, Id(i), IntegerLit(1)), ReturnStmt(BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)])))), CallStmt(test, IntegerLit(123), Id(ytx), BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(2)), IntegerLit(5)), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 819))

    def test_program_20(self):
        input = """
            var : string = "hello world";
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(i = 0, i < n, i + 1) {return "chac khong co tren tran gian";}
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = """Program([
	VarDecl(var, StringType, StringLit(hello world))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), AssignStmt(Id(var), BinExpr(::, StringLit(Lau Dai Tinh Ai), Id(var))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ReturnStmt(StringLit(chac khong co tren tran gian))])), CallStmt(test, IntegerLit(123), Id(ytx), BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(2)), IntegerLit(5)), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 820))

    def test_program_21(self):
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(6))
])"""
        self.assertTrue(TestAST.test(input, expect, 821))

    def test_program_22(self):
        input = """
            var : string = "hello world";
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(i = a + b, i < n + 1, i + a *b -2 /10) {
                    return "chac khong co tren tran gian";
                }
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = """Program([
	VarDecl(var, StringType, StringLit(hello world))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), AssignStmt(Id(var), BinExpr(::, StringLit(Lau Dai Tinh Ai), Id(var))), ForStmt(AssignStmt(Id(i), BinExpr(+, Id(a), Id(b))), BinExpr(<, Id(i), BinExpr(+, Id(n), IntegerLit(1))), BinExpr(-, BinExpr(+, Id(i), BinExpr(*, Id(a), Id(b))), BinExpr(/, IntegerLit(2), IntegerLit(10))), BlockStmt([ReturnStmt(StringLit(chac khong co tren tran gian))])), CallStmt(test, IntegerLit(123), Id(ytx), BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(2)), IntegerLit(5)), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 822))

    def test_program_23(self):
        input = """
            var : string = "hello world";
            fact : function auto (alpha : string, delta : integer) {
                if(a < b) return true;
                else return 1 + fact(1 + 1 + 2);
            }
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(i = a + b, i < n + 1,  i + a *b -2 /10) {
                    return "chac khong co tren tran gian";
                }
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = """Program([
	VarDecl(var, StringType, StringLit(hello world))
	FuncDecl(fact, AutoType, [Param(alpha, StringType), Param(delta, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(a), Id(b)), ReturnStmt(BooleanLit(True)), ReturnStmt(BinExpr(+, IntegerLit(1), FuncCall(fact, [BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(1)), IntegerLit(2))]))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), AssignStmt(Id(var), BinExpr(::, StringLit(Lau Dai Tinh Ai), Id(var))), ForStmt(AssignStmt(Id(i), BinExpr(+, Id(a), Id(b))), BinExpr(<, Id(i), BinExpr(+, Id(n), IntegerLit(1))), BinExpr(-, BinExpr(+, Id(i), BinExpr(*, Id(a), Id(b))), BinExpr(/, IntegerLit(2), IntegerLit(10))), BlockStmt([ReturnStmt(StringLit(chac khong co tren tran gian))])), CallStmt(test, IntegerLit(123), Id(ytx), BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(2)), IntegerLit(5)), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 823))

    def test_program_24(self):
        input = """
            var : string = "hello world";
            fact : function auto (alpha : string, delta : integer) {
                if(a < b) return true;
                else return 1 + fact(1 + 1 + 2);
            }
            main: function void(){
                do{
                    a : float = 121.124e+10;
                    b : float = 1_124_141.012e-10;
                    c : float = 12_124.81E-10;
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(i = a + b, i < n + 1, i + a *b -2 /10) {
                    return "chac khong co tren tran gian";
                }
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = """Program([
	VarDecl(var, StringType, StringLit(hello world))
	FuncDecl(fact, AutoType, [Param(alpha, StringType), Param(delta, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(a), Id(b)), ReturnStmt(BooleanLit(True)), ReturnStmt(BinExpr(+, IntegerLit(1), FuncCall(fact, [BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(1)), IntegerLit(2))]))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([VarDecl(a, FloatType, FloatLit(1211240000000.0)), VarDecl(b, FloatType, FloatLit(0.0001124141012)), VarDecl(c, FloatType, FloatLit(1.212481e-06)), ReturnStmt(BooleanLit(False))])), AssignStmt(Id(var), BinExpr(::, StringLit(Lau Dai Tinh Ai), Id(var))), ForStmt(AssignStmt(Id(i), BinExpr(+, Id(a), Id(b))), BinExpr(<, Id(i), BinExpr(+, Id(n), IntegerLit(1))), BinExpr(-, BinExpr(+, Id(i), BinExpr(*, Id(a), Id(b))), BinExpr(/, IntegerLit(2), IntegerLit(10))), BlockStmt([ReturnStmt(StringLit(chac khong co tren tran gian))])), CallStmt(test, IntegerLit(123), Id(ytx), BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(2)), IntegerLit(5)), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 824))

    def test_program_25(self):
        input = """
            main: function void(){
                a : auto = 12.128431e-10;
                var = se % 10 + 10 - 1;
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 , c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, FloatLit(1.2128431e-09)), AssignStmt(Id(var), BinExpr(-, BinExpr(+, BinExpr(%, Id(se), IntegerLit(10)), IntegerLit(10)), IntegerLit(1))), WhileStmt(BinExpr(>, Id(acn), BinExpr(+, IntegerLit(10), IntegerLit(1))), BlockStmt([AssignStmt(Id(s), BinExpr(+, Id(l), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(>, Id(j), IntegerLit(0)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([ReturnStmt(BinExpr(+, Id(a), FuncCall(fact, [IntegerLit(12)])))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 825))

    def test_program_26(self):
        input = """
            main: function void(){
                a : auto = 12.128431e-10;
                var = se % 10 + 10 - 1;
                c : boolean = false;
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 , c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, FloatLit(1.2128431e-09)), AssignStmt(Id(var), BinExpr(-, BinExpr(+, BinExpr(%, Id(se), IntegerLit(10)), IntegerLit(10)), IntegerLit(1))), VarDecl(c, BooleanType, BooleanLit(False)), WhileStmt(BinExpr(>, Id(acn), BinExpr(+, IntegerLit(10), IntegerLit(1))), BlockStmt([AssignStmt(Id(s), BinExpr(+, Id(l), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(>, Id(j), IntegerLit(0)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([ReturnStmt(BinExpr(+, Id(a), FuncCall(fact, [IntegerLit(12)])))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 826))

    def test_program_27(self):
        input = """
            main: function void(){
                a : auto = 12.128431e-10;
                var = se % 10 + 10 - 1;
                a : auto = "string";
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 ,  c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, FloatLit(1.2128431e-09)), AssignStmt(Id(var), BinExpr(-, BinExpr(+, BinExpr(%, Id(se), IntegerLit(10)), IntegerLit(10)), IntegerLit(1))), VarDecl(a, AutoType, StringLit(string)), WhileStmt(BinExpr(>, Id(acn), BinExpr(+, IntegerLit(10), IntegerLit(1))), BlockStmt([AssignStmt(Id(s), BinExpr(+, Id(l), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(>, Id(j), IntegerLit(0)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([ReturnStmt(BinExpr(+, Id(a), FuncCall(fact, [IntegerLit(12)])))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 827))

    def test_program_28(self):
        input = """
            main: function void(){
                a : auto = 12.128431e-10;
                var = se % 10 + 10 - 1;
                a : auto = "string";
                // abc yxy comment is here ??
                /* abcas uasdn uqwnsdad */
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 ,  c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, FloatLit(1.2128431e-09)), AssignStmt(Id(var), BinExpr(-, BinExpr(+, BinExpr(%, Id(se), IntegerLit(10)), IntegerLit(10)), IntegerLit(1))), VarDecl(a, AutoType, StringLit(string)), WhileStmt(BinExpr(>, Id(acn), BinExpr(+, IntegerLit(10), IntegerLit(1))), BlockStmt([AssignStmt(Id(s), BinExpr(+, Id(l), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(>, Id(j), IntegerLit(0)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([ReturnStmt(BinExpr(+, Id(a), FuncCall(fact, [IntegerLit(12)])))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 828))

    def test_program_29(self):
        input = """
            ABNCASDH : auto ;
            main: function void(){
                a : auto = 2.128431e-3;
                var = se % 10 + 10 - 1;
                a : auto = "string";
                // abc yxy comment is here ??
                /* abcas uasdn uqwnsdad */
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 , c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = """Program([
	VarDecl(ABNCASDH, AutoType)
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, FloatLit(0.002128431)), AssignStmt(Id(var), BinExpr(-, BinExpr(+, BinExpr(%, Id(se), IntegerLit(10)), IntegerLit(10)), IntegerLit(1))), VarDecl(a, AutoType, StringLit(string)), WhileStmt(BinExpr(>, Id(acn), BinExpr(+, IntegerLit(10), IntegerLit(1))), BlockStmt([AssignStmt(Id(s), BinExpr(+, Id(l), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(>, Id(j), IntegerLit(0)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([ReturnStmt(BinExpr(+, Id(a), FuncCall(fact, [IntegerLit(12)])))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 829))

    def test_program_30(self):
        input = """
             ABNCASDH : auto ;
             main: function void(){
                 a : auto = 12.128431e-10;
                 var = se % 10 + 10 - 1;
                 a : auto = "string";
                 // abc yxy comment is here ??
                 /* abcas uasdn uqwnsdad */

                 var = "em oi " + "lau dai tinh ai" :: "chac khong co tren tran gian";
                 while(acn > 10 + 1){
                     s = l + 1;
                     for ( i = 1, j > 0 , c + 1){
                         return a + fact(12);
                     }
                 }
             }
         """
        expect = """Program([
	VarDecl(ABNCASDH, AutoType)
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, FloatLit(1.2128431e-09)), AssignStmt(Id(var), BinExpr(-, BinExpr(+, BinExpr(%, Id(se), IntegerLit(10)), IntegerLit(10)), IntegerLit(1))), VarDecl(a, AutoType, StringLit(string)), AssignStmt(Id(var), BinExpr(::, BinExpr(+, StringLit(em oi ), StringLit(lau dai tinh ai)), StringLit(chac khong co tren tran gian))), WhileStmt(BinExpr(>, Id(acn), BinExpr(+, IntegerLit(10), IntegerLit(1))), BlockStmt([AssignStmt(Id(s), BinExpr(+, Id(l), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(>, Id(j), IntegerLit(0)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([ReturnStmt(BinExpr(+, Id(a), FuncCall(fact, [IntegerLit(12)])))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 830))

    def test_program_31(self):
        input = """
             ABNCASDH : auto ;
             main: function void(){
                do {return 0;} while(b < 9);
             }
         """
        expect = """Program([
	VarDecl(ABNCASDH, AutoType)
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(b), IntegerLit(9)), BlockStmt([ReturnStmt(IntegerLit(0))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 831))

    def test_program_32(self):
        input = """
             ABNCASDH : auto ;
             main: function void(){
                do {return 0;} while(b < 9);
                for(i = 0 , i == 1-1, a *3) return ;
             }
         """
        expect = """Program([
	VarDecl(ABNCASDH, AutoType)
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(b), IntegerLit(9)), BlockStmt([ReturnStmt(IntegerLit(0))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(==, Id(i), BinExpr(-, IntegerLit(1), IntegerLit(1))), BinExpr(*, Id(a), IntegerLit(3)), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 832))

    def test_program_33(self):
        input = """
             ABNCASDH : auto ;
             main: function void(){
                do {return 0;} while(b < 9);
                for(i = 0 , i == 1-1, a *3) return ;

                if (a == 1 + 1) return;
                a : float = 123.1241824e-10;
             }
         """
        expect = """Program([
	VarDecl(ABNCASDH, AutoType)
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(b), IntegerLit(9)), BlockStmt([ReturnStmt(IntegerLit(0))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(==, Id(i), BinExpr(-, IntegerLit(1), IntegerLit(1))), BinExpr(*, Id(a), IntegerLit(3)), ReturnStmt()), IfStmt(BinExpr(==, Id(a), BinExpr(+, IntegerLit(1), IntegerLit(1))), ReturnStmt()), VarDecl(a, FloatType, FloatLit(1.231241824e-08))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 833))

    def test_program_34(self):
        input = """
            a: integer = func(10);
            main: function string () {
                for(i = 3, i <= 10, i + 1) {
                    sum = sum + i;
                }
                print("I Love you");
            }
        """
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(func, [IntegerLit(10)]))
	FuncDecl(main, StringType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(3)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i)))])), CallStmt(print, StringLit(I Love you))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 834))

    def test_program_35(self):
        input = """
            integers: array [5] of integer = {1, 2, 3, "a"};
        """
        expect = """Program([
	VarDecl(integers, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), StringLit(a)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 835))

    def test_program_36(self):
        input = """
            integers: array [5] of integer = {1, 2, 3, "a"};
            a : integer = "hello world";
            c : float = 812.123e-10;
        """
        expect = """Program([
	VarDecl(integers, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), StringLit(a)]))
	VarDecl(a, IntegerType, StringLit(hello world))
	VarDecl(c, FloatType, FloatLit(8.12123e-08))
])"""
        self.assertTrue(TestAST.test(input, expect, 836))

    def test_program_37(self):
        """CASE : #2 202.txt"""
        input = """f : integer = {"em dong y"};"""
        expect = """Program([
	VarDecl(f, IntegerType, ArrayLit([StringLit(em dong y)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 837))

    def test_program_38(self):
        """CASE : #3 203.txt"""
        input = """flot: integer = 10;"""
        expect = """Program([
	VarDecl(flot, IntegerType, IntegerLit(10))
])"""
        self.assertTrue(TestAST.test(input, expect, 838))

    def test_program_39(self):
        input = """
            main : function void (inherit out delta : integer){
                {}
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(delta, IntegerType)], None, BlockStmt([BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 839))

    def test_program_40(self):
        input = """
            main : function void (inherit out delta : integer){
                if (n != 0 ) return 1;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(delta, IntegerType)], None, BlockStmt([IfStmt(BinExpr(!=, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 840))

    def test_program_41(self):
        input = """
            main: function boolean () {}
        """
        expect = """Program([
	FuncDecl(main, BooleanType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 841))

    def test_program_42(self):
        input = """
            /* main function */
            main: function float () {}
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 842))

    def test_program_43(self):
        input = """
            /* main function */
            main: function float () {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i + 1) break;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 843))

    def test_program_44(self):
        input = """
            /* main function */
            main: function float () {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n ,  i + 1) break;
                while(n && a) continue;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), WhileStmt(BinExpr(&&, Id(n), Id(a)), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 844))

    def test_program_45(self):
        input = """
            /* main function */
            main: function float () {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n ,  i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), WhileStmt(BinExpr(&&, Id(n), Id(a)), ContinueStmt()), DoWhileStmt(BinExpr(||, Id(n), Id(a)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 845))

    def test_program_46(self):
        input = """
            /* main function */
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n ,  i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [Param(a, AutoType), Param(b, AutoType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), WhileStmt(BinExpr(&&, Id(n), Id(a)), ContinueStmt()), DoWhileStmt(BinExpr(||, Id(n), Id(a)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 846))

    def test_program_47(self):
        input = """
            /* main function */
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n ,  i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
                if ( n > 0) {} else return 0;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [Param(a, AutoType), Param(b, AutoType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), WhileStmt(BinExpr(&&, Id(n), Id(a)), ContinueStmt()), DoWhileStmt(BinExpr(||, Id(n), Id(a)), BlockStmt([])), IfStmt(BinExpr(>, Id(n), IntegerLit(0)), BlockStmt([]), ReturnStmt(IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 847))

    def test_program_48(self):
        input = """
            /* main function */
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n ,  i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
                if ( n > 0) {
                    var : string = "hello" ::  "world";
                } else return 0;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [Param(a, AutoType), Param(b, AutoType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), WhileStmt(BinExpr(&&, Id(n), Id(a)), ContinueStmt()), DoWhileStmt(BinExpr(||, Id(n), Id(a)), BlockStmt([])), IfStmt(BinExpr(>, Id(n), IntegerLit(0)), BlockStmt([VarDecl(var, StringType, BinExpr(::, StringLit(hello), StringLit(world)))]), ReturnStmt(IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 848))

    def test_program_49(self):
        input = """
            /* main function */
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n ,  i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
                if ( n > 0) {
                    var : string = "hello" ::  "world";
                } else return 0;
                if ( n && 0 ){
                    while(n == 0){
                        return false;
                    }
                    for (i = 0, i < 5, i +1 ){
                        a = 10;
                        a = a + 123 && b - 10 * 18 -19;
                    }
                }
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [Param(a, AutoType), Param(b, AutoType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), WhileStmt(BinExpr(&&, Id(n), Id(a)), ContinueStmt()), DoWhileStmt(BinExpr(||, Id(n), Id(a)), BlockStmt([])), IfStmt(BinExpr(>, Id(n), IntegerLit(0)), BlockStmt([VarDecl(var, StringType, BinExpr(::, StringLit(hello), StringLit(world)))]), ReturnStmt(IntegerLit(0))), IfStmt(BinExpr(&&, Id(n), IntegerLit(0)), BlockStmt([WhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(10)), AssignStmt(Id(a), BinExpr(&&, BinExpr(+, Id(a), IntegerLit(123)), BinExpr(-, BinExpr(-, Id(b), BinExpr(*, IntegerLit(10), IntegerLit(18))), IntegerLit(19))))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 849))

    def test_program_50(self):
        input = """
            /* main function */

            delta : boolean = true;
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
                if ( n > 0) {
                    var : string = "hello" ::  "world";
                } else return 0;
                if ( n && 0 ){
                    while(n == 0){
                        return false;
                    }
                    for (i = 0, i < 5, i +1 ){
                        a = 10;
                        a = a + 123 && b - 10 * 18 -19;
                    }
                }
            }
        """
        expect = """Program([
	VarDecl(delta, BooleanType, BooleanLit(True))
	FuncDecl(main, FloatType, [Param(a, AutoType), Param(b, AutoType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(==, BinExpr(+, IntegerLit(10), BinExpr(/, BinExpr(*, IntegerLit(132), Id(x)), IntegerLit(10))), BinExpr(+, IntegerLit(0), Id(cn)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt()), WhileStmt(BinExpr(&&, Id(n), Id(a)), ContinueStmt()), DoWhileStmt(BinExpr(||, Id(n), Id(a)), BlockStmt([])), IfStmt(BinExpr(>, Id(n), IntegerLit(0)), BlockStmt([VarDecl(var, StringType, BinExpr(::, StringLit(hello), StringLit(world)))]), ReturnStmt(IntegerLit(0))), IfStmt(BinExpr(&&, Id(n), IntegerLit(0)), BlockStmt([WhileStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(10)), AssignStmt(Id(a), BinExpr(&&, BinExpr(+, Id(a), IntegerLit(123)), BinExpr(-, BinExpr(-, Id(b), BinExpr(*, IntegerLit(10), IntegerLit(18))), IntegerLit(19))))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 850))

    def test_program_51(self):
        input = """
            /* main function */
            main: function float () {
                a = true || false;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 851))

    def test_program_52(self):
        input = """
            /* main function */
            main: function float () {
                a = true && false;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(&&, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 852))

    def test_program_53(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = true || false;
            }
        """
        expect = """Program([
	VarDecl(factor, IntegerType, FloatLit(10.0))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 853))

    def test_program_54(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = true || false;
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 854))

    def test_program_55(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;

            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	VarDecl(str, AutoType, StringLit(abc))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 855))

    def test_program_56(self):
        input = """
            /* main function */
            main: function float () {
                a = true || false;
                return;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 856))

    def test_program_57(self):
        input = """
            /* main function */
            main: function float () {
                a = true && false;
                return a;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(&&, BooleanLit(True), BooleanLit(False))), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 857))

    def test_program_58(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = true || false;
                {}
                {}
                {}
            }
        """
        expect = """Program([
	VarDecl(factor, IntegerType, FloatLit(10.0))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False))), BlockStmt([]), BlockStmt([]), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 858))

    def test_program_59(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = true || false;
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 859))

    def test_program_60(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;
                a[0] = 19 + 123 + 19 * 13 -10 ;

            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	VarDecl(str, AutoType, StringLit(abc))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), BinExpr(-, BinExpr(+, BinExpr(+, IntegerLit(19), IntegerLit(123)), BinExpr(*, IntegerLit(19), IntegerLit(13))), IntegerLit(10)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 860))

    def test_program_61(self):
        input = """
            /* main function */
            main: function float () {
                a = true || false;
                a = as[1] + 123 - 1 + a[a[0]];
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False))), AssignStmt(Id(a), BinExpr(+, BinExpr(-, BinExpr(+, ArrayCell(as, [IntegerLit(1)]), IntegerLit(123)), IntegerLit(1)), ArrayCell(a, [ArrayCell(a, [IntegerLit(0)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 861))

    def test_program_62(self):
        input = """
            /* main function */
            main: function float () {
                a = true && false;
                print(abc);
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(&&, BooleanLit(True), BooleanLit(False))), CallStmt(print, Id(abc))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 862))

    def test_program_63(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = true || false;
                foo(123 +13 -1 + foo(5));
            }
        """
        expect = """Program([
	VarDecl(factor, IntegerType, FloatLit(10.0))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False))), CallStmt(foo, BinExpr(+, BinExpr(-, BinExpr(+, IntegerLit(123), IntegerLit(13)), IntegerLit(1)), FuncCall(foo, [IntegerLit(5)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 863))

    def test_program_64(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = {};
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 864))

    def test_program_65(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;
                b : auto;

            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	VarDecl(str, AutoType, StringLit(abc))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False))), VarDecl(b, AutoType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 865))

    def test_program_66(self):
        input = """
            /* main function */
            main: function float () {
                a = true || false;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 866))

    def test_program_67(self):
        input = """
            /* main function */
            main: function float () {
                n = strlen(str);
                for (i = 0, i < n / 2,  i + 1) {
                    swap(str[i], str[n - i - 1]);
                }
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(n), FuncCall(strlen, [Id(str)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(swap, ArrayCell(str, [Id(i)]), ArrayCell(str, [BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 867))

    def test_program_68(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = true || false;
            }
        """
        expect = """Program([
	VarDecl(factor, IntegerType, FloatLit(10.0))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 868))

    def test_program_69(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = true || false;
                foo();
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False))), CallStmt(foo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 869))

    def test_program_70(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;
                r,s : float;
                r = 2.0;
                s = r * r * myPi;
                a[0] = s;

            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	VarDecl(str, AutoType, StringLit(abc))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False))), VarDecl(r, FloatType), VarDecl(s, FloatType), AssignStmt(Id(r), FloatLit(2.0)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPi))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 870))

    def test_program_71(self):
        input = """
            /* main function */
            main: function float () {
                return 1 + 2 + {} - myPI * foo(a[a[0]] - 10 + swap());
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([ReturnStmt(BinExpr(-, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), ArrayLit([])), BinExpr(*, Id(myPI), FuncCall(foo, [BinExpr(+, BinExpr(-, ArrayCell(a, [ArrayCell(a, [IntegerLit(0)])]), IntegerLit(10)), FuncCall(swap, []))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 871))

    def test_program_72(self):
        input = """
            /* main function */
            main: function float (out n : integer, out i : float) {
                a = true && false;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [OutParam(n, IntegerType), OutParam(i, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(&&, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 872))

    def test_program_73(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float (inherit out a : auto) {
                a = true || false;
            }
        """
        expect = """Program([
	VarDecl(factor, IntegerType, FloatLit(10.0))
	FuncDecl(main, FloatType, [InheritOutParam(a, AutoType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 873))

    def test_program_74(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = true || false;
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 874))

    def test_program_75(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                }
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	VarDecl(str, AutoType, StringLit(abc))
	FuncDecl(main, FloatType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 875))

    def test_program_76(self):
        input = """
            /* main function */
            main: function string () {}
        """
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 876))

    def test_program_77(self):
        input = """
            /* main function */
            main: function float () {{{}}{}}
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([BlockStmt([BlockStmt([])]), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 877))

    def test_program_78(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                continue;
            }
        """
        expect = """Program([
	VarDecl(factor, IntegerType, FloatLit(10.0))
	FuncDecl(main, FloatType, [], None, BlockStmt([ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 878))

    def test_program_79(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = true || false;
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 879))

    def test_program_80(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = 1_23.40E+156;

            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	VarDecl(str, AutoType, StringLit(abc))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(1.234e+158))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 880))

    def test_program_81(self):
        input = """
            /* main function */
            main: function float () {
                a = 1_23.04E-56;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(1.2304e-54))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 881))

    def test_program_82(self):
        input = """
            /* main function */
            main: function float () {
                a = 1_23.456e-10;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(1.23456e-08))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 882))

    def test_program_83(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = "@#$&\t^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@";
            }
        """
        expect = """Program([
	VarDecl(factor, IntegerType, FloatLit(10.0))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(@#$&	^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 883))

    def test_program_84(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = "@#$&^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@";
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(@#$&^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 884))

    def test_program_85(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = "Chuoi cua ban la: \\"12345\\"";

            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	VarDecl(str, AutoType, StringLit(abc))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(Chuoi cua ban la: \\"12345\\"))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 885))

    def test_program_86(self):
        input = """
            /* main function */
            main: function float () {
                a = true || false;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 886))

    def test_program_87(self):
        input = """
            /* main function */
            main: function float () {
                a = "This is Hung\'s PC";
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(This is Hung's PC))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 887))

    def test_program_88(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = "He asked me: \\\"Where is John?\\\"";
            }
        """
        expect = """Program([
	VarDecl(factor, IntegerType, FloatLit(10.0))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(He asked me: \\\"Where is John?\\\"))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 888))

    def test_program_89(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = 1_23_1414_214;
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1231414214))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 889))

    def test_program_90(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = 3200_21000_123_000;

            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	VarDecl(str, AutoType, StringLit(abc))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(320021000123000))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 890))

    def test_program_91(self):
        input = """
            /* main function */
            main: function float () {
                a = 1_23.000456E-10;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(1.23000456e-08))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 891))

    def test_program_92(self):
        input = """
            /* main function */
            main: function float () {
                a = 1_23.40E+156;
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(1.234e+158))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 892))

    def test_program_93(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                /*tran khac chan nam qua xa, */ \n //ve day voi nhau hai dua dap chung men*/ abcxyz
                a = true || false;
            }
        """
        expect = """Program([
	VarDecl(factor, IntegerType, FloatLit(10.0))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 893))

    def test_program_94(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                /* anh muon ta ve cung mot nha, an sang va cung hat ca */ // nhung biet sao gio 
                a = true || false;
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 894))

    def test_program_95(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;

            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	VarDecl(str, AutoType, StringLit(abc))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 895))

    def test_program_96(self):
        input = """
            /* main function */
            main: function float () {
                a = "@#$&^@$@ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@";
            }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(@#$&^@$@ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 896))

    def test_program_97(self):
        input = """
            func: function void () {
                if (i==1) 
                    if (i==2)
                        if (i > 3)
                            if (i>=5)
                                printString("I love you");
            }
        """
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(i), IntegerLit(2)), IfStmt(BinExpr(>, Id(i), IntegerLit(3)), IfStmt(BinExpr(>=, Id(i), IntegerLit(5)), CallStmt(printString, StringLit(I love you))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 897))

    def test_program_98(self):
        input = """
            func: function void () {
                if ("i love you") 
                    if ("but")
                        if ("you don't love me")
                            if ("make")
                                printString("me and my broken heart");
            }
        """
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(StringLit(i love you), IfStmt(StringLit(but), IfStmt(StringLit(you don't love me), IfStmt(StringLit(make), CallStmt(printString, StringLit(me and my broken heart))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 898))

    def test_program_99(self):
        input = """
            func: function void () {
                if ("i wanna hide the truth") 
                    while("i wanna shelter you")
                        if ("but with the beast inside")
                            while("there's nowhere we can hide")
                                return "No matter what we breed";
            }
        """
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(StringLit(i wanna hide the truth), WhileStmt(StringLit(i wanna shelter you), IfStmt(StringLit(but with the beast inside), WhileStmt(StringLit(there's nowhere we can hide), ReturnStmt(StringLit(No matter what we breed))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 899))

    def test_program_100(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = "don't get too close, it's dark inside" :: "it's where my demon hide";
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	VarDecl(str, AutoType, StringLit(abc))
	FuncDecl(main, FloatType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, StringLit(don't get too close, it's dark inside), StringLit(it's where my demon hide)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 900))
