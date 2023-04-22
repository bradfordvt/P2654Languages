#!/usr/bin/env python
"""
    Python Protocol type class so multiple types of objects may be contained in an InstanceDef object.

    Python Protocol type class so multiple types of objects may be contained in an InstanceDef object.

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
__date__ = "2023/04/14"
__deprecated__ = False
__email__ = "bradvt59@gmail.com"
__license__ = "Apache 2.0"
__maintainer__ = "Bradford G. Van Treuren"
__status__ = "Alpha/Experimental"
__version__ = "0.0.1"

from io import TextIOBase

from STAM.stam_model.clientinterface_connection import ClientInterfaceConnection
from STAM.stam_model.hostinterface_connection import HostInterfaceConnection
from STAM.stam_model.indentation import Indentation


class InstanceItem:
    def __init__(self, cic: ClientInterfaceConnection, hic: list,
                 parover: list, attr: list):
        self.cic = cic
        if hic is not None:
            self.hic = hic[::-1]  # ANTLR4 parser processes last terminals first in DFS
        else:
            self.hic = None
        if parover is not None:
            self.parover = parover[::-1]
        else:
            self.parover = None
        if attr is not None:
            self.attr = attr[::-1]
        else:
            self.attr = None

    def get_cic(self) -> ClientInterfaceConnection:
        return self.cic

    def get_hic(self) -> list:
        return self.hic

    def get_parover(self) -> list:
        return self.parover

    def get_attr(self) -> list:
        return self.attr

    def visit_xml(self, fp: TextIOBase):
        if self.cic:
            self.cic.visit_xml(fp)
        if self.hic:
            ind = Indentation.get_indentation()
            ind.incr()
            s = ' '*ind.get_indent()
            s += '<hostinterfaceconnections>\n'
            fp.write(s)
            for a in self.hic:
                a.visit_xml(fp)
            s = ' '*ind.get_indent()
            s += '</hostinterfaceconnections>\n'
            fp.write(s)
            ind.decr()
        if self.parover:
            ind = Indentation.get_indentation()
            ind.incr()
            s = ' '*ind.get_indent()
            s += '<parameter_overrides>\n'
            fp.write(s)
            for a in self.parover:
                a.visit_xml(fp)
            s = ' '*ind.get_indent()
            s += '</parameter_overrides>\n'
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
        if self.cic:
            self.cic.visit_json(fp, terminate)
        if self.hic:
            ind = Indentation.get_indentation()
            ind.incr()
            s = ' '*ind.get_indent()
            s += '"hostinterfaceconnections": [\n'
            fp.write(s)
            n = len(self.hic) - 1
            for i, a in enumerate(self.hic):
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
        if self.parover:
            ind = Indentation.get_indentation()
            ind.incr()
            s = ' '*ind.get_indent()
            s += '"parameter_overrides": [\n'
            fp.write(s)
            n = len(self.parover) - 1
            for i, a in enumerate(self.parover):
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
