import sys
from antlr4 import *
from myhdl import intbv

from STAM.dist.STAMLexer import STAMLexer
from STAM.dist.STAMParser import STAMParser
from STAM.dist.STAMVisitor import STAMVisitor


class MyVisitor(STAMVisitor):
    def __init__(self):
        self.symbols = {}

    def __remove_underscore(self, s:str):
        return s.replace('_', '')
    
    def __remove_base_underscore(self, s:str):
        return s.translate({ ord(c): None for c in "_ \t" })
        
    # Visit a parse tree produced by STAMParser#nameSpace_def.
    def visitNameSpace_def(self, ctx:STAMParser.NameSpace_defContext):
        if ctx.nameSpace_name():
            return self.visit(ctx.nameSpace_name())
        else:
            return "Undefined"


    # Visit a parse tree produced by STAMParser#nameSpace_name.
    def visitNameSpace_name(self, ctx:STAMParser.NameSpace_nameContext):
        return ctx.SCALAR_ID().getText()


    # Visit a parse tree produced by STAMParser#useNameSpace_def.
    def visitUseNameSpace_def(self, ctx:STAMParser.UseNameSpace_defContext):
        if ctx.nameSpace_name():
            return self.visit(ctx.nameSpace_name())
        else:
            return "Undefined"


    # Visit a parse tree produced by STAMParser#protocol_def.
    def visitProtocol_def(self, ctx:STAMParser.Protocol_defContext):
        if ctx.protocolFile_name():
            return self.visit(ctx.protocolFile_name())
        else:
            return None


    # Visit a parse tree produced by STAMParser#protocolFile_name.
    def visitProtocolFile_name(self, ctx:STAMParser.ProtocolFile_nameContext):
        return ctx.SCALAR_ID().getText()


    # Visit a parse tree produced by STAMParser#clientInterface_name.
    def visitClientInterface_name(self, ctx: STAMParser.ClientInterface_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#hostInterface_name.
    def visitHostInterface_name(self, ctx: STAMParser.HostInterface_nameContext) -> str:
        name = '*undefined*'
        index = None
        if ctx.SCALAR_ID():
            name = ctx.SCALAR_ID().getText()
            index = None
            return name + '[]'
        elif ctx.indexed_id():
            name, index = self.visit(ctx.indexed_id())
            return name + '[' + str(index) + ']'

    # Visit a parse tree produced by STAMParser#instance_def.
    def visitInstance_def(self, ctx: STAMParser.Instance_defContext) -> str:
        name = '*undefined*'
        namespace = None
        module_name = '*undefined*'
        items = []
        if ctx.instance_name():
            name = self.visit(ctx.instance_name())
        # if ctx.nameSpace_name():
        #     namespace = self.visit(ctx.nameSpace_name())
        # if ctx.module_name():
        #     module_name = self.visit(ctx.module_name())
        if ctx.instance_item():
            ctx_cis = ctx.instance_item()
            for ctx_ci in ctx_cis:
                items.append(self.visit(ctx_ci))
        return '{inst} <{items}>'.format(inst=name, items=items)

    # Visit a parse tree produced by STAMParser#instance_item.
    def visitInstance_item(self, ctx: STAMParser.Instance_itemContext) -> str:
        cic = None
        hic = None
        parover = None
        attr = None
        if ctx.clientInterface_connection():
            cic = self.visit(ctx.clientInterface_connection())
        # if ctx.hostInterface_connection_list():
        #     hic = self.visit(ctx.hostInterface_connection_list())
        # if ctx.parameter_override_list():
        #     parover = self.visit(ctx.parameter_override_list())
        # if ctx.attribute_list():
        #     attr = self.visit(ctx.attribute_list())
        ii = cic
        return ii

    # Visit a parse tree produced by STAMParser#instance_name.
    def visitInstance_name(self, ctx: STAMParser.Instance_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#clientInterface_connection.
    def visitClientInterface_connection(self, ctx: STAMParser.ClientInterface_connectionContext) -> str:
        name = '*undefined*'
        source = None
        if ctx.clientInterface_name():
            name = self.visit(ctx.clientInterface_name())
        if ctx.clientInterface_source():
            source = self.visit(ctx.clientInterface_source())
        cic = '{ci}={source}'.format(ci=name, source=source)
        return cic

    # Visit a parse tree produced by STAMParser#clientInterface_source.
    def visitClientInterface_source(self, ctx: STAMParser.ClientInterface_sourceContext):
        name = '*undefined*'
        instance_name = None
        if ctx.clientInterface_name():
            name = self.visit(ctx.clientInterface_name())
        if ctx.hostInterface_name():
            name = self.visit(ctx.hostInterface_name())
        if ctx.instance_name():
            instance_name = self.visit(ctx.instance_name())
        src = '{instance}.{name}'.format(instance=instance_name, name=name)
        return src

    # Visit a parse tree produced by STAMParser#parameter_override.
    def visitParameter_override(self, ctx:STAMParser.Parameter_overrideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#parameter_def.
    def visitParameter_def(self, ctx:STAMParser.Parameter_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#parameter_name.
    def visitParameter_name(self, ctx:STAMParser.Parameter_nameContext):
        return ctx.SCALAR_ID().getText()


    # Visit a parse tree produced by STAMParser#parameter_value.
    def visitParameter_value(self, ctx:STAMParser.Parameter_valueContext):
        if ctx.concat_string():
            attribute_value_list = self.visit(ctx.concat_string())
        elif ctx.concat_number():
            attribute_value_list = self.visit(ctx.concat_number())
        value = "".join(map(str, [x for x in attribute_value_list]))
        return value


    # Visit a parse tree produced by STAMParser#concat_string.
    def visitConcat_string(self, ctx:STAMParser.Concat_stringContext):
        # self.visitChildren(ctx)
        slist = []
        refs = ctx.string_or_parameter_ref()
        for ref in refs:
            slist.append(self.visit(ref))
        return slist


    # Visit a parse tree produced by STAMParser#string_or_parameter_ref.
    def visitString_or_parameter_ref(self, ctx:STAMParser.String_or_parameter_refContext):
        if ctx.STRING():
            return ctx.STRING().getText()
        else:
            return self.visit(ctx.parameter_ref())



    # Visit a parse tree produced by STAMParser#parameter_ref.
    def visitParameter_ref(self, ctx:STAMParser.Parameter_refContext):
        id = ctx.SCALAR_ID().getText()
        val = self.symbols.get(id)
        if val is None:
            return '$' + id
        else:
            return val


    # Visit a parse tree produced by STAMParser#concat_number.
    def visitConcat_number(self, ctx:STAMParser.Concat_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#number.
    def visitNumber(self, ctx:STAMParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#unsized_number.
    def visitUnsized_number(self, ctx:STAMParser.Unsized_numberContext):
        if ctx.pos_int() is not None:
            return self.visit(ctx.pos_int())
        elif ctx.UNSIZED_DEC_NUM() is not None:
            return int(self.__remove_base_underscore((ctx.UNSIZED_DEC_NUM().getText())))
        elif ctx.UNSIZED_HEX_NUM() is not None:
            return int(self.__remove_base_underscore((ctx.UNSIZED_HEX_NUM().getText())), 16)
        elif ctx.UNSIZED_BIN_NUM() is not None:
            return int(self.__remove_base_underscore((ctx.UNSIZED_BIN_NUM().getText())), 2)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#pos_int.
    def visitPos_int(self, ctx:STAMParser.Pos_intContext):
        if ctx.POS_INT():
            return int(self.__remove_underscore(ctx.POS_INT().getText()))
        elif ctx.getToken(28, 0):
            return int(ctx.getToken(28, 0).getText())
        elif ctx.getToken(27, 0):
            return int(ctx.getToken(27, 0).getText())
        else:
            return None


    # Visit a parse tree produced by STAMParser#stam_source.
    def visitAttribute_def(self, ctx:STAMParser.Attribute_defContext):
        attribute_name = self.visit(ctx.attribute_name())
        attribute_value = self.visit(ctx.attribute_value())
        value = attribute_name + ": [ " + ", ".join(map(str, [x for x in attribute_value])) + " ]"
        return value


    # Visit a parse tree produced by STAMParser#attribute_name.
    def visitAttribute_name(self, ctx:STAMParser.Attribute_nameContext):
        return ctx.SCALAR_ID().getText()


    # Visit a parse tree produced by STAMParser#attribute_value.
    def visitAttribute_value(self, ctx:STAMParser.Attribute_valueContext):
        if ctx.concat_string():
            return self.visit(ctx.concat_string())
        elif ctx.concat_number():
            return self.visit(ctx.concat_number())
        else:
            return None


    # Visit a parse tree produced by STAMParser#size.
    def visitSize(self, ctx:STAMParser.SizeContext):
        if ctx.SCALAR_ID() is not None:
            return int(self.symbols.get(ctx.SCALER_ID().getText()))
        else:
            return self.visit(ctx.pos_int)


    # Visit a parse tree produced by STAMParser#sized_dec_num.
    def visitSized_dec_num(self, ctx:STAMParser.Sized_dec_numContext):
        size = self.visit(ctx.size())
        value = ctx.UNSIZED_DEC_NUM()[2:]
        return intbv(val=value, _nbits=size)


    # Visit a parse tree produced by STAMParser#sized_bin_num.
    def visitSized_bin_num(self, ctx:STAMParser.Sized_bin_numContext):
        size = self.visit(ctx.size())
        value = ctx.UNSIZED_BIN_NUM()
        value[0] = '0'
        value[1] = 'b'
        return intbv(val=value, _nbits=size)


    # Visit a parse tree produced by STAMParser#sized_hex_num.
    def visitSized_hex_num(self, ctx:STAMParser.Sized_hex_numContext):
        size = self.visit(ctx.size())
        value = ctx.UNSIZED_HEX_NUM()
        value[0] = '0'
        value[1] = 'h'
        return intbv(val=value, _nrbits=size)


    # Visit a parse tree produced by STAMParser#sized_number.
    def visitSized_number(self, ctx:STAMParser.Sized_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STAMParser#integer_expr.
    def visitInteger_expr(self, ctx: STAMParser.Integer_exprContext) -> int:
        if ctx.pos_int():
            return self.visit(ctx.pos_int())
        if ctx.parameter_ref():
            return self.visit(ctx.parameter_ref())
        if ctx.expr:
            return self.visit(ctx.expr)
        lt = self.visit(ctx.left)
        rt = self.visit(ctx.right)

        op = ctx.op.text
        operation = {
            '+': lambda: lt + rt,
            '-': lambda: lt - rt,
            '*': lambda: lt * rt,
            '/': lambda: lt / rt,
            '%': lambda: lt % rt,
        }
        return operation.get(op, lambda: None)()
