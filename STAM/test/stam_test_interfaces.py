import sys
import unittest
from antlr4 import *
# sys.path.append("c:\\Users\\bvt\\VisualStudioCodeProjects\\P2654Languages\\P2654Languages\\STAM")
# print(sys.path)
from STAM.dist.STAMLexer import STAMLexer
from STAM.dist.STAMParser import STAMParser
from STAM.dist.STAMVisitor import STAMVisitor
from STAM.MyVisitor import *
from STAM.ParserException import ParserException
from STAM.stamErrorListener import MyErrorListener


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_clientInterface_name001(self):
        data = InputStream('EHPIC')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.clientInterface_name()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitClientInterface_name(ctx)
        self.assertEqual(output, 'EHPIC')

    def test_protocol_def001(self):
        data = InputStream('Protocol MyProtocol.proto ;')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.clientInterface_item()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitClientInterface_item(ctx)
        self.assertEqual(output, "MyProtocol")

    def test_clientInterface_def001(self):
        data = InputStream('ClientInterface CI { Protocol I2C.proto; }')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.clientInterface_def()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitClientInterface_def(ctx)
        self.assertEqual(output, "CI: [ I2C ]")

    def test_clientInterface_source001(self):
        data = InputStream('I2CSI.HI')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.clientInterface_source()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitClientInterface_source(ctx)
        self.assertEqual("I2CSI.HI[]", output)

    def test_clientInterface_connection001(self):
        data = InputStream('ClientInterface CI = I2CSI.HI;')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.clientInterface_connection()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitClientInterface_connection(ctx)
        self.assertEqual("CI=I2CSI.HI[]", output)

    def test_Instance001(self):
        test="""Instance I1 Of SpecializedModelPoint {
    ClientInterface CI = I2CSI.HI;
}"""
        data = InputStream(test)
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.instance_def()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitInstance_def(ctx)
        self.assertEqual("I1 <['CI=I2CSI.HI[]']>", output)


if __name__ == '__main__':
    unittest.main()
