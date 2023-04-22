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

    def test_protocolFile_name001(self):
        data = InputStream('JTAG.proto')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.protocolFile_name()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitProtocolFile_name(ctx)
        self.assertEqual(output, 'JTAG')

    def test_protocolFile_name002(self):
        data = InputStream('JTAG')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        try:
            # parser
            parser = STAMParser(stream)
            parser._listeners = [MyErrorListener()]
            ctx = parser.protocolFile_name()
            # evaluator
            visitor = MyVisitor()
            output = visitor.visitProtocolFile_name(ctx)
            self.assertFalse(True, 'Did not detect wrong file extension!')
        except ParserException as re:
            print(re)
            self.assertTrue(True, "Detected wrong file extension.")

    def test_protocol_def001(self):
        data = InputStream('Protocol MyProtocol.proto ;')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.protocol_def()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitProtocol_def(ctx)
        self.assertEqual(output, "MyProtocol")

    def test_protocol_def002(self):
        data = InputStream('Protocol I2C.proto;')
        # lexer
        lexer = STAMLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.protocol_def()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visitProtocol_def(ctx)
        self.assertEqual(output, "I2C")


if __name__ == '__main__':
    unittest.main()
