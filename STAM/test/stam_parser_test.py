import unittest
from antlr4 import *
# sys.path.append("c:\\Users\\bvt\\VisualStudioCodeProjects\\P2654Languages\\P2654Languages\\STAM")
# print(sys.path)
from STAM.FormattingVisitor import FormattingVisitor
from STAM.dist.STAMLexer import STAMLexer
from STAM.dist.STAMParser import STAMParser
from STAM.dist.STAMVisitor import STAMVisitor
from STAM.ParserException import ParserException
from STAM.stamErrorListener import MyErrorListener


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parser001(self):
        stam_stream = FileStream('../modules/SerialRegister.stam', encoding="utf-8")
        xml_file = '../data/SerialRegister.xml'
        json_file = '../data/SerialRegister.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser002(self):
        stam_stream = FileStream('../modules/TTL74BCT8374.stam', encoding="utf-8")
        xml_file = '../data/TTL74BCT8374.xml'
        json_file = '../data/TTL74BCT8374.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser003(self):
        stam_stream = FileStream('../modules/FS11495TE.stam', encoding="utf-8")
        xml_file = '../data/FS11495TE.xml'
        json_file = '../data/FS11495TE.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser004(self):
        stam_stream = FileStream('../modules/I2C11495_DEV.stam', encoding="utf-8")
        xml_file = '../data/I2C11495_DEV.xml'
        json_file = '../data/I2C11495_DEV.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser005(self):
        stam_stream = FileStream('../modules/I2C11495_DEV2.stam', encoding="utf-8")
        xml_file = '../data/I2C11495_DEV2.xml'
        json_file = '../data/I2C11495_DEV2.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser006(self):
        stam_stream = FileStream('../modules/I2C11495_DEV3.stam', encoding="utf-8")
        xml_file = '../data/I2C11495_DEV3.xml'
        json_file = '../data/I2C11495_DEV3.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser007(self):
        stam_stream = FileStream('../modules/I2C11495TE.stam', encoding="utf-8")
        xml_file = '../data/I2C11495TE.xml'
        json_file = '../data/I2C11495TE.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser008(self):
        stam_stream = FileStream('../modules/I2C21145TE.stam', encoding="utf-8")
        xml_file = '../data/I2C21145TE.xml'
        json_file = '../data/I2C21145TE.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser009(self):
        stam_stream = FileStream('../modules/I2CDigitalTE.stam', encoding="utf-8")
        xml_file = '../data/I2CDigitalTE.xml'
        json_file = '../data/I2CDigitalTE.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser010(self):
        stam_stream = FileStream('../modules/I2CFSTR.stam', encoding="utf-8")
        xml_file = '../data/I2CFSTR.xml'
        json_file = '../data/I2CFSTR.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser011(self):
        stam_stream = FileStream('../modules/I2CMux.stam', encoding="utf-8")
        xml_file = '../data/I2CMux.xml'
        json_file = '../data/I2CMux.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser012(self):
        stam_stream = FileStream('../modules/JTAGDRMUX.stam', encoding="utf-8")
        xml_file = '../data/JTAGDRMUX.xml'
        json_file = '../data/JTAGDRMUX.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser013(self):
        stam_stream = FileStream('../modules/LatticeBSCAN2.stam', encoding="utf-8")
        xml_file = '../data/LatticeBSCAN2.xml'
        json_file = '../data/LatticeBSCAN2.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser014(self):
        stam_stream = FileStream('../modules/LatticeBSCAN2BB.stam', encoding="utf-8")
        xml_file = '../data/LatticeBSCAN2BB.xml'
        json_file = '../data/LatticeBSCAN2BB.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser015(self):
        stam_stream = FileStream('../modules/LatticeResyncLinker.stam', encoding="utf-8")
        xml_file = '../data/LatticeResyncLinker.xml'
        json_file = '../data/LatticeResyncLinker.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser016(self):
        stam_stream = FileStream('../modules/ModelPointCadence.stam', encoding="utf-8")
        xml_file = '../data/ModelPointCadence.xml'
        json_file = '../data/ModelPointCadence.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser017(self):
        stam_stream = FileStream('../modules/ModelPointSiemens.stam', encoding="utf-8")
        xml_file = '../data/ModelPointSiemens.xml'
        json_file = '../data/ModelPointSiemens.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser018(self):
        stam_stream = FileStream('../modules/ModelPointSynopsis.stam', encoding="utf-8")
        xml_file = '../data/ModelPointSynopsis.xml'
        json_file = '../data/ModelPointSynopsis.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser019(self):
        stam_stream = FileStream('../modules/SpecializedModelPoint.stam', encoding="utf-8")
        xml_file = '../data/SpecializedModelPoint.xml'
        json_file = '../data/SpecializedModelPoint.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    def test_parser020(self):
        stam_stream = FileStream('../modules/TAPBridge.stam', encoding="utf-8")
        xml_file = '../data/TAPBridge.xml'
        json_file = '../data/TAPBridge.json'
        # lexer
        lexer = STAMLexer(stam_stream)
        stream = CommonTokenStream(lexer)
        # parser
        parser = STAMParser(stream)
        ctx = parser.stam_source()
        # evaluator
        visitor = FormattingVisitor()
        fp = open(xml_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_xml(fp)
        fp.close()
        visitor = FormattingVisitor()
        fp = open(json_file, 'w')
        visitor.set_file_pointer(fp)
        output = visitor.visitStam_source(ctx)
        output.visit_json(fp, False)
        fp.close()
        # self.assertEqual(output, 'EHPIC')

    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
