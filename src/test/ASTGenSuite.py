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

    def test_submission(self):
        input ="""
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

main: function void () {
     printInteger(4);
}"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_6(self):
        input = """a: integer;
a = 1 + 2;"""
        expect = """Program([
	VarDecl(a, IntegerType)
	AssignStmt(Id(a), BinExpr(+, IntegerLit(1), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_7(self):
        input = """if (a < b){
    a = 2;
}"""
        expect = """Program([
	IfStmt(BinExpr(<, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_8(self):
        input = """if (true || boolVar){
    a = "phong";
}
else 
{
    a = "ky";
}"""
        expect = """Program([
	IfStmt(BinExpr(||, BooleanLit(True), Id(boolVar)), BlockStmt([AssignStmt(Id(a), StringLit(phong))]), BlockStmt([AssignStmt(Id(a), StringLit(ky))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_9(self):
        input = """x,y,z: array [2_34_5,4,2,5] of integer;"""
        expect = """Program([
	VarDecl(x, ArrayType([2345, 4, 2, 5], IntegerType))
	VarDecl(y, ArrayType([2345, 4, 2, 5], IntegerType))
	VarDecl(z, ArrayType([2345, 4, 2, 5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_10(self):
        input = """a,b,c : float;
a,b,c : float = 1.0, 4.23e2, 0.0002E-2;"""
        expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	VarDecl(a, FloatType, FloatLit(1.0))
	VarDecl(b, FloatType, FloatLit(423.0))
	VarDecl(c, FloatType, FloatLit(2e-06))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_11(self):
        input = """fact : function integer (){
	a,_c,_d : boolean;
a = _c + (a + 13) * (24 * x) / 2 - x;
}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([VarDecl(a, BooleanType), VarDecl(_c, BooleanType), VarDecl(_d, BooleanType), AssignStmt(Id(a), BinExpr(-, BinExpr(+, Id(_c), BinExpr(/, BinExpr(*, BinExpr(+, Id(a), IntegerLit(13)), BinExpr(*, IntegerLit(24), Id(x))), IntegerLit(2))), Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_12(self):
        input = """test = (a + 13) * (24 * x);"""
        expect = """Program([
	AssignStmt(Id(test), BinExpr(*, BinExpr(+, Id(a), IntegerLit(13)), BinExpr(*, IntegerLit(24), Id(x))))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_13(self):
        input = """for(i=0, i<10, i+1)
{ 
    print(i);
}
"""
        expect = """Program([
	ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_14(self):
        input = """result = funct();"""
        expect = """Program([
	AssignStmt(Id(result), CallStmt(funct, ))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_15(self):
        input = """result = funct(passid, 12, true, "string gi foo", 13.34);"""
        expect = """Program([
	AssignStmt(Id(result), CallStmt(funct, Id(passid), IntegerLit(12), BooleanLit(True), StringLit(string gi foo), FloatLit(13.34)))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_16(self):
        input = """result = funct(12) + otherFun(12) + 23;"""
        expect = """Program([
	AssignStmt(Id(result), BinExpr(+, BinExpr(+, CallStmt(funct, IntegerLit(12)), CallStmt(otherFun, IntegerLit(12))), IntegerLit(23)))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_17(self):
        input = """x,y,z: integer = 1,2,3;
        a, b: float;
        n : array [1,3,4,2] of integer;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(n, ArrayType([1, 3, 4, 2], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_18(self):
        input = """in : function void () {
                for( i = 0, i < 1, i + 1){
                        for( j = 0, j < 1 + 1, j + 1){}
                }
        }"""
        expect = """Program([
	FuncDecl(in, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(j, IntegerLit(0)), BinExpr(<, Id(j), BinExpr(+, IntegerLit(1), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_19(self):
        input = """square : function integer (out res: integer, num : integer){
    return num * num;
}"""
        expect = """Program([
	FuncDecl(square, IntegerType, [OutParam(res, IntegerType), Param(num, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(num), Id(num)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_20(self):
        input = """height : function float (inherit out someshitvalue : integer) {
    if (_height == 0) return 1;
    return height(someshitvalue - 1);
}"""
        expect = """Program([
	FuncDecl(height, FloatType, [InheritOutParam(someshitvalue, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(_height), IntegerLit(0)), ReturnStmt(IntegerLit(1))), ReturnStmt(CallStmt(height, BinExpr(-, Id(someshitvalue), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_21(self):
        input = """if (var() <= 0) return var() + 7;"""
        expect = """Program([
	IfStmt(BinExpr(<=, CallStmt(var, ), IntegerLit(0)), ReturnStmt(BinExpr(+, CallStmt(var, ), IntegerLit(7))))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_22(self):
        input = """square : function integer (out res: integer, num : integer) inherit height{
    return num * num;
}
"""
        expect = """Program([
	FuncDecl(square, IntegerType, [OutParam(res, IntegerType), Param(num, IntegerType)], height, BlockStmt([ReturnStmt(BinExpr(*, Id(num), Id(num)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_23(self):
        input = """main: function void() {while (n<11){}; }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(n), IntegerLit(11)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_24(self):
        input = """SortArray: function array[3] of integer() {}"""
        expect = """Program([
	FuncDecl(SortArray, ArrayType([3], IntegerType), [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_25(self):
        input = """SortArray: function array[3, 23_2] of float() {
    for (i = 1, i != (var(123) + 23), i / 3 + 4 * 5){
        return i;
    }
}
"""
        expect = """Program([
	FuncDecl(SortArray, ArrayType([3, 232], FloatType), [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(1)), BinExpr(!=, Id(i), BinExpr(+, CallStmt(var, IntegerLit(123)), IntegerLit(23))), BinExpr(+, BinExpr(/, Id(i), IntegerLit(3)), BinExpr(*, IntegerLit(4), IntegerLit(5))), BlockStmt([ReturnStmt(Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_26(self):
        input = """main: function void() {
            x,y: float = 1.334, 1_342.2e+4;
            n: float = x+y*y;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(1.334)), VarDecl(y, FloatType, FloatLit(13422000.0)), VarDecl(n, FloatType, BinExpr(+, Id(x), BinExpr(*, Id(y), Id(y))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_27(self):
        input = """fooooooo: function void(inherit babyloon : boolean) inherit mainn{
    q,w,e,r,r,ty,r,y,e : boolean = 1,2,3,4,5,6,7,8,9;
    q = w + e - f ;
    return false || q;
}"""
        expect = """Program([
	FuncDecl(fooooooo, VoidType, [InheritParam(babyloon, BooleanType)], mainn, BlockStmt([VarDecl(q, BooleanType, IntegerLit(1)), VarDecl(w, BooleanType, IntegerLit(2)), VarDecl(e, BooleanType, IntegerLit(3)), VarDecl(r, BooleanType, IntegerLit(4)), VarDecl(r, BooleanType, IntegerLit(5)), VarDecl(ty, BooleanType, IntegerLit(6)), VarDecl(r, BooleanType, IntegerLit(7)), VarDecl(y, BooleanType, IntegerLit(8)), VarDecl(e, BooleanType, IntegerLit(9)), AssignStmt(Id(q), BinExpr(-, BinExpr(+, Id(w), Id(e)), Id(f))), ReturnStmt(BinExpr(||, BooleanLit(False), Id(q)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_28(self):
        input = """main: function void() {
            //x = z::y;
            //preventDefault() = x;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_29(self):
        input = """main: function void() {
            x = z::y;
            preventDefault(x);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(::, Id(z), Id(y))), CallStmt(preventDefault, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_30(self):
        input = """x: array [2] of integer ;
main :function void(){
writeln(x[0]);
writeln(x[x[0]]);
return 0;
}"""
        expect = """Program([
	VarDecl(x, ArrayType([2], IntegerType))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(writeln, ArrayCell(Id(x), [IntegerLit(0)])), CallStmt(writeln, ArrayCell(Id(x), [ArrayCell(Id(x), [IntegerLit(0)])])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_31(self):
        input = """a = arr[voi(12,"sad"),aloha[x]];"""
        expect = """Program([
	AssignStmt(Id(a), ArrayCell(Id(arr), [CallStmt(voi, IntegerLit(12), StringLit(sad)), ArrayCell(Id(aloha), [Id(x)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_32(self):
        input = """foo: function void() {
            x: integer = 1;
            if (x == 1) {
                putInt(x);
            }
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), IfStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([CallStmt(putInt, Id(x))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_33(self):
        input = """do {
	break;
	int :integer;
}
while(true);"""
        expect = """Program([
	DoWhileStmt(BooleanLit(True), BlockStmt([BreakStmt(), VarDecl(int, IntegerType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_34(self):
        input = """
        program: function void (arr: array [10,12] of integer, left: integer, right: integer) {
            if (left < right) {
                mid = (left + right)/2;
                sort(arr, left, mid);
                sort(arr, mid + 1, right);
                merge(arr, left, mid, right);
            }
        }
        merge: function void (arr: array [10] of integer, left: integer, mid: integer, right: integer) {
            n1 = mid - left + 1;
            n2 = right - mid;
            left_arr : array [10] of integer;
            right_arr : array [10] of integer;
            for (i = 0, i < n1, i + 1) {
                left_arr[i] = arr[left + i];
            }
            for (j = 0, j < n2, j + 1) {
                right_arr[j] = arr[mid + 1 + j];
            }

            i = 0;
            j = 0;
            k = left;

            while ((i < n1) && (j < n2)) {
                if (left_arr[i] <= right_arr[j]) {
                    arr[k] = left_arr[i];
                    i = i + 1;
                }
                else {
                    arr[k] = right_arr[j];
                    j = j + 1;
                }
                k = k + 1;
            }

            while (i < n1) {
                arr[k] = left_arr[i];
                i = i + 1;
                k = k + 1;
            }

            while (j < n2) {
                arr[k] = right_arr[j];
                j = j + 1;
                k = k + 1;
            }
        }
        """
        expect = """Program([
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10, 12], IntegerType)), Param(left, IntegerType), Param(right, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(left), Id(right)), BlockStmt([AssignStmt(Id(mid), BinExpr(/, BinExpr(+, Id(left), Id(right)), IntegerLit(2))), CallStmt(sort, Id(arr), Id(left), Id(mid)), CallStmt(sort, Id(arr), BinExpr(+, Id(mid), IntegerLit(1)), Id(right)), CallStmt(merge, Id(arr), Id(left), Id(mid), Id(right))]))]))
	FuncDecl(merge, VoidType, [Param(arr, ArrayType([10], IntegerType)), Param(left, IntegerType), Param(mid, IntegerType), Param(right, IntegerType)], None, BlockStmt([AssignStmt(Id(n1), BinExpr(+, BinExpr(-, Id(mid), Id(left)), IntegerLit(1))), AssignStmt(Id(n2), BinExpr(-, Id(right), Id(mid))), VarDecl(left_arr, ArrayType([10], IntegerType)), VarDecl(right_arr, ArrayType([10], IntegerType)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, Id(i), Id(n1)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(Id(left_arr), [Id(i)]), ArrayCell(Id(arr), [BinExpr(+, Id(left), Id(i))]))])), ForStmt(AssignStmt(j, IntegerLit(0)), BinExpr(<, Id(j), Id(n2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(Id(right_arr), [Id(j)]), ArrayCell(Id(arr), [BinExpr(+, BinExpr(+, Id(mid), IntegerLit(1)), Id(j))]))])), AssignStmt(Id(i), IntegerLit(0)), AssignStmt(Id(j), IntegerLit(0)), AssignStmt(Id(k), Id(left)), WhileStmt(BinExpr(&&, BinExpr(<, Id(i), Id(n1)), BinExpr(<, Id(j), Id(n2))), BlockStmt([IfStmt(BinExpr(<=, ArrayCell(Id(left_arr), [Id(i)]), ArrayCell(Id(right_arr), [Id(j)])), BlockStmt([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(left_arr), [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]), BlockStmt([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(right_arr), [Id(j)])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(i), Id(n1)), BlockStmt([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(left_arr), [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(j), Id(n2)), BlockStmt([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(right_arr), [Id(j)])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_35(self):
        input = """
            program: function void (arr: array [10] of integer) {
            n = 10;
            for (i = 0, i < n - 1, i + 1) {
                for (j = 0, j < n - i - 1, j + 1) {
                    if (arr[j] > arr[j + 1]) {
                        temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }
        }"""
        expect = """Program([
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(j, IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(Id(arr), [Id(j)]), ArrayCell(Id(arr), [BinExpr(+, Id(j), IntegerLit(1))])), BlockStmt([AssignStmt(Id(temp), ArrayCell(Id(arr), [Id(j)])), AssignStmt(ArrayCell(Id(arr), [Id(j)]), ArrayCell(Id(arr), [BinExpr(+, Id(j), IntegerLit(1))])), AssignStmt(ArrayCell(Id(arr), [BinExpr(+, Id(j), IntegerLit(1))]), Id(temp))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_36(self):
        input = """program: function void() {
            a = ("a" :: "b") :: "c";
        }"""
        expect = """Program([
	FuncDecl(program, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, BinExpr(::, StringLit(a), StringLit(b)), StringLit(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    # def test_37(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 337))

    # def test_38(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 338))

    # def test_39(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 339))

    # def test_40(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 340))

    # def test_41(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 341))

    # def test_42(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 342))

    # def test_43(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 343))

    # def test_44(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 344))

    # def test_45(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 345))

    # def test_46(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 346))

    # def test_47(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 347))

    # def test_48(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 348))

    # def test_49(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 349))

    # def test_50(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 350))

    # def test_51(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 351))

    # def test_52(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 352))

    # def test_53(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 353))

    # def test_54(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 354))

    # def test_55(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 355))

    # def test_56(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 356))

    # def test_57(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 357))

    # def test_58(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 358))

    # def test_59(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 359))

    # def test_60(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 360))

    # def test_61(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 361))

    # def test_62(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 362))

    # def test_63(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 363))

    # def test_64(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 364))

    # def test_65(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 365))

    # def test_66(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 366))

    # def test_67(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 367))

    # def test_68(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 368))

    # def test_69(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 369))

    # def test_70(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 370))

    # def test_71(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 371))

    # def test_72(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 372))

    # def test_73(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 373))

    # def test_74(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 374))

    # def test_75(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 375))

    # def test_76(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 376))

    # def test_77(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 377))

    # def test_78(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 378))

    # def test_79(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 379))

    # def test_80(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 380))

    # def test_81(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 381))

    # def test_82(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 382))

    # def test_83(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 383))

    # def test_84(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 384))

    # def test_85(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 385))

    # def test_86(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 386))

    # def test_87(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 387))

    # def test_88(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 388))

    # def test_89(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 389))

    # def test_90(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 390))

    # def test_91(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 391))

    # def test_92(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 392))

    # def test_93(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 393))

    # def test_94(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 394))

    # def test_95(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 395))

    # def test_96(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 396))

    # def test_97(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 397))

    # def test_98(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 398))

    # def test_99(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 399))

    # def test_100(self):
    #     input = """"""
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, 400))
