import sys
import unittest
from antlr4 import *
# sys.path.append("c:\\Users\\bvt\\VisualStudioCodeProjects\\P2654Languages\\P2654Languages\\STAM")
# print(sys.path)
from STAM.dist.STAMLexer import STAMLexer
from STAM.dist.STAMParser import STAMParser
from STAM.dist.STAMVisitor import STAMVisitor
from STAM.MyVisitor import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_usenamespace_def001(self):
        data = InputStream('UseNameSpace MyNamespace;')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.useNameSpace_def()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitUseNameSpace_def(ctx)
        self.assertEqual(output, 'MyNamespace')

    def test_namespace_def002(self):
        data = InputStream('UseNameSpace ;')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.useNameSpace_def()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitUseNameSpace_def(ctx)
        self.assertEqual(output, 'Undefined')


if __name__ == '__main__':
    unittest.main()
