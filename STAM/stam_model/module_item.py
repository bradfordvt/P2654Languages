#!/usr/bin/env python
"""
    Container class for storing the contents of an Module_item statement in the STAM language.

    This file contains the contents of what was parsed from a STAM file for what was discovered in the
    Module_item statement.  The objects of this class will be contained in the module objects as individual
    instances of each of the module items defined.  This class also defines visitor methods for each type of
    formatted outputs supported by the parsing tool.

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
__date__ = "2023/04/17"
__deprecated__ = False
__email__ = "bradvt59@gmail.com"
__license__ = "Apache 2.0"
__maintainer__ = "Bradford G. Van Treuren"
__status__ = "Alpha/Experimental"
__version__ = "0.0.1"

from io import TextIOBase
from STAM.stam_model.clientinterface_def import ClientInterfaceDef
from STAM.stam_model.commandinterface_def import CommandInterfaceDef
from STAM.stam_model.commandlibrary_def import CommandLibraryDef
from STAM.stam_model.debuglibrary_def import DebugLibraryDef
from STAM.stam_model.hostinterface_def import HostInterfaceDef
from STAM.stam_model.indentation import Indentation
from STAM.stam_model.injectlibrary_def import InjectLibraryDef
from STAM.stam_model.instance_def import InstanceDef
from STAM.stam_model.transformlibrary_def import TransformLibraryDef


class ModuleItem:
    def __init__(self, ci: ClientInterfaceDef, hi: list, cmdi: CommandInterfaceDef, inst: list,
                 tli: TransformLibraryDef, ili: InjectLibraryDef, dli: DebugLibraryDef, cli: CommandLibraryDef,
                 par: list, attr: list):
        self.ci = ci
        if hi is not None:
            self.hi = hi[::-1]
        else:
            self.hi = None
        self.cmdi = cmdi
        if inst is not None:
            self.inst = inst[::-1]
        else:
            self.inst = None
        self.tli = tli
        self.ili = ili
        self.dli = dli
        self.cli = cli
        if par is not None:
            self.par = par[::-1]
        else:
            self.par = None
        if attr is not None:
            self.attr = attr[::-1]
        else:
            self.attr = None

    def get_ci(self) -> ClientInterfaceDef:
        return self.ci

    def get_hi(self) -> list:
        return self.hi

    def get_cmdi(self) -> CommandInterfaceDef:
        return self.cmdi

    def get_inst(self) -> InstanceDef:
        return self.inst

    def get_tli(self) -> TransformLibraryDef:
        return self.tli

    def get_ili(self) -> InjectLibraryDef:
        return self.ili

    def get_dli(self) -> DebugLibraryDef:
        return self.dli

    def get_cli(self) -> CommandLibraryDef:
        return self.cli

    def get_par(self) -> list:
        return self.par

    def get_attr(self) -> list:
        return self.attr

    def visit_xml(self, fp: TextIOBase):
        if self.ci:
            self.ci.visit_xml(fp)
        if self.hi:
            ind = Indentation.get_indentation()
            ind.incr()
            s = ' '*ind.get_indent()
            s += '<hostinterfaces>\n'
            fp.write(s)
            for a in self.hi:
                a.visit_xml(fp)
            s = ' '*ind.get_indent()
            s += '</hostinterfaces>\n'
            fp.write(s)
            ind.decr()
        if self.cmdi:
            self.cmdi.visit_xml(fp)
        if self.inst:
            ind = Indentation.get_indentation()
            ind.incr()
            s = ' '*ind.get_indent()
            s += '<instances>\n'
            fp.write(s)
            for a in self.inst:
                a.visit_xml(fp)
            s = ' '*ind.get_indent()
            s += '</instances>\n'
            fp.write(s)
            ind.decr()
        if self.tli:
            self.tli.visit_xml(fp)
        if self.ili:
            self.ili.visit_xml(fp)
        if self.dli:
            self.dli.visit_xml(fp)
        if self.cli:
            self.cli.visit_xml(fp)
        if self.par:
            ind = Indentation.get_indentation()
            ind.incr()
            s = ' '*ind.get_indent()
            s += '<parameters>\n'
            fp.write(s)
            for a in self.par:
                a.visit_xml(fp)
            s = ' '*ind.get_indent()
            s += '</parameters>\n'
            fp.write(s)
            ind.decr()

        if self.attr:
            ind = Indentation.get_indentation()
            ind.incr()
            s = ' '*ind.get_indent()
            s += '<attributes>\n'
            fp.write(s)
            for a in self.attr:
                a.visit_xml(fp)
            s = ' '*ind.get_indent()
            s += '</attributes>\n'
            fp.write(s)
            ind.decr()

    def visit_json(self, fp: TextIOBase, terminate: bool):
        if self.ci:
            self.ci.visit_json(fp, terminate)
        if self.hi:
            ind = Indentation.get_indentation()
            ind.incr()
            s = ' '*ind.get_indent()
            s += '"hostinterfaces": [\n'
            fp.write(s)
            n = len(self.hi) - 1
            for i, a in enumerate(self.hi):
                if i == n:
                    a.visit_json(fp, False)
                else:
                    a.visit_json(fp, True)
            s = ' '*ind.get_indent()
            if terminate:
                s += '],\n'
            else:
                s += ']\n'
            fp.write(s)
            ind.decr()
        if self.cmdi:
            self.cmdi.visit_json(fp, terminate)
        if self.inst:
            ind = Indentation.get_indentation()
            ind.incr()
            s = ' '*ind.get_indent()
            s += '"instances": [\n'
            fp.write(s)
            n = len(self.inst) - 1
            for i, a in enumerate(self.inst):
                if i == n:
                    a.visit_json(fp, False)
                else:
                    a.visit_json(fp, True)
            if terminate:
                s = ' ' * ind.get_indent()
                s += '],\n'
            else:
                s = ' ' * ind.get_indent()
                s += ']\n'
            fp.write(s)
            ind.decr()
        if self.tli:
            self.tli.visit_json(fp, terminate)
        if self.ili:
            self.ili.visit_json(fp, terminate)
        if self.dli:
            self.dli.visit_json(fp, terminate)
        if self.cli:
            self.cli.visit_json(fp, terminate)
        if self.par:
            ind = Indentation.get_indentation()
            ind.incr()
            s = ' '*ind.get_indent()
            s += '"parameters": [\n'
            fp.write(s)
            n = len(self.par) - 1
            for i, a in enumerate(self.par):
                if i == n:
                    a.visit_json(fp, False)
                else:
                    a.visit_json(fp, True)
            s = ' '*ind.get_indent()
            if terminate:
                s += '],\n'
            else:
                s += ']\n'
            fp.write(s)
            ind.decr()
        if self.attr:
            ind = Indentation.get_indentation()
            ind.incr()
            s = ' '*ind.get_indent()
            s += '"attributes": [\n'
            fp.write(s)
            n = len(self.attr) - 1
            for i, a in enumerate(self.attr):
                if i == n:
                    a.visit_json(fp, False)
                else:
                    a.visit_json(fp, True)
            s = ' '*ind.get_indent()
            if terminate:
                s += '],\n'
            else:
                s += ']\n'
            fp.write(s)
            ind.decr()
