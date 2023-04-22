#!/usr/bin/env python
"""
    Container class for storing the contents of an HosttInterface connection statement in the STAM language.

    This file contains the contents of what was parsed from a STAM file for what was discovered in the
    HostInterface connection statement.  The objects of this class will be contained in the module objects as
    individual instances of each of the host connections defined.  This class also defines visitor methods for each
    type of formatted outputs supported by the parsing tool.

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
__date__ = "2023/04/16"
__deprecated__ = False
__email__ = "bradvt59@gmail.com"
__license__ = "Apache 2.0"
__maintainer__ = "Bradford G. Van Treuren"
__status__ = "Alpha/Experimental"
__version__ = "0.0.1"

from io import TextIOBase

from STAM.stam_model.hostinterface_name import HostInterfaceName
from STAM.stam_model.hosttinterface_source import HostInterfaceSource
from STAM.stam_model.indentation import Indentation


class HostInterfaceConnection:
    def __init__(self, name: HostInterfaceName = HostInterfaceName(), source: HostInterfaceSource = HostInterfaceSource()):
        self.name = name
        self.source = source

    def get_name(self) -> HostInterfaceName:
        return self.name

    def get_source(self) -> HostInterfaceSource:
        return self.source

    def visit_xml(self, fp: TextIOBase):
        ind = Indentation.get_indentation()
        ind.incr()
        s = ' '*ind.get_indent()
        if self.name.get_index() is not None:
            s += '<hostinterfaceconnection name="' + self.name.get_name() + '[' + str(self.name.get_index()) + ']" >\n'
        else:
            s += '<hostinterfaceconnection name="' + self.name.get_name() + '" >\n'
        fp.write(s)
        self.source.visit_xml(fp)
        s = ' '*ind.get_indent()
        s += '</hostinterfaceconnection>\n'
        fp.write(s)
        ind.decr()

    def visit_json(self, fp: TextIOBase, terminate: bool):
        ind = Indentation.get_indentation()
        ind.incr()
        s = ' '*ind.get_indent()
        s += '{\n'
        ind.incr()
        s += ' '*ind.get_indent()
        if self.name.get_index() is not None:
            s += '"name": "' + self.name.get_name() + '[' + str(self.name.get_index()) + ']",\n'
        else:
            s += '"name": "' + self.name.get_name() + '",\n'
        fp.write(s)
        ind.decr()
        self.source.visit_json(fp, False)
        s = ' '*ind.get_indent()
        if terminate:
            s += '},\n'
        else:
            s += '}\n'
        fp.write(s)
        ind.decr()
