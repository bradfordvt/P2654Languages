import sys
from antlr4 import *
from dist.STAMLexer import STAMLexer
from dist.STAMParser import STAMParser
from dist.STAMVisitor import STAMVisitor


class MyVisitor(STAMVisitor):
    # Visit a parse tree produced by STAMParser#stam_source.
    def visitStam_source(self, ctx:STAMParser.Stam_sourceContext):
        module_name v= ctx.module_def().module_name()
        value = module_name + ":\n" + self.visitChildren(ctx).str()
        return value

def main(argv):
    if len(sys.argv) > 1:
        data = FileStream(sys.argv[1])
    else:
        data = InputStream(sys.stdin.readline())
    # lexer
    lexer = STAMLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = STAMParser(stream)
    tree = parser.stam_source()
    # evaluator
    visitor = MyVisitor()
    output = visitor.visit(tree)
    print(output)



if __name__ == "__main__":
    main(sys.argv)