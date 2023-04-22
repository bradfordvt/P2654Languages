#!/usr/bin/env python
"""
   Visitor class for transforming the contents of a STAM language file into a different formatted output.

   Visitor class for transforming the contents of a STAM language file into a different formatted output.
   The objects of this class will delegate to visit functions for the appropriate format output by creating
   objects for the different statements within a STAM file. Each object is responsible for creating its portion of the
   formatted output selected.

   Copyright 2023 VT Enterprises Consulting Services

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

__authors__ = ["Bradford G. Van Treuren"]
__contact__ = "bradvt59@gmail.com"
__copyright__ = "Copyright 2023, VT Enterprises Consulting Services"
__credits__ = ["Bradford G. Van Treuren"]
__date__ = "2023/04/13"
__deprecated__ = False
__email__ = "bradvt59@gmail.com"
__license__ = "Apache 2.0"
__maintainer__ = "Bradford G. Van Treuren"
__status__ = "Alpha/Experimental"
__version__ = "0.0.1"

from typing import Any, TextIO
from myhdl import intbv
from STAM.ParserException import ParserException
from STAM.dist.STAMParser import STAMParser
from STAM.dist.STAMVisitor import STAMVisitor
from STAM.stam_model.attribute import Attribute
from STAM.stam_model.clientinterface_connection import ClientInterfaceConnection
from STAM.stam_model.clientinterface_def import ClientInterfaceDef
from STAM.stam_model.clientinterface_source import ClientInterfaceSource
from STAM.stam_model.commandinterface_def import CommandInterfaceDef
from STAM.stam_model.commandlibrary_def import CommandLibraryDef
from STAM.stam_model.debuglibrary_def import DebugLibraryDef
from STAM.stam_model.hostinterface_connection import HostInterfaceConnection
from STAM.stam_model.hostinterface_def import HostInterfaceDef
from STAM.stam_model.hostinterface_name import HostInterfaceName
from STAM.stam_model.hosttinterface_source import HostInterfaceSource
from STAM.stam_model.injectlibrary_def import InjectLibraryDef
from STAM.stam_model.instance_def import InstanceDef
from STAM.stam_model.instance_item import InstanceItem
from STAM.stam_model.module_def import ModuleDef
from STAM.stam_model.module_item import ModuleItem
from STAM.stam_model.namespace_def import NameSpaceDef
from STAM.stam_model.parameter import Parameter
from STAM.stam_model.parameteroverride import ParameterOverride
from STAM.stam_model.rvfprotocol import RVFProtocol
from STAM.stam_model.stamsource_def import STAMSource
from STAM.stam_model.transformlibrary_def import TransformLibraryDef
from STAM.stam_model.usenamespace_def import UseNameSpaceDef


class FormattingVisitor(STAMVisitor):
    def __init__(self, symbols=None):
        if symbols is None:
            symbols = {}
        self.symbols = symbols
        self.fp = None

    @staticmethod
    def __remove_underscore(s: str):
        return s.replace('_', '')

    @staticmethod
    def __remove_base_underscore(s: str):
        return s.translate({ord(c): None for c in "_ \t"})

    @staticmethod
    def __expand_values(values: list) -> Any:
        if isinstance(values[0], str):
            s = ''.join(x for x in values)
            return s
        if isinstance(values[0], intbv):
            s = ''.join(str(x) for x in values)
            return intbv(int(s))

    def set_file_pointer(self, fp: TextIO) -> None:
        self.fp = fp

    # Visit a parse tree produced by STAMParser#stam_source.
    def visitStam_source(self, ctx: STAMParser.Stam_sourceContext) -> STAMSource:
        items = []
        if ctx.stamSource_items():
            ctxs = ctx.stamSource_items()
            for i in ctxs:
                items.append(self.visit(i))
        return STAMSource(items)

    # Visit a parse tree produced by STAMParser#stamSource_items.
    def visitStamSource_items(self, ctx: STAMParser.StamSource_itemsContext) -> Any:
        if ctx.nameSpace_def():
            return self.visit(ctx.nameSpace_def())
        if ctx.useNameSpace_def():
            return self.visit(ctx.useNameSpace_def())
        if ctx.module_def():
            return self.visit(ctx.module_def())

    # Visit a parse tree produced by STAMParser#nameSpace_def.
    def visitNameSpace_def(self, ctx: STAMParser.NameSpace_defContext) -> NameSpaceDef:
        name = '*undefined*'
        if ctx.nameSpace_name():
            name = self.visit(ctx.nameSpace_name())
        return NameSpaceDef(name)

    # Visit a parse tree produced by STAMParser#nameSpace_name.
    def visitNameSpace_name(self, ctx: STAMParser.NameSpace_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#useNameSpace_def.
    def visitUseNameSpace_def(self, ctx: STAMParser.UseNameSpace_defContext) -> UseNameSpaceDef:
        name = '*undefined*'
        if ctx.nameSpace_name():
            name = self.visit(ctx.nameSpace_name())
        return UseNameSpaceDef(name)

    # Visit a parse tree produced by STAMParser#module_def.
    def visitModule_def(self, ctx: STAMParser.Module_defContext) -> ModuleDef:
        name = '*undefined*'
        items = []
        if ctx.module_name():
            name = self.visit(ctx.module_name())
        if ctx.module_item():
            ctx_cis = ctx.module_item()
            for ctx_ci in ctx_cis:
                items.append(self.visit(ctx_ci))
        return ModuleDef(name, items)

    # Visit a parse tree produced by STAMParser#module_name.
    def visitModule_name(self, ctx: STAMParser.Module_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#module_item.
    def visitModule_item(self, ctx: STAMParser.Module_itemContext) -> ModuleItem:
        ci = None
        hi = None
        cmdi = None
        inst = None
        tli = None
        ili = None
        dli = None
        cli = None
        par = None
        attr = None
        if ctx.clientInterface_def():
            ci = self.visit(ctx.clientInterface_def())
        if ctx.hostInterface_list():
            hi = self.visit(ctx.hostInterface_list())
        if ctx.commandInterface_def():
            cmdi = self.visit(ctx.commandInterface_def())
        if ctx.instance_list():
            inst = self.visit(ctx.instance_list())
        if ctx.transformLibrary_def():
            tli = self.visit(ctx.transformLibrary_def())
        if ctx.injectLibrary_def():
            ili = self.visit(ctx.injectLibrary_def())
        if ctx.debugLibrary_def():
            dli = self.visit(ctx.debugLibrary_def())
        if ctx.commandLibrary_def():
            cli = self.visit(ctx.commandLibrary_def())
        if ctx.parameter_list():
            par = self.visit(ctx.parameter_list())
        if ctx.attribute_list():
            attr = self.visit(ctx.attribute_list())
        mi = ModuleItem(ci, hi, cmdi, inst, tli, ili, dli, cli, par, attr)
        return mi

    # Visit a parse tree produced by STAMParser#clientInterface_def.
    def visitClientInterface_def(self, ctx: STAMParser.ClientInterface_defContext) -> ClientInterfaceDef:
        name = '*undefined*'
        items = []
        if ctx.clientInterface_name():
            name = self.visit(ctx.clientInterface_name())
        if ctx.clientInterface_item():
            ctx_cis = ctx.clientInterface_item()
            for ctx_ci in ctx_cis:
                items.append(self.visit(ctx_ci))
        return ClientInterfaceDef(name, items)

    # Visit a parse tree produced by STAMParser#clientInterface_name.
    def visitClientInterface_name(self, ctx: STAMParser.ClientInterface_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#clientInterface_item.
    def visitClientInterface_item(self, ctx: STAMParser.ClientInterface_itemContext) -> RVFProtocol:
        if ctx.protocol_def():
            return self.visit(ctx.protocol_def())
        else:
            return RVFProtocol('*undefined*')

    # Visit a parse tree produced by STAMParser#protocol_def.
    def visitProtocol_def(self, ctx: STAMParser.Protocol_defContext) -> RVFProtocol:
        if ctx.protocolFile_name():
            pfn = self.visit(ctx.protocolFile_name())
            return RVFProtocol(pfn)
        else:
            return RVFProtocol('*undefined*')

    # Visit a parse tree produced by STAMParser#protocolFile_name.
    def visitProtocolFile_name(self, ctx: STAMParser.ProtocolFile_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#indexed_id.
    def visitIndexed_id(self, ctx: STAMParser.Indexed_idContext) -> tuple:
        name = '*undefined*'
        index = None
        if ctx.SCALAR_ID():
            name = ctx.SCALAR_ID().getText()
        if ctx.index():
            index = self.visit(ctx.index())
        return name, index

    # Visit a parse tree produced by STAMParser#index.
    def visitIndex(self, ctx: STAMParser.IndexContext) -> int:
        return self.visit(ctx.integer_expr())

    # Visit a parse tree produced by STAMParser#hostInterface_list.
    def visitHostInterface_list(self, ctx: STAMParser.HostInterface_listContext) -> list:
        clist = []
        if ctx.hostInterface_list():
            clist = self.visit(ctx.hostInterface_list())
        if ctx.hostInterface_def():
            clist.append(self.visit(ctx.hostInterface_def()))
        return clist

    # Visit a parse tree produced by STAMParser#hostInterface_def.
    def visitHostInterface_def(self, ctx: STAMParser.HostInterface_defContext) -> HostInterfaceDef:
        name = None
        items = []
        if ctx.hostInterface_name():
            name = self.visit(ctx.hostInterface_name())
        if ctx.hostInterface_item():
            ctx_his = ctx.hostInterface_item()
            for ctx_hi in ctx_his:
                items.append(self.visit(ctx_hi))
        hid = HostInterfaceDef(name, items)
        return hid

    # Visit a parse tree produced by STAMParser#hostInterface_name.
    def visitHostInterface_name(self, ctx: STAMParser.HostInterface_nameContext) -> HostInterfaceName:
        name = '*undefined*'
        index = None
        if ctx.SCALAR_ID():
            name = ctx.SCALAR_ID().getText()
            index = None
        elif ctx.indexed_id():
            name, index = self.visit(ctx.indexed_id())
        return HostInterfaceName(name, index)

    # Visit a parse tree produced by STAMParser#hostInterface_item.
    def visitHostInterface_item(self, ctx: STAMParser.HostInterface_itemContext) -> RVFProtocol:
        if ctx.protocol_def():
            return self.visit(ctx.protocol_def())
        else:
            return RVFProtocol('*undefined*')

    # Visit a parse tree produced by STAMParser#instance_list.
    def visitInstance_list(self, ctx: STAMParser.Instance_listContext) -> list:
        clist = []
        if ctx.instance_list():
            clist = self.visit(ctx.instance_list())
        if ctx.instance_def():
            clist.append(self.visit(ctx.instance_def()))
        return clist

    # Visit a parse tree produced by STAMParser#instance_def.
    def visitInstance_def(self, ctx: STAMParser.Instance_defContext) -> InstanceDef:
        name = '*undefined*'
        namespace = None
        module_name = '*undefined*'
        items = []
        if ctx.instance_name():
            name = self.visit(ctx.instance_name())
        if ctx.nameSpace_name():
            namespace = self.visit(ctx.nameSpace_name())
        if ctx.module_name():
            module_name = self.visit(ctx.module_name())
        if ctx.instance_item():
            ctx_cis = ctx.instance_item()
            for ctx_ci in ctx_cis:
                items.append(self.visit(ctx_ci))
        return InstanceDef(name, namespace, module_name, items)

    # Visit a parse tree produced by STAMParser#instance_item.
    def visitInstance_item(self, ctx: STAMParser.Instance_itemContext) -> InstanceItem:
        cic = None
        hic = None
        parover = None
        attr = None
        if ctx.clientInterface_connection():
            cic = self.visit(ctx.clientInterface_connection())
        if ctx.hostInterface_connection_list():
            hic = self.visit(ctx.hostInterface_connection_list())
        if ctx.parameter_override_list():
            parover = self.visit(ctx.parameter_override_list())
        if ctx.attribute_list():
            attr = self.visit(ctx.attribute_list())
        ii = InstanceItem(cic, hic, parover, attr)
        return ii

    # Visit a parse tree produced by STAMParser#instance_name.
    def visitInstance_name(self, ctx: STAMParser.Instance_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#commandInterface_def.
    def visitCommandInterface_def(self, ctx: STAMParser.CommandInterface_defContext) -> CommandInterfaceDef:
        name = '*undefined*'
        items = []
        if ctx.commandInterface_name():
            name = self.visit(ctx.commandInterface_name())
        if ctx.commandInterface_item():
            ctx_cis = ctx.commandInterface_item()
            for ctx_ci in ctx_cis:
                items.append(self.visit(ctx_ci))
        return CommandInterfaceDef(name, items)

    # Visit a parse tree produced by STAMParser#commandInterface_name.
    def visitCommandInterface_name(self, ctx: STAMParser.CommandInterface_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#commandInterface_item.
    def visitCommandInterface_item(self, ctx: STAMParser.CommandInterface_itemContext) -> RVFProtocol:
        if ctx.protocol_def():
            return self.visit(ctx.protocol_def())
        else:
            return RVFProtocol('*undefined*')

    # Visit a parse tree produced by STAMParser#transformLibrary_def.
    def visitTransformLibrary_def(self, ctx: STAMParser.TransformLibrary_defContext) -> TransformLibraryDef:
        name = '*undefined*'
        items = []
        if ctx.transformLibrary_name():
            name = self.visit(ctx.transformLibrary_name())
        if ctx.transformLibrary_item():
            ctx_cis = ctx.transformLibrary_item()
            for ctx_ci in ctx_cis:
                items.append(self.visit(ctx_ci))
        return TransformLibraryDef(name, items)

    # Visit a parse tree produced by STAMParser#transformLibrary_name.
    def visitTransformLibrary_name(self, ctx: STAMParser.TransformLibrary_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#transformLibrary_item.
    def visitTransformLibrary_item(self, ctx: STAMParser.TransformLibrary_itemContext) -> Attribute:
        if ctx.attribute_list():
            return self.visit(ctx.attribute_list())

    # Visit a parse tree produced by STAMParser#injectLibrary_def.
    def visitInjectLibrary_def(self, ctx: STAMParser.InjectLibrary_defContext) -> InjectLibraryDef:
        name = '*undefined*'
        items = []
        if ctx.injectLibrary_name():
            name = self.visit(ctx.injectLibrary_name())
        if ctx.injectLibrary_item():
            ctx_cis = ctx.injectLibrary_item()
            for ctx_ci in ctx_cis:
                items.append(self.visit(ctx_ci))
        return InjectLibraryDef(name, items)

    # Visit a parse tree produced by STAMParser#injectLibrary_name.
    def visitInjectLibrary_name(self, ctx: STAMParser.InjectLibrary_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#injectLibrary_item.
    def visitInjectLibrary_item(self, ctx: STAMParser.InjectLibrary_itemContext) -> Attribute:
        if ctx.attribute_list():
            return self.visit(ctx.attribute_list())

    # Visit a parse tree produced by STAMParser#commandLibrary_def.
    def visitCommandLibrary_def(self, ctx: STAMParser.CommandLibrary_defContext) -> CommandLibraryDef:
        name = '*undefined*'
        items = []
        if ctx.commandLibrary_name():
            name = self.visit(ctx.commandLibrary_name())
        if ctx.commandLibrary_item():
            ctx_cis = ctx.commandLibrary_item()
            for ctx_ci in ctx_cis:
                items.append(self.visit(ctx_ci))
        return CommandLibraryDef(name, items)

    # Visit a parse tree produced by STAMParser#commandLibrary_name.
    def visitCommandLibrary_name(self, ctx: STAMParser.CommandLibrary_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#commandLibrary_item.
    def visitCommandLibrary_item(self, ctx: STAMParser.CommandLibrary_itemContext) -> Attribute:
        if ctx.attribute_list():
            return self.visit(ctx.attribute_list())

    # Visit a parse tree produced by STAMParser#debugLibrary_def.
    def visitDebugLibrary_def(self, ctx: STAMParser.DebugLibrary_defContext) -> DebugLibraryDef:
        name = '*undefined*'
        items = []
        if ctx.debugLibrary_name():
            name = self.visit(ctx.debugLibrary_name())
        if ctx.debugLibrary_item():
            ctx_cis = ctx.debugLibrary_item()
            for ctx_ci in ctx_cis:
                items.append(self.visit(ctx_ci))
        return DebugLibraryDef(name, items)

    # Visit a parse tree produced by STAMParser#debugLibrary_name.
    def visitDebugLibrary_name(self, ctx: STAMParser.DebugLibrary_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#debugLibrary_item.
    def visitDebugLibrary_item(self, ctx: STAMParser.DebugLibrary_itemContext) -> Attribute:
        if ctx.attribute_list():
            return self.visit(ctx.attribute_list())

    # Visit a parse tree produced by STAMParser#clientInterface_connection.
    def visitClientInterface_connection(self, ctx: STAMParser.ClientInterface_connectionContext) ->\
            ClientInterfaceConnection:
        name = '*undefined*'
        source = ClientInterfaceSource()
        if ctx.clientInterface_name():
            name = self.visit(ctx.clientInterface_name())
        if ctx.clientInterface_source():
            source = self.visit(ctx.clientInterface_source())
        cic = ClientInterfaceConnection(name, source)
        return cic

    # Visit a parse tree produced by STAMParser#clientInterface_source.
    def visitClientInterface_source(self, ctx: STAMParser.ClientInterface_sourceContext) -> ClientInterfaceSource:
        name = '*undefined*'
        instance_name = None
        if ctx.clientInterface_name():
            name = self.visit(ctx.clientInterface_name())
        if ctx.hostInterface_name():
            name = self.visit(ctx.hostInterface_name())
        if ctx.instance_name():
            instance_name = self.visit(ctx.instance_name())
        src = ClientInterfaceSource(instance_name, name)
        return src

    # Visit a parse tree produced by STAMParser#hostInterface_connection_list.
    def visitHostInterface_connection_list(self, ctx: STAMParser.HostInterface_connection_listContext) -> list:
        clist = []
        if ctx.hostInterface_connection_list():
            clist = self.visit(ctx.hostInterface_connection_list())
        if ctx.hostInterface_connection():
            clist.append(self.visit(ctx.hostInterface_connection()))
        return clist

    # Visit a parse tree produced by STAMParser#hostInterface_connection.
    def visitHostInterface_connection(self, ctx: STAMParser.HostInterface_connectionContext) -> HostInterfaceConnection:
        name = '*undefined*'
        source = HostInterfaceSource()
        if ctx.hostInterface_name():
            name = self.visit(ctx.hostInterface_name())
        if ctx.hostInterface_source():
            source = self.visit(ctx.hostInterface_source())
        hic = HostInterfaceConnection(name, source)
        return hic

    # Visit a parse tree produced by STAMParser#hostInterface_source.
    def visitHostInterface_source(self, ctx: STAMParser.HostInterface_sourceContext) -> HostInterfaceSource:
        name = '*undefined*'
        instance_name = None
        if ctx.hostInterface_name():
            name = self.visit(ctx.hostInterface_name())
        if ctx.clientInterface_name():
            name = self.visit(ctx.clientInterface_name())
        if ctx.instance_name():
            instance_name = self.visit(ctx.instance_name())
        src = HostInterfaceSource(instance_name, name)
        return src

    # Visit a parse tree produced by STAMParser#parameter_override_list.
    def visitParameter_override_list(self, ctx: STAMParser.Parameter_override_listContext) -> list:
        plist = []
        if ctx.parameter_override_list():
            plist = self.visit(ctx.parameter_override_list())
        if ctx.parameter_override():
            plist.append(self.visit(ctx.parameter_override()))
        return plist

    # Visit a parse tree produced by STAMParser#parameter_override.
    def visitParameter_override(self, ctx: STAMParser.Parameter_overrideContext) -> ParameterOverride:
        pd = self.visit(ctx.parameter_def())
        po = ParameterOverride(pd)
        return po

    # Visit a parse tree produced by STAMParser#parameter_list.
    def visitParameter_list(self, ctx: STAMParser.Parameter_listContext) -> list:
        plist = []
        if ctx.parameter_list():
            plist = self.visit(ctx.parameter_list())
        if ctx.parameter_def():
            plist.append(self.visit(ctx.parameter_def()))
        return plist

    # Visit a parse tree produced by STAMParser#parameter_def.
    def visitParameter_def(self, ctx: STAMParser.Parameter_defContext) -> Parameter:
        name = "*undefined*"
        values = []
        if ctx.parameter_name():
            name = self.visit(ctx.parameter_name())
        if ctx.parameter_value():
            values = self.visit(ctx.parameter_value())
        if name in self.symbols.keys():
            raise ParserException("Parameter " + name + " is already in the symbol table.")
        self.symbols[name] = FormattingVisitor.__expand_values(values)
        return Parameter(name, values)

    # Visit a parse tree produced by STAMParser#parameter_name.
    def visitParameter_name(self, ctx: STAMParser.Parameter_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#parameter_value.
    def visitParameter_value(self, ctx: STAMParser.Parameter_valueContext) -> list:
        parameter_value_list = []
        if ctx.concat_string():
            parameter_value_list = self.visit(ctx.concat_string())
        elif ctx.concat_number():
            parameter_value_list = self.visit(ctx.concat_number())
        return parameter_value_list

    # Visit a parse tree produced by STAMParser#concat_string.
    def visitConcat_string(self, ctx: STAMParser.Concat_stringContext) -> list:
        sl = []
        refs = ctx.string_or_parameter_ref()
        for ref in refs:
            sl.append(self.visit(ref))
        return sl

    # Visit a parse tree produced by STAMParser#string_or_parameter_ref.
    def visitString_or_parameter_ref(self, ctx: STAMParser.String_or_parameter_refContext) -> str:
        if ctx.STRING():
            return ctx.STRING().getText()
        else:
            return self.visit(ctx.parameter_ref())

    # Visit a parse tree produced by STAMParser#parameter_ref.
    def visitParameter_ref(self, ctx: STAMParser.Parameter_refContext) -> str:
        ref = ctx.SCALAR_ID().getText()
        val = self.symbols.get(ref)
        if val is None:
            return '$' + ref
        else:
            return val

    # Visit a parse tree produced by STAMParser#concat_number.
    def visitConcat_number(self, ctx: STAMParser.Concat_numberContext) -> list:
        sl = []
        refs = ctx.compliment_number()
        for ref in refs:
            sl.append(self.visit(ref))
        return sl

    # Visit a parse tree produced by STAMParser#compliment_number.
    def visitCompliment_number(self, ctx: STAMParser.Compliment_numberContext) -> int:
        number = self.visit(ctx.number())
        if ctx.op:
            number = ~number
        return number

    # Visit a parse tree produced by STAMParser#number.
    def visitNumber(self, ctx: STAMParser.NumberContext) -> intbv:
        if ctx.integer_expr():
            return self.visit(ctx.integer_expr())
        if ctx.unsized_number():
            return self.visit(ctx.unsized_number())
        if ctx.sized_number():
            return self.visit(ctx.sized_number())

    # Visit a parse tree produced by STAMParser#unsized_number.
    def visitUnsized_number(self, ctx: STAMParser.Unsized_numberContext) -> intbv:
        if ctx.pos_int():
            return self.visit(ctx.pos_int())
        elif ctx.UNSIZED_DEC_NUM():
            return intbv(int(FormattingVisitor.__remove_base_underscore((ctx.UNSIZED_DEC_NUM().getText()))[2:]))
        elif ctx.UNSIZED_HEX_NUM():
            return intbv(int(FormattingVisitor.__remove_base_underscore((ctx.UNSIZED_HEX_NUM().getText()))[2:], 16))
        elif ctx.UNSIZED_BIN_NUM():
            return intbv(int(FormattingVisitor.__remove_base_underscore((ctx.UNSIZED_BIN_NUM().getText()))[2:], 2))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by STAMParser#pos_int.
    def visitPos_int(self, ctx: STAMParser.Pos_intContext) -> intbv:
        if ctx.POS_INT():
            return intbv(int(FormattingVisitor.__remove_underscore(ctx.POS_INT().getText())))
        elif ctx.getToken(28, 0):  # '1'
            return intbv(ctx.getToken(28, 0).getText())
        elif ctx.getToken(27, 0):  # '0'
            return intbv(ctx.getToken(27, 0).getText())

    # Visit a parse tree produced by STAMParser#attribute_list.
    def visitAttribute_list(self, ctx: STAMParser.Attribute_listContext) -> list:
        alist = []
        if ctx.attribute_list():
            alist = self.visit(ctx.attribute_list())
        if ctx.attribute_def():
            alist.append(self.visit(ctx.attribute_def()))
        return alist

    # Visit a parse tree produced by STAMParser#attribute_def.
    def visitAttribute_def(self, ctx: STAMParser.Attribute_defContext) -> Attribute:
        attribute_name = self.visit(ctx.attribute_name())
        attribute_values = self.visit(ctx.attribute_value())
        return Attribute(attribute_name, attribute_values)

    # Visit a parse tree produced by STAMParser#attribute_name.
    def visitAttribute_name(self, ctx: STAMParser.Attribute_nameContext) -> str:
        return ctx.SCALAR_ID().getText()

    # Visit a parse tree produced by STAMParser#attribute_value.
    def visitAttribute_value(self, ctx: STAMParser.Attribute_valueContext) -> list:
        if ctx.concat_string():
            return self.visit(ctx.concat_string())
        elif ctx.concat_number():
            return self.visit(ctx.concat_number())
        else:
            return []

    # Visit a parse tree produced by STAMParser#size.
    def visitSize(self, ctx: STAMParser.SizeContext) -> intbv:
        if ctx.SCALAR_ID():
            p = self.visit(ctx.SCALAR_ID())
            # i = intbv(0)
            try:
                i = intbv(self.symbols.get(p, None))
            except ValueError:
                raise ParserException("Parameter $" + p + " is not an integer value for size.")
            return i
        if ctx.pos_int():
            return self.visit(ctx.pos_int())

    # Visit a parse tree produced by STAMParser#sized_dec_num.
    def visitSized_dec_num(self, ctx: STAMParser.Sized_dec_numContext) -> intbv:
        sz = self.visit(ctx.size())
        udn = ctx.UNSIZED_DEC_NUM().getText()
        val = FormattingVisitor.__remove_base_underscore(udn)
        i = intbv(int(val[2:], 10), _nrbits=sz)
        return i

    # Visit a parse tree produced by STAMParser#sized_bin_num.
    def visitSized_bin_num(self, ctx: STAMParser.Sized_bin_numContext) -> intbv:
        sz = self.visit(ctx.size())
        udn = ctx.UNSIZED_BIN_NUM().getText()
        val = FormattingVisitor.__remove_base_underscore(udn)
        i = intbv(val[2:], _nrbits=sz)  # intbv accepts binary strings only
        return i

    # Visit a parse tree produced by STAMParser#sized_hex_num.
    def visitSized_hex_num(self, ctx: STAMParser.Sized_hex_numContext) -> intbv:
        sz = self.visit(ctx.size())
        udn = ctx.UNSIZED_HEX_NUM().getText()
        val = FormattingVisitor.__remove_base_underscore(udn)
        i = intbv(int(val[2:], 16), _nrbits=sz)
        return i

    # Visit a parse tree produced by STAMParser#sized_number.
    def visitSized_number(self, ctx: STAMParser.Sized_numberContext) -> intbv:
        if ctx.sized_dec_num():
            return self.visit(ctx.sized_dec_num())
        if ctx.sized_bin_num():
            return self.visit(ctx.sized_bin_num())
        if ctx.sized_hex_num():
            return self.visit(ctx.sized_hex_num())

    # Visit a parse tree produced by STAMParser#integer_expr.
    def visitInteger_expr(self, ctx: STAMParser.Integer_exprContext) -> intbv:
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


del STAMParser
