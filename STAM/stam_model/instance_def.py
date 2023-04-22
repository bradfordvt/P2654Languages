#!/usr/bin/env python
"""
    Container class for storing the contents of an Instance statement in the STAM language.

    This file contains the contents of what was parsed from a STAM file for what was discovered in the
    Instance statement.  The objects of this class will be contained in the module objects as individual
    instances of each of the Instances defined.  This class also defines visitor methods for each type of
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
__date__ = "2023/04/14"
__deprecated__ = False
__email__ = "bradvt59@gmail.com"
__license__ = "Apache 2.0"
__maintainer__ = "Bradford G. Van Treuren"
__status__ = "Alpha/Experimental"
__version__ = "0.0.1"

from io import TextIOBase
from typing import Any

from STAM.stam_model.indentation import Indentation


class InstanceDef:
    def __init__(self, name: str = '*undefined*', namespace: str = None, module_name: str = '*undefined*', items: list = []):
        self.name = name
        self.namespace = namespace
        self.module_name = module_name
        self.items = items

    def get_name(self) -> str:
        return self.name

    def get_namespace(self) -> str:
        return self.namespace

    def get_module_name(self) -> str:
        return self.module_name

    def get_items(self) -> list:
        return self.items

    def visit_xml(self, fp: TextIOBase):
        ind = Indentation.get_indentation()
        ind.incr()
        s = ' '*ind.get_indent()
        s += '<instance name="' + self.name + '"'
        if self.namespace:
            s += ' namespace="' + self.namespace + '"'
        s += ' module_name="' + self.module_name + '" >\n'
        fp.write(s)
        for i in self.items:
            i.visit_xml(fp)
        ind.incr()
        s = ' '*ind.get_indent()
        s += '<instance_expansion>\n'
        ind.incr()
        s += ' '*ind.get_indent()
        s += '<!--This is where altered contents of the Module template is fleshed out to represent the instance view-->\n'
        ind.decr()
        s += ' '*ind.get_indent()
        s += '</instance_expansion>\n'
        fp.write(s)
        ind.decr()
        s = ' '*ind.get_indent()
        s += '</instance>\n'
        fp.write(s)
        ind.decr()

    def visit_json(self, fp: TextIOBase, terminate: bool):
        ind = Indentation.get_indentation()
        ind.incr()
        s = ' '*ind.get_indent()
        s += '{\n'
        fp.write(s)
        ind.incr()
        s = ' '*ind.get_indent()
        s += '"name" : "' + self.name + '",\n'
        if self.namespace:
            s += ' '*ind.get_indent()
            s += '"namespace" : "' + self.namespace + '",\n'
        s += ' '*ind.get_indent()
        s += '"module_name" : "' + self.module_name + '",\n'
        fp.write(s)
        ind.decr()
        n = len(self.items)
        for i, item in enumerate(self.items):
            if i == n:
                item.visit_json(fp, False)
            else:
                item.visit_json(fp, True)
        ind.incr()
        s = ' '*ind.get_indent()
        s += '"instance_expansion": {\n'
        ind.incr()
        s += ' '*ind.get_indent()
        s += '"__comment__": "This is where altered contents of the Module template is fleshed out to represent the instance view"\n'
        ind.decr()
        s += ' '*ind.get_indent()
        s += '}\n'
        ind.decr()
        s += ' '*ind.get_indent()
        if terminate:
            s += '},\n'
        else:
            s += '}\n'
        fp.write(s)
        ind.decr()
