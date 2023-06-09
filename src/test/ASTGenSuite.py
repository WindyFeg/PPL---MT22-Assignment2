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
	ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_14(self):
        input = """result = funct();"""
        expect = """Program([
	AssignStmt(Id(result), FuncCall(funct, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_15(self):
        input = """result = funct(passid, 12, true, "string gi foo", 13.34);"""
        expect = """Program([
	AssignStmt(Id(result), FuncCall(funct, [Id(passid), IntegerLit(12), BooleanLit(True), StringLit(string gi foo), FloatLit(13.34)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_16(self):
        input = """result = funct(12) + otherFun(12) + 23;"""
        expect = """Program([
	AssignStmt(Id(result), BinExpr(+, BinExpr(+, FuncCall(funct, [IntegerLit(12)]), FuncCall(otherFun, [IntegerLit(12)])), IntegerLit(23)))
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
	FuncDecl(in, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(+, IntegerLit(1), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([]))]))]))
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
	FuncDecl(height, FloatType, [InheritOutParam(someshitvalue, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(_height), IntegerLit(0)), ReturnStmt(IntegerLit(1))), ReturnStmt(FuncCall(height, [BinExpr(-, Id(someshitvalue), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_21(self):
        input = """if (var() <= 0) return var() + 7;"""
        expect = """Program([
	IfStmt(BinExpr(<=, FuncCall(var, []), IntegerLit(0)), ReturnStmt(BinExpr(+, FuncCall(var, []), IntegerLit(7))))
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
	FuncDecl(SortArray, ArrayType([3, 232], FloatType), [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(!=, Id(i), BinExpr(+, FuncCall(var, [IntegerLit(123)]), IntegerLit(23))), BinExpr(+, BinExpr(/, Id(i), IntegerLit(3)), BinExpr(*, IntegerLit(4), IntegerLit(5))), BlockStmt([ReturnStmt(Id(i))]))]))
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
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(writeln, ArrayCell(x, [IntegerLit(0)])), CallStmt(writeln, ArrayCell(x, [ArrayCell(x, [IntegerLit(0)])])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_31(self):
        input = """a = arr[voi(12,"sad"),aloha[x]];"""
        expect = """Program([
	AssignStmt(Id(a), ArrayCell(arr, [FuncCall(voi, [IntegerLit(12), StringLit(sad)]), ArrayCell(aloha, [Id(x)])]))
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
	FuncDecl(merge, VoidType, [Param(arr, ArrayType([10], IntegerType)), Param(left, IntegerType), Param(mid, IntegerType), Param(right, IntegerType)], None, BlockStmt([AssignStmt(Id(n1), BinExpr(+, BinExpr(-, Id(mid), Id(left)), IntegerLit(1))), AssignStmt(Id(n2), BinExpr(-, Id(right), Id(mid))), VarDecl(left_arr, ArrayType([10], IntegerType)), VarDecl(right_arr, ArrayType([10], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n1)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(left_arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(left), Id(i))]))])), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(n2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(right_arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, BinExpr(+, Id(mid), IntegerLit(1)), Id(j))]))])), AssignStmt(Id(i), IntegerLit(0)), AssignStmt(Id(j), IntegerLit(0)), AssignStmt(Id(k), Id(left)), WhileStmt(BinExpr(&&, BinExpr(<, Id(i), Id(n1)), BinExpr(<, Id(j), Id(n2))), BlockStmt([IfStmt(BinExpr(<=, ArrayCell(left_arr, [Id(i)]), ArrayCell(right_arr, [Id(j)])), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(left_arr, [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(right_arr, [Id(j)])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(i), Id(n1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(left_arr, [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(j), Id(n2)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(right_arr, [Id(j)])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))]))]))
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
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), BlockStmt([AssignStmt(Id(temp), ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(temp))]))]))]))]))
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

    def test_37(self):
        input = """main: function void (){
    CallStatement();
    result = CallFunction() + 1;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(CallStatement, ), AssignStmt(Id(result), BinExpr(+, FuncCall(CallFunction, []), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_38(self):
        input = """main : function auto (){}"""
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338)) 

    def test_39(self):
        input = """main: function auto(out i: auto){

}"""
        expect = """Program([
	FuncDecl(main, AutoType, [OutParam(i, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_40(self):
        input = """main: function auto(out i: auto){
return i + "\\nsome string;";
}"""
        expect = """Program([
	FuncDecl(main, AutoType, [OutParam(i, AutoType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(i), StringLit(\\nsome string;)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_41(self):
        input = """main: function auto(out i: auto){
break;
for(i = 7, i + 4, i + 0){}
}"""
        expect = """Program([
	FuncDecl(main, AutoType, [OutParam(i, AutoType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(i), IntegerLit(7)), BinExpr(+, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(0)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_42(self):
        input = """main: function auto(out i: auto){
break;
for(i = 7, i + 4, i + 0){
if ((i :: "hello" ) == a) return a;
}
}"""
        expect = """Program([
	FuncDecl(main, AutoType, [OutParam(i, AutoType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(i), IntegerLit(7)), BinExpr(+, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, BinExpr(::, Id(i), StringLit(hello)), Id(a)), ReturnStmt(Id(a)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_43(self):
        input = """Aloha: function auto (){
A,b : integer= !1, b;
}"""
        expect = """Program([
	FuncDecl(Aloha, AutoType, [], None, BlockStmt([VarDecl(A, IntegerType, UnExpr(!, IntegerLit(1))), VarDecl(b, IntegerType, Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_44(self):
        input = """Aloha: function auto (){
A,b : integer= 1+4-3/2/q, q + 4.31/e;
}"""
        expect = """Program([
	FuncDecl(Aloha, AutoType, [], None, BlockStmt([VarDecl(A, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(4)), BinExpr(/, BinExpr(/, IntegerLit(3), IntegerLit(2)), Id(q)))), VarDecl(b, IntegerType, BinExpr(+, Id(q), BinExpr(/, FloatLit(4.31), Id(e))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_45(self):
        input = """What : function string(as: integer){
 a, b: integer = a && true, b || false;
}"""
        expect = """Program([
	FuncDecl(What, StringType, [Param(as, IntegerType)], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(&&, Id(a), BooleanLit(True))), VarDecl(b, IntegerType, BinExpr(||, Id(b), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_46(self):
        input = """a, b, c, d, e, f: integer = 1 == 1, 1 != 1, a > b, a >= b, a < 1, a <= 1;"""
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(==, IntegerLit(1), IntegerLit(1)))
	VarDecl(b, IntegerType, BinExpr(!=, IntegerLit(1), IntegerLit(1)))
	VarDecl(c, IntegerType, BinExpr(>, Id(a), Id(b)))
	VarDecl(d, IntegerType, BinExpr(>=, Id(a), Id(b)))
	VarDecl(e, IntegerType, BinExpr(<, Id(a), IntegerLit(1)))
	VarDecl(f, IntegerType, BinExpr(<=, Id(a), IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_47(self):
        input = """main: function auto(out i: auto){
Ass : string = qw :: wi;
}"""
        expect = """Program([
	FuncDecl(main, AutoType, [OutParam(i, AutoType)], None, BlockStmt([VarDecl(Ass, StringType, BinExpr(::, Id(qw), Id(wi)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_48(self):
        input = """main: function auto(out i: auto){
return qw :: wi;
}"""
        expect = """Program([
	FuncDecl(main, AutoType, [OutParam(i, AutoType)], None, BlockStmt([ReturnStmt(BinExpr(::, Id(qw), Id(wi)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_49(self):
        input = """main: function auto(out i: auto){
return 173.2874E-2;
}"""
        expect = """Program([
	FuncDecl(main, AutoType, [OutParam(i, AutoType)], None, BlockStmt([ReturnStmt(FloatLit(1.732874))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_50(self):
        input = """main: function auto(out i: auto){
return aloha();
}"""
        expect = """Program([
	FuncDecl(main, AutoType, [OutParam(i, AutoType)], None, BlockStmt([ReturnStmt(FuncCall(aloha, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_51(self):
        input = """main: function auto(out i: auto){
return alo[273];
}"""
        expect = """Program([
	FuncDecl(main, AutoType, [OutParam(i, AutoType)], None, BlockStmt([ReturnStmt(ArrayCell(alo, [IntegerLit(273)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_52(self):
        input = """main: function auto(out i: auto){
return alo[ahe("hsisif"::qi)];
}"""
        expect = """Program([
	FuncDecl(main, AutoType, [OutParam(i, AutoType)], None, BlockStmt([ReturnStmt(ArrayCell(alo, [FuncCall(ahe, [BinExpr(::, StringLit(hsisif), Id(qi))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_53(self):
        input = """x: array[2,3] of integer = {1,2,3};"""
        expect = """Program([
	VarDecl(x, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_54(self):
        input = """x: integer = 1;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_55(self):
        input = """a= {1,2,3};"""
        expect = """Program([
	AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_56(self):
        input = """x: boolean = ((((a == b) >= c) < d) > s) != 1_00_00;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(!=, BinExpr(>, BinExpr(<, BinExpr(>=, BinExpr(==, Id(a), Id(b)), Id(c)), Id(d)), Id(s)), IntegerLit(10000)))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_57(self):
        input = """x: boolean = (a && b) || c;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c)))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_58(self):
        input = """x: integer = (1_123 + 2.10e+10) - 1_0_0_0;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1123), FloatLit(21000000000.0)), IntegerLit(1000)))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_59(self):
        input = """x: integer = ((1_123 * 2.10e+10) / 1_0_0_0) % abc;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(1123), FloatLit(21000000000.0)), IntegerLit(1000)), Id(abc)))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_60(self):
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
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_61(self):
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
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_62(self):
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
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_63(self):
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
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_64(self):
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
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_65(self):
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
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_66(self):
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
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_67(self):
        input = """
    testfunc: function void (inherit out a: array[1] of boolean) {
        if(a[1, 2] == "true")
            super(printInteger(a[1*2, 3+4]), x%2);
    }
"""
        expect = """Program([
	FuncDecl(testfunc, VoidType, [InheritOutParam(a, ArrayType([1], BooleanType))], None, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), StringLit(true)), CallStmt(super, FuncCall(printInteger, [ArrayCell(a, [BinExpr(*, IntegerLit(1), IntegerLit(2)), BinExpr(+, IntegerLit(3), IntegerLit(4))])]), BinExpr(%, Id(x), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_68(self):
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
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_69(self):
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
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_70(self):
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
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_71(self):
        input = """
            /* main function */
            mainn: function float () {
                return 1 + 2 + {} - myPI * foo(a[a[0]] - 10 + swap());
            }
        """
        expect = """Program([
	FuncDecl(mainn, FloatType, [], None, BlockStmt([ReturnStmt(BinExpr(-, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), ArrayLit([])), BinExpr(*, Id(myPI), FuncCall(foo, [BinExpr(+, BinExpr(-, ArrayCell(a, [ArrayCell(a, [IntegerLit(0)])]), IntegerLit(10)), FuncCall(swap, []))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_72(self):
        input = """
            /* main function */
            mainn: function float (out n : integer, out i : float) {
                a = true && false;
            }
        """
        expect = """Program([
	FuncDecl(mainn, FloatType, [OutParam(n, IntegerType), OutParam(i, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(&&, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_73(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            mainn: function float (inherit out a : auto) {
                a = true || false;
            }
        """
        expect = """Program([
	VarDecl(factor, IntegerType, FloatLit(10.0))
	FuncDecl(mainn, FloatType, [InheritOutParam(a, AutoType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_74(self):
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
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_75(self):
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
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_76(self):
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
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_77(self):
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
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_78(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function auto () {
                a = true || false;
                b : auto;

            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	VarDecl(str, AutoType, StringLit(abc))
	FuncDecl(main, AutoType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False))), VarDecl(b, AutoType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_79(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function auto () {
                a = true || false;
            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	FuncDecl(main, AutoType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_80(self):
        input = """
            /* main function */
            main: function auto () {
                a = 1_23.04E-56;
            }
        """
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(1.2304e-54))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_81(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function auto () {
                a = "@#$&\t^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@";
            }
        """
        expect = """Program([
	VarDecl(factor, IntegerType, FloatLit(10.0))
	FuncDecl(main, AutoType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(@#$&	^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_82(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function auto () {
                a = "Chuoi cua ban la: \\"12345\\"";

            }
        """
        expect = """Program([
	VarDecl(ac, FloatType, FloatLit(1.2e-09))
	VarDecl(str, AutoType, StringLit(abc))
	FuncDecl(main, AutoType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(Chuoi cua ban la: \\"12345\\"))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_83(self):
        input = """main : function string (){
                a = 1 - foo();
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, IntegerLit(1), FuncCall(foo, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_84(self):
        input = """main : function string (){
                a = 1 - foo(foo(foo()));
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, IntegerLit(1), FuncCall(foo, [FuncCall(foo, [FuncCall(foo, [])])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_85(self):
        input = """main : function string (){
                foo(foo(foo("stupid")));
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([CallStmt(foo, FuncCall(foo, [FuncCall(foo, [StringLit(stupid)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_86(self):
        input = """main:function void() {if(false == true) a = 1; else a = 0;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, BooleanLit(False), BooleanLit(True)), AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_87(self):
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
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_88(self):
        input = """delta123 : integer = 1+1-1*2/3%3;"""
        expect = """Program([
	VarDecl(delta123, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(3))))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_89(self):
        input = """main:function string (){
                a = "hello"::"world"; 
                b = 1+2; 
                return a;
        }"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, StringLit(hello), StringLit(world))), AssignStmt(Id(b), BinExpr(+, IntegerLit(1), IntegerLit(2))), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_90(self):
        input = """main: function void() inherit abc {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], abc, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_91(self):
        input = """abc:integer;main: function void(xyz:integer, def:integer) inherit hehe {}"""
        expect = """Program([
	VarDecl(abc, IntegerType)
	FuncDecl(main, VoidType, [Param(xyz, IntegerType), Param(def, IntegerType)], hehe, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_92(self):
        input = """main:function string (){a = 2; return;}"""
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_93(self):
        input = """main: function void() {
                if(a==1) a=1;
                if(a==1) a=2; else a=3;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1))), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(a), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_94(self):
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
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_95(self):
        input ="""main: function void() {
                a: boolean = 2;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_96(self):
        input = """
            main: function boolean () {}
        """
        expect = """Program([
	FuncDecl(main, BooleanType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_97(self):
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
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_98(self):
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
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_99(self):
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
        self.assertTrue(TestAST.test(input, expect, 399))

#     def test_100(self):
#         input = """//a
# /*
# */
# x, y: integer = 65, 88;
# fact: function integer (n: integer) {
#     if (1) if (1) a(); else if (b) if (c) b(); else p(p(3),p());
#     if (n==0) return 1;
#     else return n * fact(n-1);
#     a = ((1 < 2) + (1 <= 2) + (1 > 2)+ (1 != 2)+ (1 == 2)) >= a(a(1));

# }
# inc: function void (out n: integer, delta: integer) inherit _____a {
#     n = n + !!!delta * --3 / a[1,2,3,4,5];
#     a = !!!---a();
#     b();
#     a = 1.2 + a + b(n-1,a,a(d-1), a[1,1,1], {}) - c * d::e || {} - -a && !!9 % a / 2 == 2;
# }

# sd: integer = true::false;
# if_func: function auto (inherit out n: integer, inherit delta: array[3] of boolean) {
#     if (a) while(a) while(a) while(a) do {} while("a"); else break;
#     for(x=x,x,x) if (a) if (b) continue;
#     //a = b= b= b= b=b= c= d= j[j[1]];
#     delta: array[9,9,9,9] of boolean;
#     a = a && b || !!!v;
#     a = {1,2,3,4} :: 2 * --3;
#     if (a == 0) {if (a == 1) a = 1;} else a = 3;

#     if (b == 0) if (b == 1) a = 1; else b = 3;
#     return ---1 + foo(a) * 9;
#     a = !true + false;
#     for (a[1] = 3, a == 9, a < 9) m = n::p;

# }

# main: function void() {
#     delta: integer = fact(3);
#     inc(x, delta);
#     printInteger(x);
#     m = a + b + v;
#     a, b, c, d: integer = 3::3.3, 4e4, 1.6e9, 10_2_2;
#     a, b, c, d, e: string = 3, 4, true, !10, 4 + 2;
#     a[0,2,3] = s;
#     while (1 == 2) {
#         a = 1 + 3 - 9;
#     }
#     a = b[3];
#     continue;
#     break;
#     {
#         return 1;
#     }
#     do {
#         for (x = 3,x ,x) {
#             for (x = 3, "conga" ,true/false) a[9] = 0;
#         }
#         while (!!a) {
#             while (a) a[3] = b[3];
#         }
#     } while ({1::2,2,3,4} * {1,2} + a[2] + a());    
# }

# """
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(65))
# 	VarDecl(y, IntegerType, IntegerLit(88))
# 	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(IntegerLit(1), IfStmt(IntegerLit(1), CallStmt(a, ), IfStmt(Id(b), IfStmt(Id(c), CallStmt(b, ), CallStmt(p, FuncCall(p, [IntegerLit(3)]), FuncCall(p, [])))))), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))])))), AssignStmt(Id(a), BinExpr(>=, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(<, IntegerLit(1), IntegerLit(2)), BinExpr(<=, IntegerLit(1), IntegerLit(2))), BinExpr(>, IntegerLit(1), IntegerLit(2))), BinExpr(!=, IntegerLit(1), IntegerLit(2))), BinExpr(==, IntegerLit(1), IntegerLit(2))), FuncCall(a, [FuncCall(a, [IntegerLit(1)])])))]))
# 	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], _____a, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), BinExpr(/, BinExpr(*, UnExpr(!, UnExpr(!, UnExpr(!, Id(delta)))), UnExpr(-, UnExpr(-, IntegerLit(3)))), ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])))), AssignStmt(Id(a), UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(-, UnExpr(-, UnExpr(-, FuncCall(a, [])))))))), CallStmt(b, ), AssignStmt(Id(a), BinExpr(::, BinExpr(-, BinExpr(+, BinExpr(+, FloatLit(1.2), Id(a)), FuncCall(b, [BinExpr(-, Id(n), IntegerLit(1)), Id(a), FuncCall(a, [BinExpr(-, Id(d), IntegerLit(1))]), ArrayCell(a, [IntegerLit(1), IntegerLit(1), IntegerLit(1)]), ArrayLit([])])), BinExpr(*, Id(c), Id(d))), BinExpr(==, BinExpr(&&, BinExpr(||, Id(e), BinExpr(-, ArrayLit([]), UnExpr(-, Id(a)))), BinExpr(/, BinExpr(%, UnExpr(!, UnExpr(!, IntegerLit(9))), Id(a)), IntegerLit(2))), IntegerLit(2))))]))
# 	VarDecl(sd, IntegerType, BinExpr(::, BooleanLit(True), BooleanLit(False)))
# 	FuncDecl(if_func, AutoType, [InheritOutParam(n, IntegerType), InheritParam(delta, ArrayType([3], BooleanType))], None, BlockStmt([IfStmt(Id(a), WhileStmt(Id(a), WhileStmt(Id(a), WhileStmt(Id(a), DoWhileStmt(StringLit(a), BlockStmt([]))))), BreakStmt()), ForStmt(AssignStmt(Id(x), Id(x)), Id(x), Id(x), IfStmt(Id(a), IfStmt(Id(b), ContinueStmt()))), VarDecl(delta, ArrayType([9, 9, 9, 9], BooleanType)), AssignStmt(Id(a), BinExpr(||, BinExpr(&&, Id(a), Id(b)), UnExpr(!, UnExpr(!, UnExpr(!, Id(v)))))), AssignStmt(Id(a), BinExpr(::, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), BinExpr(*, IntegerLit(2), UnExpr(-, UnExpr(-, IntegerLit(3)))))), IfStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1)))]), AssignStmt(Id(a), IntegerLit(3))), IfStmt(BinExpr(==, Id(b), IntegerLit(0)), IfStmt(BinExpr(==, Id(b), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(b), IntegerLit(3)))), ReturnStmt(BinExpr(+, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(1)))), BinExpr(*, FuncCall(foo, [Id(a)]), IntegerLit(9)))), AssignStmt(Id(a), BinExpr(+, UnExpr(!, BooleanLit(True)), BooleanLit(False))), ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(1)]), IntegerLit(3)), BinExpr(==, Id(a), IntegerLit(9)), BinExpr(<, Id(a), IntegerLit(9)), AssignStmt(Id(m), BinExpr(::, Id(n), Id(p))))]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x)), AssignStmt(Id(m), BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(v))), VarDecl(a, IntegerType, BinExpr(::, IntegerLit(3), FloatLit(3.3))), VarDecl(b, IntegerType, FloatLit(40000.0)), VarDecl(c, IntegerType, FloatLit(1600000000.0)), VarDecl(d, IntegerType, IntegerLit(1022)), VarDecl(a, StringType, IntegerLit(3)), VarDecl(b, StringType, IntegerLit(4)), VarDecl(c, StringType, BooleanLit(True)), VarDecl(d, StringType, UnExpr(!, IntegerLit(10))), VarDecl(e, StringType, BinExpr(+, IntegerLit(4), IntegerLit(2))), AssignStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(2), IntegerLit(3)]), Id(s)), WhileStmt(BinExpr(==, IntegerLit(1), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(3)), IntegerLit(9)))])), AssignStmt(Id(a), ArrayCell(b, [IntegerLit(3)])), ContinueStmt(), BreakStmt(), BlockStmt([ReturnStmt(IntegerLit(1))]), DoWhileStmt(BinExpr(+, BinExpr(+, BinExpr(*, ArrayLit([BinExpr(::, IntegerLit(1), IntegerLit(2)), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(1), IntegerLit(2)])), ArrayCell(a, [IntegerLit(2)])), FuncCall(a, [])), BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(3)), Id(x), Id(x), BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(3)), StringLit(conga), BinExpr(/, BooleanLit(True), BooleanLit(False)), AssignStmt(ArrayCell(a, [IntegerLit(9)]), IntegerLit(0)))])), WhileStmt(UnExpr(!, UnExpr(!, Id(a))), BlockStmt([WhileStmt(Id(a), AssignStmt(ArrayCell(a, [IntegerLit(3)]), ArrayCell(b, [IntegerLit(3)])))]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 400))