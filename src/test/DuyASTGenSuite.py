import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

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

    def test_full_vardecl_concate_1(self):
        input = """x: auto = a :: b;"""
        expect = """Program([
	VarDecl(x, AutoType, BinExpr(::, Id(a), Id(b)))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_full_vardecl_concate_2(self):
        input = """x, y: float = a :: b, (a_sdq :: sda) :: asw; """
        expect = """Program([
	VarDecl(x, FloatType, BinExpr(::, Id(a), Id(b)))
	VarDecl(y, FloatType, BinExpr(::, BinExpr(::, Id(a_sdq), Id(sda)), Id(asw)))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
    
    def test_full_vardecl_concate_3(self):
        input = """x, y: array [1_02, 23] of string = (\"he slo ae\" :: true) :: (1_23.0e-10 :: a), (a_sdq :: sda) :: asw; """
        expect = """Program([
	VarDecl(x, ArrayType([102, 23], StringType), BinExpr(::, BinExpr(::, StringLit(he slo ae), BooleanLit(True)), BinExpr(::, FloatLit(1.23e-08), Id(a))))
	VarDecl(y, ArrayType([102, 23], StringType), BinExpr(::, BinExpr(::, Id(a_sdq), Id(sda)), Id(asw)))
])"""

        self.assertTrue(TestAST.test(input, expect, 307))
    
    def test_full_vardecl_compares(self):
        input = """x: boolean = ((((a == b) >= c) < d) > s) != 1_00_00;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(!=, BinExpr(>, BinExpr(<, BinExpr(>=, BinExpr(==, Id(a), Id(b)), Id(c)), Id(d)), Id(s)), IntegerLit(10000)))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_full_vardecl_andor(self):
        input = """x: boolean = (a && b) || c;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c)))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_full_vardecl_operator1(self):
        input = """x: integer = (1_123 + 2.10e+10) - 1_0_0_0;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1123), FloatLit(21000000000.0)), IntegerLit(1000)))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_full_vardecl_operator2(self):
        input = """x: integer = ((1_123 * 2.10e+10) / 1_0_0_0) % abc;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(1123), FloatLit(21000000000.0)), IntegerLit(1000)), Id(abc)))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_full_vardecl_negation(self):
        input = """x, y, z: integer = !ab, !(!a), !(!(!b));"""
        expect = """Program([
	VarDecl(x, IntegerType, UnExpr(!, Id(ab)))
	VarDecl(y, IntegerType, UnExpr(!, UnExpr(!, Id(a))))
	VarDecl(z, IntegerType, UnExpr(!, UnExpr(!, UnExpr(!, Id(b)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
    
    def test_full_vardecl_index(self):
        input = """x: integer = a[1 + 2, a == b, \"hello\", !a_SADsd, 3 * 3.0];"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(==, Id(a), Id(b)), StringLit(hello), UnExpr(!, Id(a_SADsd)), BinExpr(*, IntegerLit(3), FloatLit(3.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))


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

    def test_assignstmt_program_1(self):
        input = """main: function void () {
            a = b;
            as = c + 2.0e-3;
            ass = (\"Hello\" + \"asdas\") :: 10_20.1e2;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(as), BinExpr(+, Id(c), FloatLit(0.002))), AssignStmt(Id(ass), BinExpr(::, BinExpr(+, StringLit(Hello), StringLit(asdas)), FloatLit(102010.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))   


    def test_assignstmt_program_2(self):
        input = """main: function void () {
            a[1_0, 2] = b >= a;
            a[1] = arr[1];

        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(10), IntegerLit(2)]), BinExpr(>=, Id(b), Id(a))), AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayCell(arr, [IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
    
    def test_ifstmt_program_1(self):
        input = """main: function void () {
           if (DSAD == b) print(2_213_1231);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(DSAD), Id(b)), CallStmt(print, IntegerLit(22131231)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316)) 
    
    def test_ifstmt_program_2(self):
        """if with blockstmt"""
        input = """main: function void(){
                    if ((x > 1) && (x <= 10)) 
                        {
                            y = 2;
                            continue;
                        }
                    }
                """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(>, Id(x), IntegerLit(1)), BinExpr(<=, Id(x), IntegerLit(10))), BlockStmt([AssignStmt(Id(y), IntegerLit(2)), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317)) 

    def test_ifstmt_program_3(self):
        """if else with blockstmt"""
        input = """main: function void () {
           if ((DSAD == b) && (a :: b))  {
                return asdasdads();
           }
           else {
                if (a + 1 == 2) break;
           }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(==, Id(DSAD), Id(b)), BinExpr(::, Id(a), Id(b))), BlockStmt([ReturnStmt(FuncCall(asdasdads, []))]), BlockStmt([IfStmt(BinExpr(==, BinExpr(+, Id(a), IntegerLit(1)), IntegerLit(2)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318)) 

    def test_forstmt_program_1(self):
        """for statement"""
        input = """main: function void () {
             for ( i = a::b, i <= 1_12, (-i) + 1)
                printInteger();
           }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(::, Id(a), Id(b))), BinExpr(<=, Id(i), IntegerLit(112)), BinExpr(+, UnExpr(-, Id(i)), IntegerLit(1)), CallStmt(printInteger, ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319)) 
    
    def test_forstmt_program_2(self):
        """for statement wwith blockstmt"""
        input = """main: function void () {
             for ( i = a::b, i <= 1_12, (-i) + 1)
                {
                    printInteger();
                    a: integer = 10_23; 
                    return a + 1;
                }
           }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(::, Id(a), Id(b))), BinExpr(<=, Id(i), IntegerLit(112)), BinExpr(+, UnExpr(-, Id(i)), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ), VarDecl(a, IntegerType, IntegerLit(1023)), ReturnStmt(BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320)) 
    
    def test_forstmt_program_3(self):
        """for statement wwith blockstmt"""
        input = """main: function void () {
             for ( i = a::b, i <= 1_12, (-i) + 1)
                {
                    if ((a && b) >= 1.21) return helloworld();
                    else break;
                    a,b: array[2] of integer;
                }
           }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(::, Id(a), Id(b))), BinExpr(<=, Id(i), IntegerLit(112)), BinExpr(+, UnExpr(-, Id(i)), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>=, BinExpr(&&, Id(a), Id(b)), FloatLit(1.21)), ReturnStmt(FuncCall(helloworld, [])), BreakStmt()), VarDecl(a, ArrayType([2], IntegerType)), VarDecl(b, ArrayType([2], IntegerType))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321)) 

    def test_whilestmt_program_1(self):
        """while statement without blockstmt"""
        input = """ASDASD: function boolean(inherit out a: auto, out b: array [2] of string) inherit a
        {
            while( a >= b ) return a();
        }
        """
        expect = """Program([
	FuncDecl(ASDASD, BooleanType, [InheritOutParam(a, AutoType), OutParam(b, ArrayType([2], StringType))], a, BlockStmt([WhileStmt(BinExpr(>=, Id(a), Id(b)), ReturnStmt(FuncCall(a, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322)) 
    

    def test_whilestmt_program_2(self):
        """while statement without blockstmt"""
        input = """ASDASD: function boolean(inherit out a: auto, out b: array [2] of string) inherit a
        {
            while( a >= b ) 
                if (a == n) return printInteger(); 
                else break;
        }
        """
        expect = """Program([
	FuncDecl(ASDASD, BooleanType, [InheritOutParam(a, AutoType), OutParam(b, ArrayType([2], StringType))], a, BlockStmt([WhileStmt(BinExpr(>=, Id(a), Id(b)), IfStmt(BinExpr(==, Id(a), Id(n)), ReturnStmt(FuncCall(printInteger, [])), BreakStmt()))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323)) 

    def test_whilestmt_program_3(self):
        """while statement with blockstmt"""
        input = """main: function void()
        {
            while( a >= b ) {
                a,b,c: integer = 1,2,3;
                a[1] = 1.2;
                break;    
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>=, Id(a), Id(b)), BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3)), AssignStmt(ArrayCell(a, [IntegerLit(1)]), FloatLit(1.2)), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324)) 
    
    def test_whilestmt_program_4(self):
        """while statement with blockstmt"""
        input = """main: function void()
        {
            while( a >= b ) {
                while(a == b) {
                    break;
                }  
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>=, Id(a), Id(b)), BlockStmt([WhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([BreakStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325)) 
    

    def test_whilestmt_program_5(self):
        """while statement with blockstmt"""
        input = """main: function void()
        {
            while( a >= b ) {
                while(a == b) {
                    while (a <= b) 
                    {
                        {break;}
                    }
                }  
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(>=, Id(a), Id(b)), BlockStmt([WhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([WhileStmt(BinExpr(<=, Id(a), Id(b)), BlockStmt([BlockStmt([BreakStmt()])]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326)) 
    
    def test_dowhilestmt_program_1(self):
        input = """main: function void()
        {
           do {a = a + 1;} while(a == b);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
    
    def test_dowhilestmt_program_2(self):
        input = """main: function void()
        {
           do {{{a = a + 1;}}} while(a[1] == b);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1)]), Id(b)), BlockStmt([BlockStmt([BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
    
    
 

# -----------------------TESTCASE--------------------------------
    def testcase29(self):
        # test vardecl with init of expression
        input = """x, y: integer = 1*2, 2+3;
                    a: string = "abc" :: "def";"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))
	VarDecl(y, IntegerType, BinExpr(+, IntegerLit(2), IntegerLit(3)))
	VarDecl(a, StringType, BinExpr(::, StringLit(abc), StringLit(def)))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def testcase30(self):
        # test vardecl with init of expression
        input = """x, y: integer = 1*2, 2+3;
                    a: string = "abc" :: "def";
                    a: integer = a[1+2, 1*5];"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))
	VarDecl(y, IntegerType, BinExpr(+, IntegerLit(2), IntegerLit(3)))
	VarDecl(a, StringType, BinExpr(::, StringLit(abc), StringLit(def)))
	VarDecl(a, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def testcase31(self):
        # test vardecl with init of expression
        input = """x, y: integer = 1*2, 2+3;
                    a: string = "abc" :: "def";
                    d: integer = a[1+2, 1*5];
                    c: string = a(1, f("abc"));"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))
	VarDecl(y, IntegerType, BinExpr(+, IntegerLit(2), IntegerLit(3)))
	VarDecl(a, StringType, BinExpr(::, StringLit(abc), StringLit(def)))
	VarDecl(d, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(5))]))
	VarDecl(c, StringType, FuncCall(a, [IntegerLit(1), FuncCall(f, [StringLit(abc)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def testcase32(self):
        # test vardecl with no init of array
        input = """x: array[2,3] of integer = {1,2,3};"""
        expect = """Program([
	VarDecl(x, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def testcase33(self):
        # test basic funcdecls
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
        printInteger(4);
}"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def testcase34(self):
        # test funcdecls
        input = """main: function void () {
        x: integer;
        x = (3+4)*2;
        b: array [2] of float;
        b[0] = 4.5;
        preventDefault();
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), BinExpr(*, BinExpr(+, IntegerLit(3), IntegerLit(4)), IntegerLit(2))), VarDecl(b, ArrayType([2], FloatType)), AssignStmt(ArrayCell(b, [IntegerLit(0)]), FloatLit(4.5)), CallStmt(preventDefault, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def testcase35(self):
        # ifstmt without blockstmt and else
        input = """
    main: function void () {
        if (3 > 4 + 5) a[0] = "hello world";
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(3), BinExpr(+, IntegerLit(4), IntegerLit(5))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(hello world)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def testcase36(self):
        # ifstmt without blockstmt but have else
        input = """
    main: function void () {
        if (3 > 4 + 5) a[0] = "hello world";
        else a[0] = "hello world in else";
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(3), BinExpr(+, IntegerLit(4), IntegerLit(5))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(hello world)), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(hello world in else)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def testcase37(self):
        # forstmt without block
        input = """
    a,b,c : array [2] of integer = {1,1}, {2,2}, {3,5-4};
    main: function void () {
        for (i=1,i<100,i+1) break;
}"""
        expect = """Program([
	VarDecl(a, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(1)]))
	VarDecl(b, ArrayType([2], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(2)]))
	VarDecl(c, ArrayType([2], IntegerType), ArrayLit([IntegerLit(3), BinExpr(-, IntegerLit(5), IntegerLit(4))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def testcase38(self):
        # forstmt with block
        input = """
    main: function void () {
        for (i=1,i<100,i+1) {
            if (a<1) continue;
            a: boolean = false;
        }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, Id(a), IntegerLit(1)), ContinueStmt()), VarDecl(a, BooleanType, BooleanLit(False))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def testcase39(self):
        # whilestmt without block
        input = """
    testfunc: function integer (a: integer) {
        while (a < 10) a = a + 1;
        return a + 3;
    }
    main: function void () {
        testfunc();
}"""
        expect = """Program([
	FuncDecl(testfunc, IntegerType, [Param(a, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))), ReturnStmt(BinExpr(+, Id(a), IntegerLit(3)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(testfunc, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def testcase40(self):
        # whilestmt with block
        input = """
    testfunc: function integer (a: integer) {
        while (a < 10) {
            for(i = 1, i < 10, i + 1) a = a + 1;
        }
        readBoolean(a==10);
        return a + 3;
    }
    main: function void () {
        testfunc();
}"""
        expect = """Program([
	FuncDecl(testfunc, IntegerType, [Param(a, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))])), CallStmt(readBoolean, BinExpr(==, Id(a), IntegerLit(10))), ReturnStmt(BinExpr(+, Id(a), IntegerLit(3)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(testfunc, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def testcase41(self):
        # dowhile
        input = """
    testfunc: function integer (c: string) {
        do {
            readString("abc");
            c = c :: "abc";
            printString(c);
        } while (c != "" );
        return 1;
    }
    main: function void () {
        testfunc();
}"""
        expect = """Program([
	FuncDecl(testfunc, IntegerType, [Param(c, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(c), StringLit()), BlockStmt([CallStmt(readString, StringLit(abc)), AssignStmt(Id(c), BinExpr(::, Id(c), StringLit(abc))), CallStmt(printString, Id(c))])), ReturnStmt(IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(testfunc, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def testcase42(self):
        input = """
    testfunc: function auto (a: boolean) {
        while (a < 10) {
            {
                a = a + 1;
            }
        }
    }
"""
        expect = """Program([
	FuncDecl(testfunc, AutoType, [Param(a, BooleanType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def testcase43(self):
        input = """
    testfunc: function string (a: boolean) {
        x: float = 1.5e-10 + x + y;
    }
"""
        expect = """Program([
	FuncDecl(testfunc, StringType, [Param(a, BooleanType)], None, BlockStmt([VarDecl(x, FloatType, BinExpr(+, BinExpr(+, FloatLit(1.5e-10), Id(x)), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def testcase44(self):
        input = """
    testfunc: function void (inherit out a: array[1] of boolean) {
        if(a[1, 2] == "true")
            super(printInteger(a[1*2, 3+4]), x%2);
    }
"""
        expect = """Program([
	FuncDecl(testfunc, VoidType, [InheritOutParam(a, ArrayType([1], BooleanType))], None, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), StringLit(true)), CallStmt(super, FuncCall(printInteger, [ArrayCell(a, [BinExpr(*, IntegerLit(1), IntegerLit(2)), BinExpr(+, IntegerLit(3), IntegerLit(4))])]), BinExpr(%, Id(x), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def testcase45(self):
        input = """
    testfunc: function void (inherit out a: array[2, 3] of boolean) inherit foo {
        if(a[a[1, 2], 2] == "true") {
            {
                {
                    a[a[a[1, 2], 3], 2] = "false";
                }
            }
        }
            
    }
"""
        expect = """Program([
	FuncDecl(testfunc, VoidType, [InheritOutParam(a, ArrayType([2, 3], BooleanType))], foo, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), IntegerLit(2)]), StringLit(true)), BlockStmt([BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), IntegerLit(3)]), IntegerLit(2)]), StringLit(false))])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))



