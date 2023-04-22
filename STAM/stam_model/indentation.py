#!/usr/bin/env python
"""
    This file keeps track of the formatting flow for a given output.

    This Indentation class implements a Singleton pattern and Factory Method pattern to manage global scope attributes
    used by all formatting visitors.

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

INDENT = 4


class Indentation:
    instance = None

    @staticmethod
    def get_indentation():
        if Indentation.instance is None:
            Indentation.instance = Indentation()
        return Indentation.instance

    def __init__(self):
        self.indent = 0

    def get_indent(self):
        return self.indent

    def incr(self):
        self.indent += INDENT

    def decr(self):
        self.indent -= INDENT
        if self.indent < 0:
            self.indent = 0
