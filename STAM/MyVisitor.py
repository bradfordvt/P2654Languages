import sys
from antlr4 import *
from dist.STAMLexer import STAMLexer
from dist.STAMParser import STAMParser
from dist.STAMVisitor import STAMVisitor


class MyVisitor(STAMVisitor):
    def __remove_underscore(self, s:str):
        return s.replace('_', '')
    
    def __remove_base_underscore(self, s:str):
        return s.translate({ ord(c): None for c in "_ \t" })
        
    # Visit a parse tree produced by STAMParser#concat_string.
    def visitConcat_string(self, ctx:STAMParser.Concat_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#parameter_ref.
    def visitParameter_ref(self, ctx:STAMParser.Parameter_refContext):
        ret = self.visitChildren(ctx)
        return ctx.getText()


    # Visit a parse tree produced by STAMParser#concat_number.
    def visitConcat_number(self, ctx:STAMParser.Concat_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#number.
    def visitNumber(self, ctx:STAMParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#unsized_number.
    def visitUnsized_number(self, ctx:STAMParser.Unsized_numberContext):
        if ctx.pos_int() is not None:
            return ctx.pos_int()
        elif ctx.UNSIZED_DEC_NUM() is not None:
            return int(self.__remove_base_underscore((ctx.UNSIZED_DEC_NUM().getText())))
        elif ctx.UNSIZED_HEX_NUM() is not None:
            return int(self.__remove_base_underscore((ctx.UNSIZED_HEX_NUM().getText())), 16)
        elif ctx.UNSIZED_BIN_NUM() is not None:
            return int(self.__remove_base_underscore((ctx.UNSIZED_BIN_NUM().getText())), 2)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#pos_int.
    def visitPos_int(self, ctx:STAMParser.Pos_intContext):
         return int(self.__remove_underscore(self.visit(ctx.POS_INT)))


    # Visit a parse tree produced by STAMParser#stam_source.
    def visitAttribute_def(self, ctx:STAMParser.Attribute_defContext):
        # ret = self.visitChildren(ctx)
        # print("ctx = ")
        # print(ctx.getText())
        # attribute_name = ctx.attribute_name().SCALAR_ID().getText()
        attribute_name = self.visit(ctx.attribute_name)
        # attribute_value = ctx.attribute_value().concat_string().STRING()
        attribute_value = self.visit(ctx.attribute_value)
        # print("attribute_name = ", attribute_name)
        # value = attribute_name + ":" + attribute_value[0].getText()
        value = attribute_name + ": [ " + ", ".join(map(str, attribute_value)) + " ]"
        return value


    # Visit a parse tree produced by STAMParser#size.
    def visitSize(self, ctx:STAMParser.SizeContext):
        if ctx.SCALAR_ID() is not None:
            return int(self.memory.get(ctx.SCALER_ID().getText()))
        else:
            return self.visit(ctx.pos_int)


    # Visit a parse tree produced by STAMParser#sized_dec_num.
    def visitSized_dec_num(self, ctx:STAMParser.Sized_dec_numContext):
        # return self.visitChildren(ctx)
        size = self.visit(ctx.size)
        value = ctx.UNSIZED_DEC_NUM()[2:]
        return intbv(val=value, _nbits=size)


    # Visit a parse tree produced by STAMParser#sized_bin_num.
    def visitSized_bin_num(self, ctx:STAMParser.Sized_bin_numContext):
        # return self.visitChildren(ctx)
        size = self.visit(ctx.size)
        value = ctx.UNSIZED_BIN_NUM()
        value[0] = '0'
        value[1] = 'b'
        return intbv(val=value, _nbits=size)


    # Visit a parse tree produced by STAMParser#sized_hex_num.
    def visitSized_hex_num(self, ctx:STAMParser.Sized_hex_numContext):
        # return self.visitChildren(ctx)
        size = self.visit(ctx.size)
        value = ctx.UNSIZED_HEX_NUM()
        value[0] = '0'
        value[1] = 'h'
        return intbv(val=value, _nrbits=size)


    # Visit a parse tree produced by STAMParser#sized_number.
    def visitSized_number(self, ctx:STAMParser.Sized_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#integer_expr.
    def visitInteger_expr(self, ctx:STAMParser.Integer_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#integer_expr_lvl1.
    def visitInteger_expr_lvl1(self, ctx:STAMParser.Integer_expr_lvl1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#integer_expr_lvl2.
    def visitInteger_expr_lvl2(self, ctx:STAMParser.Integer_expr_lvl2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#integer_expr_paren.
    def visitInteger_expr_paren(self, ctx:STAMParser.Integer_expr_parenContext):
        # return self.visitChildren(ctx)
        return self.visit(ctx.integer_expr)


    # Visit a parse tree produced by STAMParser#integer_expr_arg.
    def visitInteger_expr_arg(self, ctx:STAMParser.Integer_expr_argContext):
        # return self.visitChildren(ctx)
        if self.visit(ctx.pos_int):
            return ctx.pos_int()
        elif self.visit(ctx.parameter_ref):
            return ctx.parameter_ref()
        elif self.visit(ctx.integer_expr_paren):
            return ctx.integer_expr_paren()
        else:
            return None

