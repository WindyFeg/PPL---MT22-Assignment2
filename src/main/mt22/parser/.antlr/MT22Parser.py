# Generated from f:\Univercity\S2 Y3\PRINCIPLES OF PROGRAMMING LANGUAGES\Assignment\assignment2\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u01b8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\7\2f\n\2\f\2\16")
        buf.write("\2i\13\2\3\2\5\2l\n\2\3\2\7\2o\n\2\f\2\16\2r\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3|\n\3\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u008a\n\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\t\u0091\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u0098")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\5\13\u009f\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ad\n\r")
        buf.write("\3\r\3\r\3\r\7\r\u00b2\n\r\f\r\16\r\u00b5\13\r\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00ca\n\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00d5")
        buf.write("\n\17\f\17\16\17\u00d8\13\17\3\20\3\20\3\21\3\21\3\21")
        buf.write("\5\21\u00df\n\21\3\21\3\21\3\22\3\22\3\22\3\23\5\23\u00e7")
        buf.write("\n\23\3\23\5\23\u00ea\n\23\3\23\3\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u00fc\n\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u0105\n\27\3\27\3\27\5\27\u0109\n\27\3\27\3\27\3\27")
        buf.write("\5\27\u010e\n\27\3\30\3\30\3\31\3\31\3\32\3\32\5\32\u0116")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0122\n\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\5\35\u0130\n\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#")
        buf.write("\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\7\'\u015d\n")
        buf.write("\'\f\'\16\'\u0160\13\'\3\'\3\'\3(\3(\3(\3(\5(\u0168\n")
        buf.write("(\3)\3)\3)\3)\3)\3)\5)\u0170\n)\5)\u0172\n)\3*\3*\3*\3")
        buf.write("*\3*\5*\u0179\n*\3+\3+\3+\3+\3+\5+\u0180\n+\3,\3,\3,\3")
        buf.write(",\3,\3,\5,\u0188\n,\5,\u018a\n,\3-\3-\3-\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u019f\n.\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5")
        buf.write("\61\u01ae\n\61\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u01b6")
        buf.write("\n\62\3\62\3\u015e\4\30\34\63\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`b\2\t\3\2/\63\3\2\64\66\3\2\67<\3\2\65\66\3\2/\60")
        buf.write("\3\2\61\63\6\2\5\5\32\32\35\36  \2\u01c7\2g\3\2\2\2\4")
        buf.write("{\3\2\2\2\6}\3\2\2\2\b\177\3\2\2\2\n\u0081\3\2\2\2\f\u0083")
        buf.write("\3\2\2\2\16\u0089\3\2\2\2\20\u0090\3\2\2\2\22\u0097\3")
        buf.write("\2\2\2\24\u009e\3\2\2\2\26\u00a0\3\2\2\2\30\u00ac\3\2")
        buf.write("\2\2\32\u00b6\3\2\2\2\34\u00c9\3\2\2\2\36\u00d9\3\2\2")
        buf.write("\2 \u00db\3\2\2\2\"\u00e2\3\2\2\2$\u00e6\3\2\2\2&\u00ef")
        buf.write("\3\2\2\2(\u00f3\3\2\2\2*\u00f5\3\2\2\2,\u00ff\3\2\2\2")
        buf.write(".\u010f\3\2\2\2\60\u0111\3\2\2\2\62\u0115\3\2\2\2\64\u0121")
        buf.write("\3\2\2\2\66\u0123\3\2\2\28\u0128\3\2\2\2:\u0131\3\2\2")
        buf.write("\2<\u013c\3\2\2\2>\u013f\3\2\2\2@\u0144\3\2\2\2B\u0147")
        buf.write("\3\2\2\2D\u014c\3\2\2\2F\u014f\3\2\2\2H\u0152\3\2\2\2")
        buf.write("J\u0156\3\2\2\2L\u0159\3\2\2\2N\u0167\3\2\2\2P\u0171\3")
        buf.write("\2\2\2R\u0178\3\2\2\2T\u017f\3\2\2\2V\u0189\3\2\2\2X\u018b")
        buf.write("\3\2\2\2Z\u019e\3\2\2\2\\\u01a0\3\2\2\2^\u01a3\3\2\2\2")
        buf.write("`\u01a6\3\2\2\2b\u01b5\3\2\2\2df\5b\62\2ed\3\2\2\2fi\3")
        buf.write("\2\2\2ge\3\2\2\2gh\3\2\2\2hk\3\2\2\2ig\3\2\2\2jl\5^\60")
        buf.write("\2kj\3\2\2\2kl\3\2\2\2lp\3\2\2\2mo\5b\62\2nm\3\2\2\2o")
        buf.write("r\3\2\2\2pn\3\2\2\2pq\3\2\2\2qs\3\2\2\2rp\3\2\2\2st\7")
        buf.write("\2\2\3t\3\3\2\2\2u|\7\6\2\2v|\7\21\2\2w|\7\b\2\2x|\7\13")
        buf.write("\2\2y|\7\17\2\2z|\5`\61\2{u\3\2\2\2{v\3\2\2\2{w\3\2\2")
        buf.write("\2{x\3\2\2\2{y\3\2\2\2{z\3\2\2\2|\5\3\2\2\2}~\t\2\2\2")
        buf.write("~\7\3\2\2\2\177\u0080\t\3\2\2\u0080\t\3\2\2\2\u0081\u0082")
        buf.write("\7=\2\2\u0082\13\3\2\2\2\u0083\u0084\t\4\2\2\u0084\r\3")
        buf.write("\2\2\2\u0085\u0086\7\36\2\2\u0086\u0087\7!\2\2\u0087\u008a")
        buf.write("\5\16\b\2\u0088\u008a\7\36\2\2\u0089\u0085\3\2\2\2\u0089")
        buf.write("\u0088\3\2\2\2\u008a\17\3\2\2\2\u008b\u0091\5\6\4\2\u008c")
        buf.write("\u0091\5\b\5\2\u008d\u0091\5\n\6\2\u008e\u0091\5\f\7\2")
        buf.write("\u008f\u0091\5\"\22\2\u0090\u008b\3\2\2\2\u0090\u008c")
        buf.write("\3\2\2\2\u0090\u008d\3\2\2\2\u0090\u008e\3\2\2\2\u0090")
        buf.write("\u008f\3\2\2\2\u0091\21\3\2\2\2\u0092\u0098\5\36\20\2")
        buf.write("\u0093\u0098\7\37\2\2\u0094\u0098\5\20\t\2\u0095\u0098")
        buf.write("\5 \21\2\u0096\u0098\5\32\16\2\u0097\u0092\3\2\2\2\u0097")
        buf.write("\u0093\3\2\2\2\u0097\u0094\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0097\u0096\3\2\2\2\u0098\23\3\2\2\2\u0099\u009f\5\36")
        buf.write("\20\2\u009a\u009f\7\37\2\2\u009b\u009f\5\20\t\2\u009c")
        buf.write("\u009f\5 \21\2\u009d\u009f\5\26\f\2\u009e\u0099\3\2\2")
        buf.write("\2\u009e\u009a\3\2\2\2\u009e\u009b\3\2\2\2\u009e\u009c")
        buf.write("\3\2\2\2\u009e\u009d\3\2\2\2\u009f\25\3\2\2\2\u00a0\u00a1")
        buf.write("\7\'\2\2\u00a1\u00a2\5\30\r\2\u00a2\u00a3\7(\2\2\u00a3")
        buf.write("\27\3\2\2\2\u00a4\u00a5\b\r\1\2\u00a5\u00a6\5\24\13\2")
        buf.write("\u00a6\u00a7\5\f\7\2\u00a7\u00a8\5\24\13\2\u00a8\u00ad")
        buf.write("\3\2\2\2\u00a9\u00aa\7\64\2\2\u00aa\u00ad\5\24\13\2\u00ab")
        buf.write("\u00ad\5\24\13\2\u00ac\u00a4\3\2\2\2\u00ac\u00a9\3\2\2")
        buf.write("\2\u00ac\u00ab\3\2\2\2\u00ad\u00b3\3\2\2\2\u00ae\u00af")
        buf.write("\f\5\2\2\u00af\u00b0\t\5\2\2\u00b0\u00b2\5\24\13\2\u00b1")
        buf.write("\u00ae\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2")
        buf.write("\u00b3\u00b4\3\2\2\2\u00b4\31\3\2\2\2\u00b5\u00b3\3\2")
        buf.write("\2\2\u00b6\u00b7\7\'\2\2\u00b7\u00b8\5\34\17\2\u00b8\u00b9")
        buf.write("\7(\2\2\u00b9\33\3\2\2\2\u00ba\u00bb\b\17\1\2\u00bb\u00bc")
        buf.write("\5\22\n\2\u00bc\u00bd\5\n\6\2\u00bd\u00be\5\22\n\2\u00be")
        buf.write("\u00ca\3\2\2\2\u00bf\u00c0\5\22\n\2\u00c0\u00c1\5\f\7")
        buf.write("\2\u00c1\u00c2\5\22\n\2\u00c2\u00ca\3\2\2\2\u00c3\u00c4")
        buf.write("\7\64\2\2\u00c4\u00ca\5\22\n\2\u00c5\u00c6\7\60\2\2\u00c6")
        buf.write("\u00ca\5\22\n\2\u00c7\u00ca\5&\24\2\u00c8\u00ca\5\22\n")
        buf.write("\2\u00c9\u00ba\3\2\2\2\u00c9\u00bf\3\2\2\2\u00c9\u00c3")
        buf.write("\3\2\2\2\u00c9\u00c5\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00ca\u00d6\3\2\2\2\u00cb\u00cc\f\t\2\2")
        buf.write("\u00cc\u00cd\t\5\2\2\u00cd\u00d5\5\22\n\2\u00ce\u00cf")
        buf.write("\f\b\2\2\u00cf\u00d0\t\6\2\2\u00d0\u00d5\5\22\n\2\u00d1")
        buf.write("\u00d2\f\7\2\2\u00d2\u00d3\t\7\2\2\u00d3\u00d5\5\22\n")
        buf.write("\2\u00d4\u00cb\3\2\2\2\u00d4\u00ce\3\2\2\2\u00d4\u00d1")
        buf.write("\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6")
        buf.write("\u00d7\3\2\2\2\u00d7\35\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9")
        buf.write("\u00da\t\b\2\2\u00da\37\3\2\2\2\u00db\u00dc\7\37\2\2\u00dc")
        buf.write("\u00de\7\'\2\2\u00dd\u00df\5T+\2\u00de\u00dd\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\7(\2\2")
        buf.write("\u00e1!\3\2\2\2\u00e2\u00e3\7\37\2\2\u00e3\u00e4\5&\24")
        buf.write("\2\u00e4#\3\2\2\2\u00e5\u00e7\7\27\2\2\u00e6\u00e5\3\2")
        buf.write("\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e9\3\2\2\2\u00e8\u00ea")
        buf.write("\7\24\2\2\u00e9\u00e8\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write("\u00eb\3\2\2\2\u00eb\u00ec\7\37\2\2\u00ec\u00ed\7\"\2")
        buf.write("\2\u00ed\u00ee\5\4\3\2\u00ee%\3\2\2\2\u00ef\u00f0\7%\2")
        buf.write("\2\u00f0\u00f1\5P)\2\u00f1\u00f2\7&\2\2\u00f2\'\3\2\2")
        buf.write("\2\u00f3\u00f4\5\34\17\2\u00f4)\3\2\2\2\u00f5\u00f6\7")
        buf.write("\31\2\2\u00f6\u00f7\7\"\2\2\u00f7\u00f8\7\r\2\2\u00f8")
        buf.write("\u00f9\7\23\2\2\u00f9\u00fb\7\'\2\2\u00fa\u00fc\5R*\2")
        buf.write("\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\3")
        buf.write("\2\2\2\u00fd\u00fe\7(\2\2\u00fe+\3\2\2\2\u00ff\u0100\7")
        buf.write("\37\2\2\u0100\u0101\7\"\2\2\u0101\u0104\7\r\2\2\u0102")
        buf.write("\u0105\7\23\2\2\u0103\u0105\5\4\3\2\u0104\u0102\3\2\2")
        buf.write("\2\u0104\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0108")
        buf.write("\7\'\2\2\u0107\u0109\5R*\2\u0108\u0107\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010d\7(\2\2\u010b")
        buf.write("\u010c\7\27\2\2\u010c\u010e\7\37\2\2\u010d\u010b\3\2\2")
        buf.write("\2\u010d\u010e\3\2\2\2\u010e-\3\2\2\2\u010f\u0110\5L\'")
        buf.write("\2\u0110/\3\2\2\2\u0111\u0112\7\37\2\2\u0112\61\3\2\2")
        buf.write("\2\u0113\u0116\5\60\31\2\u0114\u0116\5\"\22\2\u0115\u0113")
        buf.write("\3\2\2\2\u0115\u0114\3\2\2\2\u0116\63\3\2\2\2\u0117\u0122")
        buf.write("\5\66\34\2\u0118\u0122\58\35\2\u0119\u0122\5<\37\2\u011a")
        buf.write("\u0122\5@!\2\u011b\u0122\5B\"\2\u011c\u0122\5D#\2\u011d")
        buf.write("\u0122\5F$\2\u011e\u0122\5H%\2\u011f\u0122\5J&\2\u0120")
        buf.write("\u0122\5L\'\2\u0121\u0117\3\2\2\2\u0121\u0118\3\2\2\2")
        buf.write("\u0121\u0119\3\2\2\2\u0121\u011a\3\2\2\2\u0121\u011b\3")
        buf.write("\2\2\2\u0121\u011c\3\2\2\2\u0121\u011d\3\2\2\2\u0121\u011e")
        buf.write("\3\2\2\2\u0121\u011f\3\2\2\2\u0121\u0120\3\2\2\2\u0122")
        buf.write("\65\3\2\2\2\u0123\u0124\5\62\32\2\u0124\u0125\7+\2\2\u0125")
        buf.write("\u0126\5\34\17\2\u0126\u0127\7#\2\2\u0127\67\3\2\2\2\u0128")
        buf.write("\u0129\7\16\2\2\u0129\u012a\7\'\2\2\u012a\u012b\5\34\17")
        buf.write("\2\u012b\u012c\7(\2\2\u012c\u012f\5\64\33\2\u012d\u012e")
        buf.write("\7\n\2\2\u012e\u0130\5\64\33\2\u012f\u012d\3\2\2\2\u012f")
        buf.write("\u0130\3\2\2\2\u01309\3\2\2\2\u0131\u0132\7\f\2\2\u0132")
        buf.write("\u0133\7\'\2\2\u0133\u0134\5\60\31\2\u0134\u0135\7+\2")
        buf.write("\2\u0135\u0136\5\34\17\2\u0136\u0137\7!\2\2\u0137\u0138")
        buf.write("\5\30\r\2\u0138\u0139\7!\2\2\u0139\u013a\5\34\17\2\u013a")
        buf.write("\u013b\7(\2\2\u013b;\3\2\2\2\u013c\u013d\5:\36\2\u013d")
        buf.write("\u013e\5L\'\2\u013e=\3\2\2\2\u013f\u0140\7\22\2\2\u0140")
        buf.write("\u0141\7\'\2\2\u0141\u0142\5\30\r\2\u0142\u0143\7(\2\2")
        buf.write("\u0143?\3\2\2\2\u0144\u0145\5> \2\u0145\u0146\5\64\33")
        buf.write("\2\u0146A\3\2\2\2\u0147\u0148\7\t\2\2\u0148\u0149\5L\'")
        buf.write("\2\u0149\u014a\5> \2\u014a\u014b\7#\2\2\u014bC\3\2\2\2")
        buf.write("\u014c\u014d\7\7\2\2\u014d\u014e\7#\2\2\u014eE\3\2\2\2")
        buf.write("\u014f\u0150\7\25\2\2\u0150\u0151\7#\2\2\u0151G\3\2\2")
        buf.write("\2\u0152\u0153\7\20\2\2\u0153\u0154\5\34\17\2\u0154\u0155")
        buf.write("\7#\2\2\u0155I\3\2\2\2\u0156\u0157\5 \21\2\u0157\u0158")
        buf.write("\7#\2\2\u0158K\3\2\2\2\u0159\u015e\7)\2\2\u015a\u015d")
        buf.write("\5V,\2\u015b\u015d\5X-\2\u015c\u015a\3\2\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015f\3\2\2\2\u015e")
        buf.write("\u015c\3\2\2\2\u015f\u0161\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0161\u0162\7*\2\2\u0162M\3\2\2\2\u0163\u0164\7\37\2")
        buf.write("\2\u0164\u0165\7!\2\2\u0165\u0168\5N(\2\u0166\u0168\7")
        buf.write("\37\2\2\u0167\u0163\3\2\2\2\u0167\u0166\3\2\2\2\u0168")
        buf.write("O\3\2\2\2\u0169\u016a\5\34\17\2\u016a\u016b\7!\2\2\u016b")
        buf.write("\u016c\5P)\2\u016c\u0172\3\2\2\2\u016d\u016f\5\34\17\2")
        buf.write("\u016e\u0170\7#\2\2\u016f\u016e\3\2\2\2\u016f\u0170\3")
        buf.write("\2\2\2\u0170\u0172\3\2\2\2\u0171\u0169\3\2\2\2\u0171\u016d")
        buf.write("\3\2\2\2\u0172Q\3\2\2\2\u0173\u0174\5$\23\2\u0174\u0175")
        buf.write("\7!\2\2\u0175\u0176\5R*\2\u0176\u0179\3\2\2\2\u0177\u0179")
        buf.write("\5$\23\2\u0178\u0173\3\2\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("S\3\2\2\2\u017a\u017b\5(\25\2\u017b\u017c\7!\2\2\u017c")
        buf.write("\u017d\5T+\2\u017d\u0180\3\2\2\2\u017e\u0180\5(\25\2\u017f")
        buf.write("\u017a\3\2\2\2\u017f\u017e\3\2\2\2\u0180U\3\2\2\2\u0181")
        buf.write("\u0182\5\64\33\2\u0182\u0183\7#\2\2\u0183\u0184\5V,\2")
        buf.write("\u0184\u018a\3\2\2\2\u0185\u0187\5\64\33\2\u0186\u0188")
        buf.write("\7#\2\2\u0187\u0186\3\2\2\2\u0187\u0188\3\2\2\2\u0188")
        buf.write("\u018a\3\2\2\2\u0189\u0181\3\2\2\2\u0189\u0185\3\2\2\2")
        buf.write("\u018aW\3\2\2\2\u018b\u018c\5Z.\2\u018c\u018d\7#\2\2\u018d")
        buf.write("Y\3\2\2\2\u018e\u018f\7\37\2\2\u018f\u0190\7!\2\2\u0190")
        buf.write("\u0191\5Z.\2\u0191\u0192\7!\2\2\u0192\u0193\5\34\17\2")
        buf.write("\u0193\u019f\3\2\2\2\u0194\u0195\7\37\2\2\u0195\u0196")
        buf.write("\7\"\2\2\u0196\u0197\5\4\3\2\u0197\u0198\7+\2\2\u0198")
        buf.write("\u0199\5\34\17\2\u0199\u019f\3\2\2\2\u019a\u019b\5N(\2")
        buf.write("\u019b\u019c\7\"\2\2\u019c\u019d\5\4\3\2\u019d\u019f\3")
        buf.write("\2\2\2\u019e\u018e\3\2\2\2\u019e\u0194\3\2\2\2\u019e\u019a")
        buf.write("\3\2\2\2\u019f[\3\2\2\2\u01a0\u01a1\5,\27\2\u01a1\u01a2")
        buf.write("\5.\30\2\u01a2]\3\2\2\2\u01a3\u01a4\5*\26\2\u01a4\u01a5")
        buf.write("\5.\30\2\u01a5_\3\2\2\2\u01a6\u01ad\7\30\2\2\u01a7\u01a8")
        buf.write("\7%\2\2\u01a8\u01a9\5\16\b\2\u01a9\u01aa\7&\2\2\u01aa")
        buf.write("\u01ab\7\26\2\2\u01ab\u01ac\5\4\3\2\u01ac\u01ae\3\2\2")
        buf.write("\2\u01ad\u01a7\3\2\2\2\u01ad\u01ae\3\2\2\2\u01aea\3\2")
        buf.write("\2\2\u01af\u01b6\5\\/\2\u01b0\u01b1\5Z.\2\u01b1\u01b2")
        buf.write("\7#\2\2\u01b2\u01b6\3\2\2\2\u01b3\u01b6\5P)\2\u01b4\u01b6")
        buf.write("\5V,\2\u01b5\u01af\3\2\2\2\u01b5\u01b0\3\2\2\2\u01b5\u01b3")
        buf.write("\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6c\3\2\2\2%gkp{\u0089")
        buf.write("\u0090\u0097\u009e\u00ac\u00b3\u00c9\u00d4\u00d6\u00de")
        buf.write("\u00e6\u00e9\u00fb\u0104\u0108\u010d\u0115\u0121\u012f")
        buf.write("\u015c\u015e\u0167\u016f\u0171\u0178\u017f\u0187\u0189")
        buf.write("\u019e\u01ad\u01b5")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
                     "'float'", "'for'", "'function'", "'if'", "'integer'", 
                     "'return'", "'string'", "'while'", "'void'", "'out'", 
                     "'continue'", "'of'", "'inherit'", "'array'", "'main'", 
                     "<INVALID>", "'false'", "'true'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "':'", "';'", "'.'", 
                     "'['", "']'", "'('", "')'", "'{'", "'}'", "'='", "'\"'", 
                     "'0'", "'_'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>", "COMMENT_C", "COMMENT_CPP", "STR", "AUTO", 
                      "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", 
                      "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "WHILE", 
                      "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                      "MAIN", "BOOL", "FALSE", "TRUE", "FLO", "INT", "ID", 
                      "ARR", "COMA", "COL", "SEM", "DOT", "LSB", "RSB", 
                      "LB", "RB", "LCB", "RCB", "EQU", "DB", "ZERO", "UNDE", 
                      "PLUS", "MINU", "MUTI", "DIVI", "MODU", "NOT", "AND", 
                      "OR", "EQUL", "NEQ", "LESS", "LOEQ", "GREA", "GOEQ", 
                      "SCOPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vartype = 1
    RULE_arithmetricop = 2
    RULE_booleanop = 3
    RULE_stringop = 4
    RULE_relationalop = 5
    RULE_demention = 6
    RULE_operator = 7
    RULE_operand = 8
    RULE_condeoperand = 9
    RULE_subcondexpression = 10
    RULE_condexpression = 11
    RULE_subexpression = 12
    RULE_expression = 13
    RULE_constant = 14
    RULE_functioncall = 15
    RULE_indexop = 16
    RULE_parameter = 17
    RULE_indexexpression = 18
    RULE_arguement = 19
    RULE_functionmainprot = 20
    RULE_functionprot = 21
    RULE_functionbody = 22
    RULE_scalarvar = 23
    RULE_lhs = 24
    RULE_statement = 25
    RULE_assignstatement = 26
    RULE_ifstatement = 27
    RULE_forhead = 28
    RULE_forstatement = 29
    RULE_whilecondition = 30
    RULE_whilestatement = 31
    RULE_dowhilestatement = 32
    RULE_breakstatement = 33
    RULE_continuestatement = 34
    RULE_returnstatement = 35
    RULE_callstatement = 36
    RULE_blockstatement = 37
    RULE_idlist = 38
    RULE_expressionlist = 39
    RULE_parameterlist = 40
    RULE_arguementlist = 41
    RULE_statementlist = 42
    RULE_variabledecl = 43
    RULE_variabledecls = 44
    RULE_functiondecl = 45
    RULE_mainfunction = 46
    RULE_arraytype = 47
    RULE_decl = 48

    ruleNames =  [ "program", "vartype", "arithmetricop", "booleanop", "stringop", 
                   "relationalop", "demention", "operator", "operand", "condeoperand", 
                   "subcondexpression", "condexpression", "subexpression", 
                   "expression", "constant", "functioncall", "indexop", 
                   "parameter", "indexexpression", "arguement", "functionmainprot", 
                   "functionprot", "functionbody", "scalarvar", "lhs", "statement", 
                   "assignstatement", "ifstatement", "forhead", "forstatement", 
                   "whilecondition", "whilestatement", "dowhilestatement", 
                   "breakstatement", "continuestatement", "returnstatement", 
                   "callstatement", "blockstatement", "idlist", "expressionlist", 
                   "parameterlist", "arguementlist", "statementlist", "variabledecl", 
                   "variabledecls", "functiondecl", "mainfunction", "arraytype", 
                   "decl" ]

    EOF = Token.EOF
    COMMENT_C=1
    COMMENT_CPP=2
    STR=3
    AUTO=4
    BREAK=5
    BOOLEAN=6
    DO=7
    ELSE=8
    FLOAT=9
    FOR=10
    FUNCTION=11
    IF=12
    INTEGER=13
    RETURN=14
    STRING=15
    WHILE=16
    VOID=17
    OUT=18
    CONTINUE=19
    OF=20
    INHERIT=21
    ARRAY=22
    MAIN=23
    BOOL=24
    FALSE=25
    TRUE=26
    FLO=27
    INT=28
    ID=29
    ARR=30
    COMA=31
    COL=32
    SEM=33
    DOT=34
    LSB=35
    RSB=36
    LB=37
    RB=38
    LCB=39
    RCB=40
    EQU=41
    DB=42
    ZERO=43
    UNDE=44
    PLUS=45
    MINU=46
    MUTI=47
    DIVI=48
    MODU=49
    NOT=50
    AND=51
    OR=52
    EQUL=53
    NEQ=54
    LESS=55
    LOEQ=56
    GREA=57
    GOEQ=58
    SCOPE=59
    WS=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.DeclContext)
            else:
                return self.getTypedRuleContext(MT22Parser.DeclContext,i)


        def mainfunction(self):
            return self.getTypedRuleContext(MT22Parser.MainfunctionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 98
                    self.decl() 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.MAIN:
                self.state = 104
                self.mainfunction()


            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STR) | (1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.BOOL) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ID) | (1 << MT22Parser.ARR) | (1 << MT22Parser.LSB) | (1 << MT22Parser.LB) | (1 << MT22Parser.LCB) | (1 << MT22Parser.PLUS) | (1 << MT22Parser.MINU) | (1 << MT22Parser.MUTI) | (1 << MT22Parser.DIVI) | (1 << MT22Parser.MODU) | (1 << MT22Parser.NOT) | (1 << MT22Parser.AND) | (1 << MT22Parser.OR) | (1 << MT22Parser.EQUL) | (1 << MT22Parser.NEQ) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LOEQ) | (1 << MT22Parser.GREA) | (1 << MT22Parser.GOEQ) | (1 << MT22Parser.SCOPE))) != 0):
                self.state = 107
                self.decl()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def arraytype(self):
            return self.getTypedRuleContext(MT22Parser.ArraytypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vartype




    def vartype(self):

        localctx = MT22Parser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vartype)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(MT22Parser.AUTO)
                pass
            elif token in [MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.match(MT22Parser.STRING)
                pass
            elif token in [MT22Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.match(MT22Parser.BOOLEAN)
                pass
            elif token in [MT22Parser.FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
                self.match(MT22Parser.FLOAT)
                pass
            elif token in [MT22Parser.INTEGER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 119
                self.match(MT22Parser.INTEGER)
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 120
                self.arraytype()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmetricopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINU(self):
            return self.getToken(MT22Parser.MINU, 0)

        def PLUS(self):
            return self.getToken(MT22Parser.PLUS, 0)

        def MUTI(self):
            return self.getToken(MT22Parser.MUTI, 0)

        def DIVI(self):
            return self.getToken(MT22Parser.DIVI, 0)

        def MODU(self):
            return self.getToken(MT22Parser.MODU, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arithmetricop




    def arithmetricop(self):

        localctx = MT22Parser.ArithmetricopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arithmetricop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.PLUS) | (1 << MT22Parser.MINU) | (1 << MT22Parser.MUTI) | (1 << MT22Parser.DIVI) | (1 << MT22Parser.MODU))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_booleanop




    def booleanop(self):

        localctx = MT22Parser.BooleanopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_booleanop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.NOT) | (1 << MT22Parser.AND) | (1 << MT22Parser.OR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCOPE(self):
            return self.getToken(MT22Parser.SCOPE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_stringop




    def stringop(self):

        localctx = MT22Parser.StringopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stringop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(MT22Parser.SCOPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUL(self):
            return self.getToken(MT22Parser.EQUL, 0)

        def NEQ(self):
            return self.getToken(MT22Parser.NEQ, 0)

        def LESS(self):
            return self.getToken(MT22Parser.LESS, 0)

        def GREA(self):
            return self.getToken(MT22Parser.GREA, 0)

        def LOEQ(self):
            return self.getToken(MT22Parser.LOEQ, 0)

        def GOEQ(self):
            return self.getToken(MT22Parser.GOEQ, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_relationalop




    def relationalop(self):

        localctx = MT22Parser.RelationalopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relationalop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUL) | (1 << MT22Parser.NEQ) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LOEQ) | (1 << MT22Parser.GREA) | (1 << MT22Parser.GOEQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DementionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MT22Parser.INT, 0)

        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def demention(self):
            return self.getTypedRuleContext(MT22Parser.DementionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_demention




    def demention(self):

        localctx = MT22Parser.DementionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_demention)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(MT22Parser.INT)
                self.state = 132
                self.match(MT22Parser.COMA)
                self.state = 133
                self.demention()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(MT22Parser.INT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetricop(self):
            return self.getTypedRuleContext(MT22Parser.ArithmetricopContext,0)


        def booleanop(self):
            return self.getTypedRuleContext(MT22Parser.BooleanopContext,0)


        def stringop(self):
            return self.getTypedRuleContext(MT22Parser.StringopContext,0)


        def relationalop(self):
            return self.getTypedRuleContext(MT22Parser.RelationalopContext,0)


        def indexop(self):
            return self.getTypedRuleContext(MT22Parser.IndexopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_operator




    def operator(self):

        localctx = MT22Parser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operator)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.PLUS, MT22Parser.MINU, MT22Parser.MUTI, MT22Parser.DIVI, MT22Parser.MODU]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.arithmetricop()
                pass
            elif token in [MT22Parser.NOT, MT22Parser.AND, MT22Parser.OR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.booleanop()
                pass
            elif token in [MT22Parser.SCOPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.stringop()
                pass
            elif token in [MT22Parser.EQUL, MT22Parser.NEQ, MT22Parser.LESS, MT22Parser.LOEQ, MT22Parser.GREA, MT22Parser.GOEQ]:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.relationalop()
                pass
            elif token in [MT22Parser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 141
                self.indexop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(MT22Parser.ConstantContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def operator(self):
            return self.getTypedRuleContext(MT22Parser.OperatorContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(MT22Parser.FunctioncallContext,0)


        def subexpression(self):
            return self.getTypedRuleContext(MT22Parser.SubexpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_operand




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operand)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.constant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(MT22Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.operator()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.functioncall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 148
                self.subexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondeoperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(MT22Parser.ConstantContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def operator(self):
            return self.getTypedRuleContext(MT22Parser.OperatorContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(MT22Parser.FunctioncallContext,0)


        def subcondexpression(self):
            return self.getTypedRuleContext(MT22Parser.SubcondexpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_condeoperand




    def condeoperand(self):

        localctx = MT22Parser.CondeoperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condeoperand)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.constant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(MT22Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.operator()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.functioncall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.subcondexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubcondexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def condexpression(self):
            return self.getTypedRuleContext(MT22Parser.CondexpressionContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_subcondexpression




    def subcondexpression(self):

        localctx = MT22Parser.SubcondexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_subcondexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(MT22Parser.LB)
            self.state = 159
            self.condexpression(0)
            self.state = 160
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condeoperand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.CondeoperandContext)
            else:
                return self.getTypedRuleContext(MT22Parser.CondeoperandContext,i)


        def relationalop(self):
            return self.getTypedRuleContext(MT22Parser.RelationalopContext,0)


        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def condexpression(self):
            return self.getTypedRuleContext(MT22Parser.CondexpressionContext,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_condexpression



    def condexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.CondexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_condexpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 163
                self.condeoperand()
                self.state = 164
                self.relationalop()
                self.state = 165
                self.condeoperand()
                pass

            elif la_ == 2:
                self.state = 167
                self.match(MT22Parser.NOT)
                self.state = 168
                self.condeoperand()
                pass

            elif la_ == 3:
                self.state = 169
                self.condeoperand()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.CondexpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condexpression)
                    self.state = 172
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 173
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 174
                    self.condeoperand() 
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SubexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_subexpression




    def subexpression(self):

        localctx = MT22Parser.SubexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_subexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(MT22Parser.LB)
            self.state = 181
            self.expression(0)
            self.state = 182
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.OperandContext)
            else:
                return self.getTypedRuleContext(MT22Parser.OperandContext,i)


        def stringop(self):
            return self.getTypedRuleContext(MT22Parser.StringopContext,0)


        def relationalop(self):
            return self.getTypedRuleContext(MT22Parser.RelationalopContext,0)


        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def MINU(self):
            return self.getToken(MT22Parser.MINU, 0)

        def indexexpression(self):
            return self.getTypedRuleContext(MT22Parser.IndexexpressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def PLUS(self):
            return self.getToken(MT22Parser.PLUS, 0)

        def MUTI(self):
            return self.getToken(MT22Parser.MUTI, 0)

        def DIVI(self):
            return self.getToken(MT22Parser.DIVI, 0)

        def MODU(self):
            return self.getToken(MT22Parser.MODU, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 185
                self.operand()
                self.state = 186
                self.stringop()
                self.state = 187
                self.operand()
                pass

            elif la_ == 2:
                self.state = 189
                self.operand()
                self.state = 190
                self.relationalop()
                self.state = 191
                self.operand()
                pass

            elif la_ == 3:
                self.state = 193
                self.match(MT22Parser.NOT)
                self.state = 194
                self.operand()
                pass

            elif la_ == 4:
                self.state = 195
                self.match(MT22Parser.MINU)
                self.state = 196
                self.operand()
                pass

            elif la_ == 5:
                self.state = 197
                self.indexexpression()
                pass

            elif la_ == 6:
                self.state = 198
                self.operand()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 210
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = MT22Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 201
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 202
                        _la = self._input.LA(1)
                        if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 203
                        self.operand()
                        pass

                    elif la_ == 2:
                        localctx = MT22Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 204
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 205
                        _la = self._input.LA(1)
                        if not(_la==MT22Parser.PLUS or _la==MT22Parser.MINU):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 206
                        self.operand()
                        pass

                    elif la_ == 3:
                        localctx = MT22Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 207
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 208
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUTI) | (1 << MT22Parser.DIVI) | (1 << MT22Parser.MODU))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 209
                        self.operand()
                        pass

             
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(MT22Parser.STR, 0)

        def BOOL(self):
            return self.getToken(MT22Parser.BOOL, 0)

        def FLO(self):
            return self.getToken(MT22Parser.FLO, 0)

        def INT(self):
            return self.getToken(MT22Parser.INT, 0)

        def ARR(self):
            return self.getToken(MT22Parser.ARR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_constant




    def constant(self):

        localctx = MT22Parser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STR) | (1 << MT22Parser.BOOL) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ARR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def arguementlist(self):
            return self.getTypedRuleContext(MT22Parser.ArguementlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functioncall




    def functioncall(self):

        localctx = MT22Parser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functioncall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(MT22Parser.ID)
            self.state = 218
            self.match(MT22Parser.LB)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STR) | (1 << MT22Parser.BOOL) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ID) | (1 << MT22Parser.ARR) | (1 << MT22Parser.LSB) | (1 << MT22Parser.LB) | (1 << MT22Parser.PLUS) | (1 << MT22Parser.MINU) | (1 << MT22Parser.MUTI) | (1 << MT22Parser.DIVI) | (1 << MT22Parser.MODU) | (1 << MT22Parser.NOT) | (1 << MT22Parser.AND) | (1 << MT22Parser.OR) | (1 << MT22Parser.EQUL) | (1 << MT22Parser.NEQ) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LOEQ) | (1 << MT22Parser.GREA) | (1 << MT22Parser.GOEQ) | (1 << MT22Parser.SCOPE))) != 0):
                self.state = 219
                self.arguementlist()


            self.state = 222
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def indexexpression(self):
            return self.getTypedRuleContext(MT22Parser.IndexexpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_indexop




    def indexop(self):

        localctx = MT22Parser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MT22Parser.ID)
            self.state = 225
            self.indexexpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameter




    def parameter(self):

        localctx = MT22Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 227
                self.match(MT22Parser.INHERIT)


            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 230
                self.match(MT22Parser.OUT)


            self.state = 233
            self.match(MT22Parser.ID)
            self.state = 234
            self.match(MT22Parser.COL)
            self.state = 235
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_indexexpression




    def indexexpression(self):

        localctx = MT22Parser.IndexexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_indexexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(MT22Parser.LSB)
            self.state = 238
            self.expressionlist()
            self.state = 239
            self.match(MT22Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArguementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arguement




    def arguement(self):

        localctx = MT22Parser.ArguementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arguement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionmainprotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(MT22Parser.MAIN, 0)

        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(MT22Parser.ParameterlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionmainprot




    def functionmainprot(self):

        localctx = MT22Parser.FunctionmainprotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_functionmainprot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(MT22Parser.MAIN)
            self.state = 244
            self.match(MT22Parser.COL)
            self.state = 245
            self.match(MT22Parser.FUNCTION)
            self.state = 246
            self.match(MT22Parser.VOID)
            self.state = 247
            self.match(MT22Parser.LB)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.OUT) | (1 << MT22Parser.INHERIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 248
                self.parameterlist()


            self.state = 251
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionprotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def parameterlist(self):
            return self.getTypedRuleContext(MT22Parser.ParameterlistContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functionprot




    def functionprot(self):

        localctx = MT22Parser.FunctionprotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_functionprot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(MT22Parser.ID)
            self.state = 254
            self.match(MT22Parser.COL)
            self.state = 255
            self.match(MT22Parser.FUNCTION)
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.VOID]:
                self.state = 256
                self.match(MT22Parser.VOID)
                pass
            elif token in [MT22Parser.AUTO, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING, MT22Parser.ARRAY]:
                self.state = 257
                self.vartype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 260
            self.match(MT22Parser.LB)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.OUT) | (1 << MT22Parser.INHERIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 261
                self.parameterlist()


            self.state = 264
            self.match(MT22Parser.RB)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 265
                self.match(MT22Parser.INHERIT)
                self.state = 266
                self.match(MT22Parser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionbody




    def functionbody(self):

        localctx = MT22Parser.FunctionbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_functionbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_scalarvar




    def scalarvar(self):

        localctx = MT22Parser.ScalarvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_scalarvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(MT22Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarvar(self):
            return self.getTypedRuleContext(MT22Parser.ScalarvarContext,0)


        def indexop(self):
            return self.getTypedRuleContext(MT22Parser.IndexopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_lhs




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_lhs)
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.scalarvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.indexop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstatement(self):
            return self.getTypedRuleContext(MT22Parser.AssignstatementContext,0)


        def ifstatement(self):
            return self.getTypedRuleContext(MT22Parser.IfstatementContext,0)


        def forstatement(self):
            return self.getTypedRuleContext(MT22Parser.ForstatementContext,0)


        def whilestatement(self):
            return self.getTypedRuleContext(MT22Parser.WhilestatementContext,0)


        def dowhilestatement(self):
            return self.getTypedRuleContext(MT22Parser.DowhilestatementContext,0)


        def breakstatement(self):
            return self.getTypedRuleContext(MT22Parser.BreakstatementContext,0)


        def continuestatement(self):
            return self.getTypedRuleContext(MT22Parser.ContinuestatementContext,0)


        def returnstatement(self):
            return self.getTypedRuleContext(MT22Parser.ReturnstatementContext,0)


        def callstatement(self):
            return self.getTypedRuleContext(MT22Parser.CallstatementContext,0)


        def blockstatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statement)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.assignstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.ifstatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.forstatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.whilestatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 281
                self.dowhilestatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 282
                self.breakstatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 283
                self.continuestatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 284
                self.returnstatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 285
                self.callstatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 286
                self.blockstatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def EQU(self):
            return self.getToken(MT22Parser.EQU, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignstatement




    def assignstatement(self):

        localctx = MT22Parser.AssignstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.lhs()
            self.state = 290
            self.match(MT22Parser.EQU)
            self.state = 291
            self.expression(0)
            self.state = 292
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_ifstatement




    def ifstatement(self):

        localctx = MT22Parser.IfstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ifstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(MT22Parser.IF)
            self.state = 295
            self.match(MT22Parser.LB)
            self.state = 296
            self.expression(0)
            self.state = 297
            self.match(MT22Parser.RB)
            self.state = 298
            self.statement()
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 299
                self.match(MT22Parser.ELSE)
                self.state = 300
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForheadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def scalarvar(self):
            return self.getTypedRuleContext(MT22Parser.ScalarvarContext,0)


        def EQU(self):
            return self.getToken(MT22Parser.EQU, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMA)
            else:
                return self.getToken(MT22Parser.COMA, i)

        def condexpression(self):
            return self.getTypedRuleContext(MT22Parser.CondexpressionContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_forhead




    def forhead(self):

        localctx = MT22Parser.ForheadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_forhead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(MT22Parser.FOR)
            self.state = 304
            self.match(MT22Parser.LB)
            self.state = 305
            self.scalarvar()
            self.state = 306
            self.match(MT22Parser.EQU)
            self.state = 307
            self.expression(0)
            self.state = 308
            self.match(MT22Parser.COMA)
            self.state = 309
            self.condexpression(0)
            self.state = 310
            self.match(MT22Parser.COMA)
            self.state = 311
            self.expression(0)
            self.state = 312
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forhead(self):
            return self.getTypedRuleContext(MT22Parser.ForheadContext,0)


        def blockstatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forstatement




    def forstatement(self):

        localctx = MT22Parser.ForstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.forhead()
            self.state = 315
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileconditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def condexpression(self):
            return self.getTypedRuleContext(MT22Parser.CondexpressionContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_whilecondition




    def whilecondition(self):

        localctx = MT22Parser.WhileconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_whilecondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(MT22Parser.WHILE)
            self.state = 318
            self.match(MT22Parser.LB)
            self.state = 319
            self.condexpression(0)
            self.state = 320
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def whilecondition(self):
            return self.getTypedRuleContext(MT22Parser.WhileconditionContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whilestatement




    def whilestatement(self):

        localctx = MT22Parser.WhilestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_whilestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.whilecondition()
            self.state = 323
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def blockstatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatementContext,0)


        def whilecondition(self):
            return self.getTypedRuleContext(MT22Parser.WhileconditionContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhilestatement




    def dowhilestatement(self):

        localctx = MT22Parser.DowhilestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_dowhilestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(MT22Parser.DO)
            self.state = 326
            self.blockstatement()
            self.state = 327
            self.whilecondition()
            self.state = 328
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakstatement




    def breakstatement(self):

        localctx = MT22Parser.BreakstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_breakstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(MT22Parser.BREAK)
            self.state = 331
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continuestatement




    def continuestatement(self):

        localctx = MT22Parser.ContinuestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_continuestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(MT22Parser.CONTINUE)
            self.state = 334
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_returnstatement




    def returnstatement(self):

        localctx = MT22Parser.ReturnstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_returnstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(MT22Parser.RETURN)
            self.state = 337
            self.expression(0)
            self.state = 338
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functioncall(self):
            return self.getTypedRuleContext(MT22Parser.FunctioncallContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callstatement




    def callstatement(self):

        localctx = MT22Parser.CallstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_callstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.functioncall()
            self.state = 341
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def statementlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementlistContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementlistContext,i)


        def variabledecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.VariabledeclContext)
            else:
                return self.getTypedRuleContext(MT22Parser.VariabledeclContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockstatement




    def blockstatement(self):

        localctx = MT22Parser.BlockstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_blockstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(MT22Parser.LCB)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 346
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        self.state = 344
                        self.statementlist()
                        pass

                    elif la_ == 2:
                        self.state = 345
                        self.variabledecl()
                        pass

             
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 351
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idlist




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_idlist)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.match(MT22Parser.ID)
                self.state = 354
                self.match(MT22Parser.COMA)
                self.state = 355
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expressionlist




    def expressionlist(self):

        localctx = MT22Parser.ExpressionlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expressionlist)
        self._la = 0 # Token type
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.expression(0)
                self.state = 360
                self.match(MT22Parser.COMA)
                self.state = 361
                self.expressionlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.expression(0)
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MT22Parser.SEM:
                    self.state = 364
                    self.match(MT22Parser.SEM)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MT22Parser.ParameterContext,0)


        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(MT22Parser.ParameterlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_parameterlist




    def parameterlist(self):

        localctx = MT22Parser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_parameterlist)
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.parameter()
                self.state = 370
                self.match(MT22Parser.COMA)
                self.state = 371
                self.parameterlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArguementlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arguement(self):
            return self.getTypedRuleContext(MT22Parser.ArguementContext,0)


        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def arguementlist(self):
            return self.getTypedRuleContext(MT22Parser.ArguementlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arguementlist




    def arguementlist(self):

        localctx = MT22Parser.ArguementlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arguementlist)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.arguement()
                self.state = 377
                self.match(MT22Parser.COMA)
                self.state = 378
                self.arguementlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.arguement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def statementlist(self):
            return self.getTypedRuleContext(MT22Parser.StatementlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statementlist




    def statementlist(self):

        localctx = MT22Parser.StatementlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_statementlist)
        self._la = 0 # Token type
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.statement()
                self.state = 384
                self.match(MT22Parser.SEM)
                self.state = 385
                self.statementlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.statement()
                self.state = 389
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MT22Parser.SEM:
                    self.state = 388
                    self.match(MT22Parser.SEM)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariabledeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variabledecls(self):
            return self.getTypedRuleContext(MT22Parser.VariabledeclsContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_variabledecl




    def variabledecl(self):

        localctx = MT22Parser.VariabledeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_variabledecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.variabledecls()
            self.state = 394
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariabledeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMA)
            else:
                return self.getToken(MT22Parser.COMA, i)

        def variabledecls(self):
            return self.getTypedRuleContext(MT22Parser.VariabledeclsContext,0)


        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def EQU(self):
            return self.getToken(MT22Parser.EQU, 0)

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variabledecls




    def variabledecls(self):

        localctx = MT22Parser.VariabledeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_variabledecls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 396
                self.match(MT22Parser.ID)
                self.state = 397
                self.match(MT22Parser.COMA)
                self.state = 398
                self.variabledecls()
                self.state = 399
                self.match(MT22Parser.COMA)
                self.state = 400
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 402
                self.match(MT22Parser.ID)
                self.state = 403
                self.match(MT22Parser.COL)
                self.state = 404
                self.vartype()
                self.state = 405
                self.match(MT22Parser.EQU)
                self.state = 406
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 408
                self.idlist()
                self.state = 409
                self.match(MT22Parser.COL)
                self.state = 410
                self.vartype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctiondeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionprot(self):
            return self.getTypedRuleContext(MT22Parser.FunctionprotContext,0)


        def functionbody(self):
            return self.getTypedRuleContext(MT22Parser.FunctionbodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functiondecl




    def functiondecl(self):

        localctx = MT22Parser.FunctiondeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_functiondecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.functionprot()
            self.state = 415
            self.functionbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainfunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionmainprot(self):
            return self.getTypedRuleContext(MT22Parser.FunctionmainprotContext,0)


        def functionbody(self):
            return self.getTypedRuleContext(MT22Parser.FunctionbodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_mainfunction




    def mainfunction(self):

        localctx = MT22Parser.MainfunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_mainfunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.functionmainprot()
            self.state = 418
            self.functionbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def demention(self):
            return self.getTypedRuleContext(MT22Parser.DementionContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraytype




    def arraytype(self):

        localctx = MT22Parser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_arraytype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(MT22Parser.ARRAY)
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.LSB:
                self.state = 421
                self.match(MT22Parser.LSB)
                self.state = 422
                self.demention()
                self.state = 423
                self.match(MT22Parser.RSB)
                self.state = 424
                self.match(MT22Parser.OF)
                self.state = 425
                self.vartype()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functiondecl(self):
            return self.getTypedRuleContext(MT22Parser.FunctiondeclContext,0)


        def variabledecls(self):
            return self.getTypedRuleContext(MT22Parser.VariabledeclsContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def statementlist(self):
            return self.getTypedRuleContext(MT22Parser.StatementlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_decl)
        try:
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.functiondecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.variabledecls()
                self.state = 431
                self.match(MT22Parser.SEM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 433
                self.expressionlist()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 434
                self.statementlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.condexpression_sempred
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condexpression_sempred(self, localctx:CondexpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




