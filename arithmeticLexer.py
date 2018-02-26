# Generated from arithmetic.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write(" \b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7\33\n")
        buf.write("\7\r\7\16\7\34\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\3\2\3\5\2\13\f\17\17\"\"\2 \2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3\17\3")
        buf.write("\2\2\2\5\21\3\2\2\2\7\23\3\2\2\2\t\25\3\2\2\2\13\27\3")
        buf.write("\2\2\2\r\32\3\2\2\2\17\20\7-\2\2\20\4\3\2\2\2\21\22\7")
        buf.write("/\2\2\22\6\3\2\2\2\23\24\7,\2\2\24\b\3\2\2\2\25\26\7\61")
        buf.write("\2\2\26\n\3\2\2\2\27\30\4\62;\2\30\f\3\2\2\2\31\33\t\2")
        buf.write("\2\2\32\31\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35\3")
        buf.write("\2\2\2\35\36\3\2\2\2\36\37\b\7\2\2\37\16\3\2\2\2\4\2\34")
        buf.write("\3\2\3\2")
        return buf.getvalue()


class arithmeticLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIV = 4
    DIGIT = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "TIMES", "DIV", "DIGIT", "WS" ]

    ruleNames = [ "PLUS", "MINUS", "TIMES", "DIV", "DIGIT", "WS" ]

    grammarFileName = "arithmetic.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


