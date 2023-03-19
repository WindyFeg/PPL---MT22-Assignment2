import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = """Program([
	VarDecl(x, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_short_vardecl_1(self):
        input = """y: boolean;"""
        expect = """Program([
	VarDecl(y, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_short_vardecl_2(self):
        input = """x,y,z: integer;"""
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_short_vardecl_3(self):
        input = """x: array [1,2] of integer;"""
        expect = """Program([
	VarDecl(x, ArrayType([1, 2], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_short_vardecl_4(self):
        input = """x: integer = 1;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_short_vardecl_5(self):
        input = """x: integer = 1 + 1 - 2 * 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(*, IntegerLit(2), IntegerLit(3))))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_short_vardecl_6(self):
        input = """x: integer = 1 && 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(&&, IntegerLit(1), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_short_vardecl_7(self):
        input = """x: integer = "Hello world";"""
        expect = """Program([
	VarDecl(x, IntegerType, StringLit(Hello world))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_short_vardecl_8(self):
        input = """x: integer = false;"""
        expect = """Program([
	VarDecl(x, IntegerType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_short_vardecl_9(self):
        input = """x: integer = {1};"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayLit([IntegerLit(1)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_short_vardecl_10(self):
        input = """x: integer = {};"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_short_vardecl_11(self):
        input = """x: integer = {1,2,3,4};"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_short_vardecl_12(self):
        input = """x: integer = {1,false,true,"hello",2.01};"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayLit([IntegerLit(1), BooleanLit(False), BooleanLit(True), StringLit(hello), FloatLit(2.01)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_short_vardecl_13(self):
        input = """x: integer = false;"""
        expect = """Program([
	VarDecl(x, IntegerType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_short_vardecl_14(self):
        input = """x: integer = iden;"""
        expect = """Program([
	VarDecl(x, IntegerType, Id(iden))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_short_vardecl_15(self):
        input = """x: integer = iden;
y: float = 1.02;
z: float = 11.1;"""
        expect = """Program([
	VarDecl(x, IntegerType, Id(iden))
	VarDecl(y, FloatType, FloatLit(1.02))
	VarDecl(z, FloatType, FloatLit(11.1))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_short_vardecl_16(self):
        input = """x: integer = a==4;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(==, Id(a), IntegerLit(4)))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_short_vardecl_17(self):
        input = """x: integer = 2+4*5&&!a==4;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(==, BinExpr(&&, BinExpr(+, IntegerLit(2), BinExpr(*, IntegerLit(4), IntegerLit(5))), UnExpr(!, Id(a))), IntegerLit(4)))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_func_decl_1(self):
        input = """fact : function integer (n : integer){}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_func_decl_2(self):
        input = """fact : function integer (n : integer){}
fuk : function integer (n : integer){}
fik : function integer (n : integer){}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([]))
	FuncDecl(fuk, IntegerType, [Param(n, IntegerType)], None, BlockStmt([]))
	FuncDecl(fik, IntegerType, [Param(n, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_func_decl_3(self):
        input = """fact : function integer (n : integer, m : float, a : boolean){}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType), Param(m, FloatType), Param(a, BooleanType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_func_decl_4(self):
        input = """fact : function integer (n : integer, m : float, a : boolean){
                        a = 1;
                }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType), Param(m, FloatType), Param(a, BooleanType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_func_decl_5(self):
        input = """fact : function integer (n : integer){
                        a = 1;
                        b = 1 + 2 - 3;
                }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(b), BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_func_decl_6(self):
        input = """fact : function integer (n : integer) inherit lol {
                        a = 1;
                        b = 1 + 2 - 3;
                }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], lol, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(b), BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_func_decl_7(self):
        input = """fact : function integer (n : integer) inherit lol {
                        a[1] = 1;
                        b[1,2,3] = 1 + 2 - 3;
                }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], lol, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)), AssignStmt(ArrayCell(b, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_func_decl_8(self):
        input = """fact : function integer (){}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_func_decl_9(self):
        input = """fact : function integer (){
                if(1+1)
                {
                        a = 1;
                        b = 2;
                }
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(+, IntegerLit(1), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(b), IntegerLit(2))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_func_decl_10(self):
        input = """fact : function integer (){
                if(1+1) a = 1;
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(+, IntegerLit(1), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_func_decl_11(self):
        input = """fact : function integer (){
                break;
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_func_decl_12(self):
        input = """fact : function integer (){
                for(x=1,x<1,x+1) a = 1;
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(1)), BinExpr(<, Id(x), IntegerLit(1)), BinExpr(+, Id(x), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_func_decl_13(self):
        input = """fact : function integer (){
                for(x=1,x<1,x+1) {
                        a = 1;
                }
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(1)), BinExpr(<, Id(x), IntegerLit(1)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_func_decl_14(self):
        input = """fact : function integer (){
                while(x<1) {
                        a = 1;
                }
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_func_decl_15(self):
        input = """fact : function integer (){
                while(x<1) a = 1;
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_func_decl_16(self):
        input = """fact : function integer (){
                do{a = a+1;}
                while(a < 10);
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_func_decl_17(self):
        input = """fact : function integer (){
                do{a = a+1;}
                while(a < 10);
                return;
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_func_decl_18(self):
        input = """fact : function integer (){
                do{a = a+1;}
                while(a < 10);
                return a;
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_func_decl_19(self):
        input = """fact : function integer (){
                do{a = a+1;
                continue;
                break;
                }
                while(a < 10);
                return a;
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), ContinueStmt(), BreakStmt()])), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_func_decl_20(self):
        input = """fact : function integer (){
                readInteger();
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([CallStmt(readInteger, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_func_decl_21(self):
        input = """fact : function integer (){
                readInteger(a,b);
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([CallStmt(readInteger, Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_func_decl_22(self):
        input = """fact : function integer (){
                readInteger(a,b,1,2+1,true,"hello");
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([CallStmt(readInteger, Id(a), Id(b), IntegerLit(1), BinExpr(+, IntegerLit(2), IntegerLit(1)), BooleanLit(True), StringLit(hello))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_func_decl_23(self):
        input = """fact : function integer (){
                if(a==0) if(b==0) a = 1;
                 
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), IfStmt(BinExpr(==, Id(b), IntegerLit(0)), AssignStmt(Id(a), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_func_decl_24(self):
        input = """fact : function integer (){
                a = {};
                 
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_func_decl_25(self):
        input = """fact : function integer (){
                a : integer = 1;           
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_func_decl_26(self):
        input = """fact : function integer (){
                a,b,c : integer = 1,2,3;           
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_func_decl_27(self):
        input = """fact : function integer (){
                a,b,c : integer = 1,{},"hello";           
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, ArrayLit([])), VarDecl(c, IntegerType, StringLit(hello))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_func_decl_28(self):
        input = """fact : function integer (){
                a,_c,_d : boolean;
                a = _c + (a + 13) * (24 * x) / 2 - x;           
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([VarDecl(a, BooleanType), VarDecl(_c, BooleanType), VarDecl(_d, BooleanType), AssignStmt(Id(a), BinExpr(-, BinExpr(+, Id(_c), BinExpr(/, BinExpr(*, BinExpr(+, Id(a), IntegerLit(13)), BinExpr(*, IntegerLit(24), Id(x))), IntegerLit(2))), Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_func_decl_29(self):
        input = """fact : function integer (){
                if (true || boolVar){
                        a = "phong";
                }
                else 
                {
                        a = "ky";
                }          
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(||, BooleanLit(True), Id(boolVar)), BlockStmt([AssignStmt(Id(a), StringLit(phong))]), BlockStmt([AssignStmt(Id(a), StringLit(ky))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_func_decl_30(self):
        input = """main : function string (){
                a = 1 - foo();
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, IntegerLit(1), FuncCall(foo, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_func_decl_31(self):
        input = """main : function string (){
                a = 1 - foo(foo(foo()));
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, IntegerLit(1), FuncCall(foo, [FuncCall(foo, [FuncCall(foo, [])])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_func_decl_32(self):
        input = """main : function string (){
                a = d;
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), Id(d))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_func_decl_33(self):
        input = """main : function string (){
                foo(foo(foo("stupid")));
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([CallStmt(foo, FuncCall(foo, [FuncCall(foo, [StringLit(stupid)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_func_decl_34(self):
        input = """main : function string (){
                return foo(1-2);
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([ReturnStmt(FuncCall(foo, [BinExpr(-, IntegerLit(1), IntegerLit(2))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_func_decl_35(self):
        input = """a, b: array [5] of integer;"""
        expect = """Program([
	VarDecl(a, ArrayType([5], IntegerType))
	VarDecl(b, ArrayType([5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_func_decl_36(self):
        input = """a, b: array [5_1] of integer;"""
        expect = """Program([
	VarDecl(a, ArrayType([51], IntegerType))
	VarDecl(b, ArrayType([51], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_func_decl_37(self):
        input = """a, b: array [5_1, 2, 3] of integer = {1,2,3,4,5}, false;"""
        expect = """Program([
	VarDecl(a, ArrayType([51, 2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	VarDecl(b, ArrayType([51, 2, 3], IntegerType), BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_func_decl_38(self):
        input = """main:function void() {if(false == true) a = 1; else a = 0;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, BooleanLit(False), BooleanLit(True)), AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_func_decl_39(self):
        input = """main:function void() {
            for(i=1, i<10, i+1){

            }
        } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_func_decl_40(self):
        input = """main:function void() {
            for(i=1, i<10, i+1){
                writeInt(i);
                a = 1;
                a:integer;
                b:integer = 2;
                if (1 < 2) a = 0;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i)), AssignStmt(Id(a), IntegerLit(1)), VarDecl(a, IntegerType), VarDecl(b, IntegerType, IntegerLit(2)), IfStmt(BinExpr(<, IntegerLit(1), IntegerLit(2)), AssignStmt(Id(a), IntegerLit(0)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_func_decl_41(self):
        input = """main:function void() {
            do {
                a = "Helloabcd";
                break;
            }
            while (a < 2);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), StringLit(Helloabcd)), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_func_decl_42(self):
        input = """delta123 : integer = 1+1-1*2/3%3;"""
        expect = """Program([
	VarDecl(delta123, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(3))))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_func_decl_43(self):
        input = """main:function string (){
                a = "hello"; b = 1; 
                c = 0.123; 
                d = f; 
                e = foo(); 
                f = false; return 1_2;
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(hello)), AssignStmt(Id(b), IntegerLit(1)), AssignStmt(Id(c), FloatLit(0.123)), AssignStmt(Id(d), Id(f)), AssignStmt(Id(e), FuncCall(foo, [])), AssignStmt(Id(f), BooleanLit(False)), ReturnStmt(IntegerLit(12))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_func_decl_44(self):
        input = """main:function string (){
                a = "hello"::"world"; 
                b = 1+2; 
                return a;
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, StringLit(hello), StringLit(world))), AssignStmt(Id(b), BinExpr(+, IntegerLit(1), IntegerLit(2))), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_func_decl_45(self):
        input = """main:function string (){return 1+!3;}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([ReturnStmt(BinExpr(+, IntegerLit(1), UnExpr(!, IntegerLit(3))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_func_decl_46(self):
        input = """main:function string (){return 1+-3;}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([ReturnStmt(BinExpr(+, IntegerLit(1), UnExpr(-, IntegerLit(3))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_func_decl_47(self):
        input = """main: function void() {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_func_decl_48(self):
        input = """delta123 : string = "Hello World";"""
        expect = """Program([
	VarDecl(delta123, StringType, StringLit(Hello World))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_func_decl_49(self):
        input = """delta123,alpha123 : string = "Hello","World";"""
        expect = """Program([
	VarDecl(delta123, StringType, StringLit(Hello))
	VarDecl(alpha123, StringType, StringLit(World))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_func_decl_50(self):
        input = """delta123 : boolean = true;"""
        expect = """Program([
	VarDecl(delta123, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_func_decl_51(self):
        input = """delta123 : integer = 1;
        count : integer = 0;
        up : string = "GO";"""
        expect = """Program([
	VarDecl(delta123, IntegerType, IntegerLit(1))
	VarDecl(count, IntegerType, IntegerLit(0))
	VarDecl(up, StringType, StringLit(GO))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_func_decl_52(self):
        input = """main: function void() inherit abc {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], abc, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_func_decl_53(self):
        input = """main: function integer(a: integer, out b: float, inherit c: string) inherit abc {}"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(b, FloatType), InheritParam(c, StringType)], abc, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_func_decl_54(self):
        input = """abc:integer;main: function void(xyz:integer, def:integer) inherit hehe {}"""
        expect = """Program([
	VarDecl(abc, IntegerType)
	FuncDecl(main, VoidType, [Param(xyz, IntegerType), Param(def, IntegerType)], hehe, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_func_decl_55(self):
        input = """main: function void(xyz:integer, def:integer) inherit hehe {} 
        abc:integer;"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(xyz, IntegerType), Param(def, IntegerType)], hehe, BlockStmt([]))
	VarDecl(abc, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_func_decl_56(self):
        input = """main:function string (){a = 2; return;}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_func_decl_57(self):
        input = """main:function string (){a = 2; b =1; return;}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(b), IntegerLit(1)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_func_decl_58(self):
        input = """main:function string (){}
        main:function string (){}
        main:function string (){}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([]))
	FuncDecl(main, StringType, [], None, BlockStmt([]))
	FuncDecl(main, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_func_decl_59(self):
        input = """main:function string (){a = 2; b =1; break;}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(b), IntegerLit(1)), BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_func_decl_60(self):
        input = """main:function string (){a = "hello"; b = 1; c = 0.123; d = f; e = foo(); f = false; return 1_2;}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(hello)), AssignStmt(Id(b), IntegerLit(1)), AssignStmt(Id(c), FloatLit(0.123)), AssignStmt(Id(d), Id(f)), AssignStmt(Id(e), FuncCall(foo, [])), AssignStmt(Id(f), BooleanLit(False)), ReturnStmt(IntegerLit(12))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_func_decl_61(self):
        input = """main:function string (){return foo(1 - 2, a, "True");}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([ReturnStmt(FuncCall(foo, [BinExpr(-, IntegerLit(1), IntegerLit(2)), Id(a), StringLit(True)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_func_decl_62(self):
        input = """main: function void() {
                x,y,z: integer = 1,2,{1,2,2};
                {a=3;}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), VarDecl(y, IntegerType, IntegerLit(2)), VarDecl(z, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(2)])), BlockStmt([AssignStmt(Id(a), IntegerLit(3))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_func_decl_63(self):
        input = """main: function void() {
                if(a==1) a=1;
                if(a==1) a=2; else a=3;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1))), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(a), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_func_decl_64(self):
        input = """main: function void() {
                if(a==1) a=2; 
                else {
                        a=3;
                        if (a==4) a = 1;
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), IntegerLit(3)), IfStmt(BinExpr(==, Id(a), IntegerLit(4)), AssignStmt(Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_func_decl_65(self):
        input = """main: function void() {
                a: auto = -var[a||3==b*!-g[12]];
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, UnExpr(-, ArrayCell(var, [BinExpr(==, BinExpr(||, Id(a), IntegerLit(3)), BinExpr(*, Id(b), UnExpr(!, UnExpr(-, ArrayCell(g, [IntegerLit(12)])))))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_func_decl_66(self):
        input = """main: function void() {
                a: auto = a/a==b/b-((asdf)::(asdf));
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, BinExpr(==, BinExpr(/, Id(a), Id(a)), BinExpr(-, BinExpr(/, Id(b), Id(b)), BinExpr(::, Id(asdf), Id(asdf)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_func_decl_67(self):
        input = """main: function void() {
                a = (a < b) < (c < d);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(<, BinExpr(<, Id(a), Id(b)), BinExpr(<, Id(c), Id(d))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_func_decl_68(self):
        input = """main: function void() {
                a = (a > (b > c)) > d;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, BinExpr(>, Id(a), BinExpr(>, Id(b), Id(c))), Id(d)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_func_decl_69(self):
        input = """main: function void () {}
            sum: function auto () {}
            _VAR1: integer;
            _VAR2: string = "string";"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([]))\n\tFuncDecl(sum, AutoType, [], None, BlockStmt([]))\n\tVarDecl(_VAR1, IntegerType)\n\tVarDecl(_VAR2, StringType, StringLit(string))\n])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_func_decl_70(self):
        input = """main: function void() {
                while(123123){
                    if(you==me) print("hell no man");
                    else if(you==him) print("maybe");
                    else print("this is ok now");
                }
            }"""
        expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(IntegerLit(123123), BlockStmt([IfStmt(BinExpr(==, Id(you), Id(me)), CallStmt(print, StringLit(hell no man)), IfStmt(BinExpr(==, Id(you), Id(him)), CallStmt(print, StringLit(maybe)), CallStmt(print, StringLit(this is ok now))))]))]))\n])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_func_decl_71(self):
        input = """main: function void() {
                a: integer = 123*123*123;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(*, BinExpr(*, IntegerLit(123), IntegerLit(123)), IntegerLit(123)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_func_decl_72(self):
        input = """main: function void() {
                a: integer = 123/(123/123);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(/, IntegerLit(123), BinExpr(/, IntegerLit(123), IntegerLit(123))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_func_decl_73(self):
        input = """main: function void() {
                a: integer = 123 % 123 % a;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(%, BinExpr(%, IntegerLit(123), IntegerLit(123)), Id(a)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_func_decl_74(self):
        input = """main: function void() {
                a: integer = --12;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, UnExpr(-, UnExpr(-, IntegerLit(12))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_func_decl_75(self):
        input = """main: function void() {
                a: boolean = !!!b;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, UnExpr(!, UnExpr(!, UnExpr(!, Id(b)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_func_decl_76(self):
        input = """main: function void() {
                a: boolean = !-b;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, UnExpr(!, UnExpr(-, Id(b))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_func_decl_77(self):
        input = """main: function void() {
                a: boolean = 1;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_func_decl_78(self):
        input = """main: function void() {
                a: boolean = 2;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))
