# Generated from arithmetic.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .arithmeticParser import arithmeticParser
else:
    from arithmeticParser import arithmeticParser

# This class defines a complete listener for a parse tree produced by arithmeticParser.
class arithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by arithmeticParser#expression.
    def enterExpression(self, ctx:arithmeticParser.ExpressionContext):
        pass

    # Exit a parse tree produced by arithmeticParser#expression.
    def exitExpression(self, ctx:arithmeticParser.ExpressionContext):
        pass


    # Enter a parse tree produced by arithmeticParser#multiplyingExpression.
    def enterMultiplyingExpression(self, ctx:arithmeticParser.MultiplyingExpressionContext):
        pass

    # Exit a parse tree produced by arithmeticParser#multiplyingExpression.
    def exitMultiplyingExpression(self, ctx:arithmeticParser.MultiplyingExpressionContext):
        pass


    # Enter a parse tree produced by arithmeticParser#number.
    def enterNumber(self, ctx:arithmeticParser.NumberContext):
        pass

    # Exit a parse tree produced by arithmeticParser#number.
    def exitNumber(self, ctx:arithmeticParser.NumberContext):
        pass


