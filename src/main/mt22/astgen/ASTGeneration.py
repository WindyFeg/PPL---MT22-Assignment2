from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    #@ 1. Program

    #% program: decls;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decls()))

    #% decls: decl decls | decl;
    # ! Return a list 
    def visitDecls(self, ctx: MT22Parser.decls):
        if ctx.decls():
            return self.visit(ctx.decl()) + self.visit(ctx.decls())
        return self.visit(ctx.decl())
    
    #% decl: functiondecl |variabledecl | statementlist |mainfunction;
    def visitDecl(self, ctx: MT22Parser.decl):
        if ctx.functiondecl():
            return self.visit(ctx.functiondecl())
        elif ctx.variabledecl():
            return self.visit(ctx.variabledecl())
        elif ctx.statementlist():
            return self.visit(ctx.statementlist())
        return self.visit(ctx.mainfunction())

    #@ 2. Declaration
    #@ 2.1 Function declare

    #@ 2.1.1 Main function
    #% mainfunction: functionmainprot functionbody;
    def visitMainfunction(self, ctx: MT22Parser.mainfunction):
        mf_name, mf_return_type, mf_params, mf_inherit = self.visit(ctx.functionmainprot())
        return FuncDecl(
            mf_name,
            mf_return_type,
            mf_params,
            mf_inherit,
            self.visit(ctx.functionbody()) # BlockStmt
        )
    
    #% functionmainprot:MAIN COL FUNCTION (VOID|AUTO) LB parameterlist? RB (INHERIT ID)?;
    def visitFunctionmainprot(self, ctx: MT22Parser.functionmainprot):
        mf_name = ctx.MAIN().getText()
        mf_return_type = ctx.VOID().getText() if ctx.VOID() else self.visit(ctx.vartype())
        mf_params = self.visit(ctx.parameterlist())
        mf_inherit = self.visit(ctx.Id())
        return mf_name, mf_return_type, mf_params, mf_inherit
    
    #@ 2.1.2 Normal function
    #% functiondecl: functionprot functionbody;
    def visitFunctiondecl(self, ctx: MT22Parser.functiondecl):
        f_name, f_return_type, f_params, f_inherit = self.visit(ctx.functionprot())
        return FuncDecl(
            f_name,
            f_return_type,
            f_params,
            f_inherit,
            self.visit(ctx.functionbody()) # BlockStmt
        )
    
    #% functionprot: ID COL FUNCTION (VOID|vartype) LB parameterlist? RB (INHERIT ID)?;
    def visitFunctionprot(self, ctx: MT22Parser.functionprot):
        f_name = self.visit(ctx.Id())
        f_return_type = ctx.VOID().getText() if ctx.VOID() else self.visit(ctx.vartype()) 
        f_params = self.visit(ctx.parameterlist())
        f_inherit = self.visit(ctx.Id())
        return f_name, f_return_type, f_params, f_inherit

    #@ 2.2 Variable declare
    #%variabledecl: (variabledeclassign|variabledecls) SEM;
    def visitVariabledecl(self, ctx: MT22Parser.variabledecl):
        if ctx.variabledeclassign():
            # [("a", 3), ("b", 2), ("c", 1)]
            idList, expList = [], []
            for tup in [self.visit(ctx.variabledeclassign())]:
                idList.append(tup[0])
                expList.append(tup[1])
            return list(map(
                lambda id, exp: VarDecl(id, exp),
                idList,
                expList[::-1]
            ))
        return self.visit(ctx.variabledecls())

    #% variabledecls:idlist COL vartype;
    def visitVariabledecls(self, ctx: MT22Parser.variabledecls):
        idList = self.visit(ctx.idlist())
        varType = self.visit(ctx.vartype())
        return [VarDecl(id, varType) for id in idList]

    #% variabledeclassign: ID COMA variabledeclassign COMA expression
    #% | ID COL vartype EQU expression;
    def visitVariabledeclassign(self, ctx: MT22Parser.variabledeclassign):
        if ctx.vartype():
            return [(ctx.ID().getText(), ctx.expression())]
        return [(ctx.ID().getText(), ctx.expression())] + self.visit(ctx.variabledeclassign())
    
    #@ 3. LIST
    #@ 3.1. Parameter list
    #% parameterlist: parameter COMA parameterlist| parameter;
    def visitParameterlist(self, ctx: MT22Parser.parameterlist):
        if ctx.parameterlist():
            return [self.visit(ctx.parameter())] + self.visit(ctx.parameterlist())
        return [self.visit(ctx.parameter())]

    #% parameter: INHERIT? OUT? ID COL vartype;
    def visitParameter(self, ctx: MT22Parser.parameter):
        return ParamDecl(
            str(ctx.Id().getText()),
            self.visit(ctx.vartype()),
            True if ctx.OUT() else False,
            True if ctx.INHERIT() else False
        )
    
    #@ 3.2. ID list
    #% idlist: ID  COMA idlist | ID;
    def visitIdlist(self, ctx: MT22Parser.idlist):
        if ctx.idlist():
            return [ctx.ID().getText()] + self.visit(ctx.idlist())
        return [ctx.ID().getText()]
    
    #@ 3.3. Expression list
    #% expressionlist: expression COMA expressionlist| expression SEM?;
    def visitExpressionlist(self, ctx: MT22Parser.expressionlist):
        if ctx.expressionlist():
            return [self.visit(ctx.expression())] + self.visit(ctx.expressionlist())
        return [self.visit(ctx.expression())]

    #@ 4. STATEMENT

    #@ 5. EXPRESSION
    #%  stringop: SCOPE;
    def visitStringop(self, ctx: MT22Parser.stringop):
        return str(ctx.SCOPE().getText())
    
    #% relationalop: EQUL | NEQ | LESS | GREA | LOEQ | GOEQ;
    def visitRelationalop(self, ctx: MT22Parser.relationalop):
        return str(ctx.getText())

    #% indexexpression: ID indexop;
    def visitIndexexpression(self, ctx: MT22Parser.indexexpression):
        return ArrayCell(
            Id(ctx.ID().getText()),
            #! return Expr list
            self.visit(ctx.indexop())
        )
    
    #%indexop:LSB expressionlist RSB;
    def visitIndexop(self, ctx: MT22Parser.indexop):
        return self.visit(ctx.expressionlist())

    #% operand: constant | functioncall | ID |subexpression ;

    #% constant: STR | BOOL | FLO | INT | arr;

    #@ 5.1. Binary expression
    #% expression: expression_relat stringop expression_relat | expression_relat;
    def visitExpression(self, ctx: MT22Parser.expression):
        if ctx.stringop(): 
            return BinExpr(
                self.visit(ctx.stringop()),
                self.visit(ctx.expression_relat(0)),
                self.visit(ctx.expression_relat(1))
            )
        return self.visit(ctx.expression_relat())
    
    #%expression_relat: expression_logic relationalop expression_logic |expression_logic ;
    def visitExpression_relat(self, ctx: MT22Parser.expression_relat):
        if ctx.relationalop():
            return BinExpr(
                self.visit(ctx.relationalop()),
                self.visit(ctx.expression_logic(0)),
                self.visit(ctx.expression_logic(1))
            )
        return self.visit(ctx.expression_logic())
    
    #% expression_logic: expression_logic (AND|OR) expression_bina1|expression_bina1;
    def visitExpression_logic(self, ctx: MT22Parser.expression_logic):
        if ctx.AND() or ctx.OR():
            return BinExpr(
                str(ctx.getChild(1).getText()),
                self.visit(ctx.expression_logic()),
                self.visit(ctx.expression_bina1(0))
            )
        return self.visit(ctx.expression_bina1())

    #% expression_bina1: expression_bina1 (PLUS|MINU) expression_bina2|expression_bina2;
    def visitExpression_bina1(self, ctx: MT22Parser.expression_bina1):
        if ctx.PLUS() or ctx.MINU():
            return BinExpr(
                str(ctx.getChild(1).getText()),
                self.visit(ctx.expression_bina1()),
                self.visit(ctx.expression_bina2(0))
            )
        return self.visit(ctx.expression_bina2())

    #%expression_bina2: expression_bina2 (MUTI|DIVI|MODU) expression_unary | expression_unary;
    def visitExpression_bina2(self, ctx: MT22Parser.expression_bina2):
        if ctx.MUTI() or ctx.DIVI() or ctx.MODU():
            return BinExpr(
                str(ctx.getChild(1).getText()),
                self.visit(ctx.expression_bina2()),
                self.visit(ctx.expression_unary(0))
            )
        return self.visit(ctx.expression_unary())
    
    #@ 5.2. Unary expression
    #% expression_unary: NOT operand
    #% | MINU operand
    #% | indexexpression
    #% | operand;
    def visitExpression_unary(self, ctx: MT22Parser.expression_unary):
        if ctx.NOT():
            return UnExpr(
                str(ctx.NOT().getText()),
                self.visit(ctx.operand())
            )
        elif ctx.MINU():
            return UnExpr(
                str(ctx.MINU().getText()),
                self.visit(ctx.operand())
            )
        # a[1,2,3]
        elif ctx.indexexpression():
            #! return arrayCell
            return self.visit(ctx.indexexpression())
        else:
            #! return Expr type
            return self.visit(ctx.operand())

    #@ TYPE & ARRAY
    #% vartype: atomictype | arraytype ;
    def visitVartype(self, ctx: MT22Parser.vartype):
        if ctx.atomictype():
            return self.visit(ctx.atomictype())
        return self.visit(ctx.arraytype())

    #@ Array
    #% arraytype:ARRAY (LSB dimension RSB OF atomictype)?;
    def visitArraytype(self, ctx: MT22Parser.arraytype):
        return ArrayType(self.visit(ctx.dimension()), 
                         self.visit(ctx.atomictype()))
    
    #% dimension: INT COMA dimension | INT;
    def visitDimension(self, ctx: MT22Parser.dimension):
        if ctx.dimension():
            return [self.visit(ctx.INT(0))] + self.visit(ctx.dimension())
        return [self.visit(ctx.INT(0))]

    #% atomictype: AUTO| STRING | BOOLEAN | FLOAT | INTEGER ;
    def visitAtomictype(self, ctx: MT22Parser.atomictype):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.FLOAT():
            return FloatType()
    
    #@ Type


    # @ ID & LITERAL
    # just .getText() and set it type
    #% ID: (LETTER | UNDE) (LETTER | UNDE | DIGIT)*;
    def visitId(self, ctx: MT22Parser.ID):
        return Id(str(ctx.getText()))

    #% INT: (POSINT | ZERO){self.text = self.text.replace('_','')} ;
    def visitInt(self, ctx: MT22Parser.INT):
        return IntegerLit(int(str(ctx.getText())))

    #% BOOL: FALSE | TRUE;
    def visitBool(self, ctx: MT22Parser.BOOL):
        return BooleanLit(True if ctx.TRUE() else False)
    
    #% FLO:  ((POSINT | ZERO)+ DOT DECIMAL EXPONENT?
	#% | (POSINT | ZERO)+ DOT? EXPONENT
	#% | DOT DECIMAL EXPONENT){self.text = self.text.replace('_','')};
    def visitFlo(self, ctx: MT22Parser.FLO):
        return FloatLit(float(str(ctx.getText())))
    
    #% STR: (DB STR_CHAR*  DB) {self.text = self.text[1:-1]};
    def visitStr(self, ctx: MT22Parser.STR):
        return StringLit(str(ctx.getText()))

