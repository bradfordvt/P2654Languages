#!/usr/bin/env python
"""
    Parser error class for storing the messages from STAM language parser.

    This file contains the contents of exceptions raised by the parser when processing a STAM file.

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

from antlr4.error.ErrorListener import ErrorListener
from STAM.ParserException import ParserException


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        raise ParserException("Syntax Error: " + str(line) + ":" + str(column) + ": syntax ERROR, " + str(msg))

    def reportAmbiguity(self, recognizer, dfa, start_index, stop_index, exact, ambig_alts, configs):
        print("Ambiguity ERROR, " + str(configs))
        raise ParserException("Ambiguity ERROR: " + str(configs))

    def reportAttemptingFullContext(self, recognizer, dfa, start_index, stop_index, conflicting_alts, configs):
        raise ParserException("Attempting full context ERROR: " + str(configs))

    def reportContextSensitivity(self, recognizer, dfa, start_index, stop_index, prediction, configs):
        print("Context ERROR, " + str(configs))
        raise ParserException("Context ERROR: " + str(configs))

