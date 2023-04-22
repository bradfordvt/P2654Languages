#!/usr/bin/env python
"""
    Container class for storing the contents of an HostInterface_name statement in the STAM language.

    This file contains the contents of what was parsed from a STAM file for what was discovered in the
    HostInterface_name statement.  The objects of this class will be contained in the module objects as individual
    instances of each of the host interface names defined.  This class also defines visitor methods for each type of
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
__date__ = "2023/04/13"
__deprecated__ = False
__email__ = "bradvt59@gmail.com"
__license__ = "Apache 2.0"
__maintainer__ = "Bradford G. Van Treuren"
__status__ = "Alpha/Experimental"
__version__ = "0.0.1"

from io import TextIOBase
from STAM.stam_model.indentation import Indentation


class HostInterfaceName:
    def __init__(self, name: str = '*undefined*', index: int = None):
        self.name = name
        self.index = index

    def get_name(self) -> str:
        return self.name

    def get_index(self) -> int:
        return self.index

    def visit_xml(self, fp: TextIOBase) -> None:
        ind = Indentation.get_indentation()
        ind.incr()
        s = ' '*ind.get_indent()
        s += ' <hostname name="' + self.name + '"'
        if self.index is not None:
            s += ' index="' + str(self.index) + '"'
        s += ' />\n'
        ind.decr()
        fp.write(s)

    def visit_json(self, fp: TextIOBase, terminate: bool) -> None:
        ind = Indentation.get_indentation()
        ind.incr()
        s = ' '*ind.get_indent()
        s += '"hostname": "' + self.name + '"'
        if self.index is not None:
            s += ',\n"index": "' + str(self.index) + '"'
        if terminate:
            s += ',\n'
        else:
            s += '\n'
        ind.decr()
        fp.write(s)
