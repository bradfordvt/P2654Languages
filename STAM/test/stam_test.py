import sys
import unittest
from antlr4 import *
sys.path.append("c:\\Users\\bvt\\VisualStudioCodeProjects\\P2654Languages\\P2654Languages\\STAM")
# print(sys.path)
from dist.STAMLexer import STAMLexer
from dist.STAMParser import STAMParser
from dist.STAMVisitor import STAMVisitor
from MyVisitor import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pos_int001(self):
        data = InputStream('23456')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        tree = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)
        self.AssertEquals(output, 23456)

    def test_pos_int002(self):
        data = InputStream('23_456')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        tree = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)
        self.AssertEquals(output, 23456)

    def test_pos_int003(self):
        data = InputStream('1')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        tree = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)
        self.AssertEquals(output, 1)

    def test_pos_int004(self):
        data = InputStream('0')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        tree = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)
        self.AssertEquals(output, 0)

    def test_Attribute001(self):
        data = InputStream('Attribute atrib1 = "This is the attribute value!";')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        tree = parser.attribute_def()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)


if __name__ == '__main__':
    unittest.main()
