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

    def test_namespace_name001(self):
        data = InputStream('MyNamespace')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.nameSpace_name()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitNameSpace_name(ctx)
        self.assertEqual(output, 'MyNamespace')

    def test_parameter_ref001(self):
        data = InputStream('$Param1')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.parameter_ref()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitParameter_ref(ctx)
        self.assertEqual(output, '$Param1')

    def test_parameter_ref002(self):
        data = InputStream('$Param1')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.parameter_ref()
        # evaluator
        visitor = MyVisitor()
        visitor.symbols['Param1'] = "MyParameter"
        output = visitor.visitParameter_ref(ctx)
        self.assertEqual(output, "MyParameter")

    def test_parameter_name001(self):
        data = InputStream('Param1')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.parameter_name()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitParameter_name(ctx)
        self.assertEqual(output, 'Param1')

    def test_pos_int001(self):
        data = InputStream('23456')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitPos_int(ctx)
        self.assertEqual(output, 23456)

    def test_pos_int002(self):
        data = InputStream('23_456')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitPos_int(ctx)
        self.assertEqual(output, 23456)

    def test_pos_int003(self):
        data = InputStream('1')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitPos_int(ctx)
        self.assertEqual(output, 1)

    def test_pos_int004(self):
        data = InputStream('0')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitPos_int(ctx)
        self.assertEqual(output, 0)

    def test_pos_int005(self):
        data = InputStream('2')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitPos_int(ctx)
        self.assertEqual(output, 2)

    def test_pos_int006(self):
        data = InputStream('3')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitPos_int(ctx)
        self.assertEqual(output, 3)

    def test_pos_int007(self):
        data = InputStream('4')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitPos_int(ctx)
        self.assertEqual(output, 4)

    def test_pos_int008(self):
        data = InputStream('5')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitPos_int(ctx)
        self.assertEqual(output, 5)

    def test_pos_int009(self):
        data = InputStream('6')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitPos_int(ctx)
        self.assertEqual(output, 6)

    def test_pos_int010(self):
        data = InputStream('7')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitPos_int(ctx)
        self.assertEqual(output, 7)

    def test_pos_int011(self):
        data = InputStream('8')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitPos_int(ctx)
        self.assertEqual(output, 8)

    def test_pos_int012(self):
        data = InputStream('9')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.pos_int()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitPos_int(ctx)
        self.assertEqual(output, 9)

    def test_Attribute001(self):
        data = InputStream('Attribute atrib1 = "This is the attribute value!", $Parm1, "More value!!!!";')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.attribute_def()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitAttribute_def(ctx)
        self.assertEqual(output, 'atrib1: [ "This is the attribute value!", $Parm1, "More value!!!!" ]')


if __name__ == '__main__':
    unittest.main()
