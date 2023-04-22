#!/usr/bin/env python
"""
    Container class for storing the contents of an Parameter statement in the STAM language.

    This file contains the contents of what was parsed from a STAM file for what was discovered in the Parameter
    statement.  The objects of this class will be contained in the module objects as individual instances
    of each of the parameters defined.  This class also defines visitor methods for each type of formatted outputs
    supported by the parsing tool.

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

from myhdl import intbv

from STAM.stam_model.indentation import Indentation
from io import TextIOBase


class Parameter:
    def __init__(self, name: str, value: list):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def visit_xml(self, fp: TextIOBase):
        ind = Indentation.get_indentation()
        ind.incr()
        s = ' '*ind.get_indent()
        s += '<parameter name="' + self.name + '" >\n'
        ind.incr()
        for val in self.value:
            s += ' '*ind.get_indent()
            if isinstance(val, intbv):
                s += '<value type="int" > "0x' + str(val) + '" </value>\n'
            else:
                s += '<value type="string"> ' + val + ' </value>\n'
        ind.decr()
        s += ' '*ind.get_indent()
        s += '</parameter>\n'
        ind.decr()
        fp.write(s)

    def visit_json(self, fp: TextIOBase, terminate: bool):
        ind = Indentation.get_indentation()
        ind.incr()
        s = ' '*ind.get_indent()
        s += '"' + self.get_name() + '": [\n'
        ind.incr()
        n = len(self.value) - 1
        for i, val in enumerate(self.value):
            s += ' '*ind.get_indent()
            if isinstance(val, intbv):
                s += '{ "type": "int", "val": "0x' + str(val) + '" }'
            else:
                s += '{ "type": "string", "val": ' + val + ' }'
            if i == n:
                s += '\n'
            else:
                s += ',\n'
        ind.decr()
        s += ' '*ind.get_indent()
        if terminate:
            s += '],\n'
        else:
            s += ']\n'
        ind.decr()
        fp.write(s)
