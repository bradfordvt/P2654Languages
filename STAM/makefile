ANTLR=antlr4

all: dist/STAMLexer.py dist/STAMParser.py dist/STAMVisitor.py

dist/STAMLexer.py: STAM.g4
	$(ANTLR) -Dlanguage=Python3 STAM.g4 -visitor -o dist

dist/STAMParser.py:  STAM.g4
	$(ANTLR) -Dlanguage=Python3 STAM.g4 -visitor -o dist

dist/STAMVisitor.py: STAM.g4
	$(ANTLR) -Dlanguage=Python3 STAM.g4 -visitor -o dist
