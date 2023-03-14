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
        # if ctx.vartype():
        #     return (ctx.ID().getText(), ctx.expression())
        # IdNExp = (ctx.ID().getText(), ctx.expression())
        # return IdNExp.append(self.visit(ctx.variabledeclassign()))
        return [("a", IntegerLit(1)), ("b", IntegerLit(2)), ("c", IntegerLit(3))]
    
    
    
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
    
    #@ 4. STATEMENT

    #@ 5. EXPRESSION
    #@ 5.1. Binary expression
    def visitExpression(self, ctx: MT22Parser.expression):
        return IntegerLit(1)
    # ! not done

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

