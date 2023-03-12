# Generated from f:\Univercity\S2 Y3\PRINCIPLES OF PROGRAMMING LANGUAGES\Assignment\assignment2\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u021c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\2\7\2\u009c\n\2\f\2\16\2\u009f\13\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u00aa\n\3\f\3\16\3\u00ad")
        buf.write("\13\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u00b5\n\4\3\5\3\5\5")
        buf.write("\5\u00b9\n\5\3\6\3\6\7\6\u00bd\n\6\f\6\16\6\u00c0\13\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\5\34\u013f")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\6\37\u014d\n\37\r\37\16\37\u014e\3 \3 \5 \u0153")
        buf.write("\n \3 \6 \u0156\n \r \16 \u0157\3!\3!\6!\u015c\n!\r!\16")
        buf.write("!\u015d\3!\3!\3!\5!\u0163\n!\3!\3!\6!\u0167\n!\r!\16!")
        buf.write("\u0168\3!\5!\u016c\n!\3!\3!\3!\3!\3!\3!\5!\u0174\n!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3\"\7\"\u017d\n\"\f\"\16\"\u0180")
        buf.write("\13\"\3#\3#\5#\u0184\n#\3#\3#\3$\3$\3%\5%\u018b\n%\3&")
        buf.write("\3&\5&\u018f\n&\3&\3&\3&\7&\u0194\n&\f&\16&\u0197\13&")
        buf.write("\3\'\3\'\3\'\3\'\3\'\5\'\u019e\n\'\3(\3(\7(\u01a2\n(\f")
        buf.write("(\16(\u01a5\13(\3(\3(\7(\u01a9\n(\f(\16(\u01ac\13(\3(")
        buf.write("\3(\3(\5(\u01b1\n(\3)\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3@\3A\3")
        buf.write("A\3A\3B\3B\3C\3C\3C\3D\3D\3E\3E\3E\3F\3F\3F\3G\6G\u01f9")
        buf.write("\nG\rG\16G\u01fa\3G\3G\3H\3H\3H\3I\3I\3I\5I\u0205\nI\3")
        buf.write("J\3J\7J\u0209\nJ\fJ\16J\u020c\13J\3J\5J\u020f\nJ\3J\3")
        buf.write("J\3K\3K\7K\u0215\nK\fK\16K\u0218\13K\3K\3K\3K\3\u009d")
        buf.write("\2L\3\3\5\4\7\2\t\2\13\5\r\2\17\6\21\7\23\b\25\t\27\n")
        buf.write("\31\13\33\f\35\r\37\16!\17#\20%\21\'\22)\23+\24-\25/\26")
        buf.write("\61\27\63\30\65\31\67\329\33;\34=\2?\2A\35C\2E\36G\2I")
        buf.write("\2K\37M\2O\2Q S!U\"W#Y$[%]&_\'a(c)e*g+i,k-m.o/q\60s\61")
        buf.write("u\62w\63y\64{\65}\66\177\67\u00818\u00839\u0085:\u0087")
        buf.write(";\u0089<\u008b=\u008d>\u008f?\u0091\2\u0093@\u0095A\3")
        buf.write("\2\17\4\2\f\f\17\17\b\2))ddhhppttvv\4\2$$^^\7\2\f\f\17")
        buf.write("\17$$))^^\4\2GGgg\4\2--//\3\2\63;\3\2\62;\4\2C\\c|\5\2")
        buf.write("\13\f\17\17\"\"\n\2$$))^^ddhhppttvv\3\2^^\7\3\n\f\16\17")
        buf.write("$$))^^\2\u0234\2\3\3\2\2\2\2\5\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2A\3\2\2\2\2E\3\2\2\2\2K\3\2\2\2\2Q\3\2\2\2")
        buf.write("\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2")
        buf.write("\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2")
        buf.write("\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3")
        buf.write("\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y")
        buf.write("\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2")
        buf.write("\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\3\u0097\3\2\2")
        buf.write("\2\5\u00a5\3\2\2\2\7\u00b0\3\2\2\2\t\u00b8\3\2\2\2\13")
        buf.write("\u00ba\3\2\2\2\r\u00c5\3\2\2\2\17\u00c7\3\2\2\2\21\u00cc")
        buf.write("\3\2\2\2\23\u00d2\3\2\2\2\25\u00da\3\2\2\2\27\u00dd\3")
        buf.write("\2\2\2\31\u00e2\3\2\2\2\33\u00e8\3\2\2\2\35\u00ec\3\2")
        buf.write("\2\2\37\u00f5\3\2\2\2!\u00f8\3\2\2\2#\u0100\3\2\2\2%\u0107")
        buf.write("\3\2\2\2\'\u010e\3\2\2\2)\u0114\3\2\2\2+\u0119\3\2\2\2")
        buf.write("-\u011d\3\2\2\2/\u0126\3\2\2\2\61\u0129\3\2\2\2\63\u0131")
        buf.write("\3\2\2\2\65\u0137\3\2\2\2\67\u013e\3\2\2\29\u0140\3\2")
        buf.write("\2\2;\u0146\3\2\2\2=\u014c\3\2\2\2?\u0150\3\2\2\2A\u0173")
        buf.write("\3\2\2\2C\u0177\3\2\2\2E\u0183\3\2\2\2G\u0187\3\2\2\2")
        buf.write("I\u018a\3\2\2\2K\u018e\3\2\2\2M\u019d\3\2\2\2O\u01b0\3")
        buf.write("\2\2\2Q\u01b2\3\2\2\2S\u01b6\3\2\2\2U\u01b8\3\2\2\2W\u01ba")
        buf.write("\3\2\2\2Y\u01bc\3\2\2\2[\u01be\3\2\2\2]\u01c0\3\2\2\2")
        buf.write("_\u01c2\3\2\2\2a\u01c4\3\2\2\2c\u01c6\3\2\2\2e\u01c8\3")
        buf.write("\2\2\2g\u01ca\3\2\2\2i\u01cc\3\2\2\2k\u01ce\3\2\2\2m\u01d0")
        buf.write("\3\2\2\2o\u01d2\3\2\2\2q\u01d4\3\2\2\2s\u01d6\3\2\2\2")
        buf.write("u\u01d8\3\2\2\2w\u01da\3\2\2\2y\u01dc\3\2\2\2{\u01de\3")
        buf.write("\2\2\2}\u01e1\3\2\2\2\177\u01e4\3\2\2\2\u0081\u01e7\3")
        buf.write("\2\2\2\u0083\u01ea\3\2\2\2\u0085\u01ec\3\2\2\2\u0087\u01ef")
        buf.write("\3\2\2\2\u0089\u01f1\3\2\2\2\u008b\u01f4\3\2\2\2\u008d")
        buf.write("\u01f8\3\2\2\2\u008f\u01fe\3\2\2\2\u0091\u0204\3\2\2\2")
        buf.write("\u0093\u0206\3\2\2\2\u0095\u0212\3\2\2\2\u0097\u0098\7")
        buf.write("\61\2\2\u0098\u0099\7,\2\2\u0099\u009d\3\2\2\2\u009a\u009c")
        buf.write("\13\2\2\2\u009b\u009a\3\2\2\2\u009c\u009f\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a0\3\2\2\2")
        buf.write("\u009f\u009d\3\2\2\2\u00a0\u00a1\7,\2\2\u00a1\u00a2\7")
        buf.write("\61\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\b\2\2\2\u00a4")
        buf.write("\4\3\2\2\2\u00a5\u00a6\7\61\2\2\u00a6\u00a7\7\61\2\2\u00a7")
        buf.write("\u00ab\3\2\2\2\u00a8\u00aa\n\2\2\2\u00a9\u00a8\3\2\2\2")
        buf.write("\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3")
        buf.write("\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af")
        buf.write("\b\3\2\2\u00af\6\3\2\2\2\u00b0\u00b4\7^\2\2\u00b1\u00b5")
        buf.write("\t\3\2\2\u00b2\u00b5\5i\65\2\u00b3\u00b5\t\4\2\2\u00b4")
        buf.write("\u00b1\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2")
        buf.write("\u00b5\b\3\2\2\2\u00b6\u00b9\5\7\4\2\u00b7\u00b9\n\5\2")
        buf.write("\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\n\3\2")
        buf.write("\2\2\u00ba\u00be\5i\65\2\u00bb\u00bd\5\t\5\2\u00bc\u00bb")
        buf.write("\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00c1\3\2\2\2\u00c0\u00be\3\2\2\2")
        buf.write("\u00c1\u00c2\5i\65\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\b")
        buf.write("\6\3\2\u00c4\f\3\2\2\2\u00c5\u00c6\5\u008bF\2\u00c6\16")
        buf.write("\3\2\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\u00cb\7q\2\2\u00cb\20\3\2\2\2\u00cc\u00cd")
        buf.write("\7d\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0")
        buf.write("\7c\2\2\u00d0\u00d1\7m\2\2\u00d1\22\3\2\2\2\u00d2\u00d3")
        buf.write("\7d\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6")
        buf.write("\7n\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9")
        buf.write("\7p\2\2\u00d9\24\3\2\2\2\u00da\u00db\7f\2\2\u00db\u00dc")
        buf.write("\7q\2\2\u00dc\26\3\2\2\2\u00dd\u00de\7g\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1\7g\2\2\u00e1\30")
        buf.write("\3\2\2\2\u00e2\u00e3\7h\2\2\u00e3\u00e4\7n\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7\7v\2\2\u00e7\32")
        buf.write("\3\2\2\2\u00e8\u00e9\7h\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb\34\3\2\2\2\u00ec\u00ed\7h\2\2\u00ed\u00ee")
        buf.write("\7w\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7e\2\2\u00f0\u00f1")
        buf.write("\7v\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4")
        buf.write("\7p\2\2\u00f4\36\3\2\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7")
        buf.write("\7h\2\2\u00f7 \3\2\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa")
        buf.write("\7p\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd")
        buf.write("\7i\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7t\2\2\u00ff\"")
        buf.write("\3\2\2\2\u0100\u0101\7t\2\2\u0101\u0102\7g\2\2\u0102\u0103")
        buf.write("\7v\2\2\u0103\u0104\7w\2\2\u0104\u0105\7t\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106$\3\2\2\2\u0107\u0108\7u\2\2\u0108\u0109")
        buf.write("\7v\2\2\u0109\u010a\7t\2\2\u010a\u010b\7k\2\2\u010b\u010c")
        buf.write("\7p\2\2\u010c\u010d\7i\2\2\u010d&\3\2\2\2\u010e\u010f")
        buf.write("\7y\2\2\u010f\u0110\7j\2\2\u0110\u0111\7k\2\2\u0111\u0112")
        buf.write("\7n\2\2\u0112\u0113\7g\2\2\u0113(\3\2\2\2\u0114\u0115")
        buf.write("\7x\2\2\u0115\u0116\7q\2\2\u0116\u0117\7k\2\2\u0117\u0118")
        buf.write("\7f\2\2\u0118*\3\2\2\2\u0119\u011a\7q\2\2\u011a\u011b")
        buf.write("\7w\2\2\u011b\u011c\7v\2\2\u011c,\3\2\2\2\u011d\u011e")
        buf.write("\7e\2\2\u011e\u011f\7q\2\2\u011f\u0120\7p\2\2\u0120\u0121")
        buf.write("\7v\2\2\u0121\u0122\7k\2\2\u0122\u0123\7p\2\2\u0123\u0124")
        buf.write("\7w\2\2\u0124\u0125\7g\2\2\u0125.\3\2\2\2\u0126\u0127")
        buf.write("\7q\2\2\u0127\u0128\7h\2\2\u0128\60\3\2\2\2\u0129\u012a")
        buf.write("\7k\2\2\u012a\u012b\7p\2\2\u012b\u012c\7j\2\2\u012c\u012d")
        buf.write("\7g\2\2\u012d\u012e\7t\2\2\u012e\u012f\7k\2\2\u012f\u0130")
        buf.write("\7v\2\2\u0130\62\3\2\2\2\u0131\u0132\7c\2\2\u0132\u0133")
        buf.write("\7t\2\2\u0133\u0134\7t\2\2\u0134\u0135\7c\2\2\u0135\u0136")
        buf.write("\7{\2\2\u0136\64\3\2\2\2\u0137\u0138\7o\2\2\u0138\u0139")
        buf.write("\7c\2\2\u0139\u013a\7k\2\2\u013a\u013b\7p\2\2\u013b\66")
        buf.write("\3\2\2\2\u013c\u013f\59\35\2\u013d\u013f\5;\36\2\u013e")
        buf.write("\u013c\3\2\2\2\u013e\u013d\3\2\2\2\u013f8\3\2\2\2\u0140")
        buf.write("\u0141\7h\2\2\u0141\u0142\7c\2\2\u0142\u0143\7n\2\2\u0143")
        buf.write("\u0144\7u\2\2\u0144\u0145\7g\2\2\u0145:\3\2\2\2\u0146")
        buf.write("\u0147\7v\2\2\u0147\u0148\7t\2\2\u0148\u0149\7w\2\2\u0149")
        buf.write("\u014a\7g\2\2\u014a<\3\2\2\2\u014b\u014d\5G$\2\u014c\u014b")
        buf.write("\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014c\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f>\3\2\2\2\u0150\u0152\t\6\2\2\u0151")
        buf.write("\u0153\t\7\2\2\u0152\u0151\3\2\2\2\u0152\u0153\3\2\2\2")
        buf.write("\u0153\u0155\3\2\2\2\u0154\u0156\5G$\2\u0155\u0154\3\2")
        buf.write("\2\2\u0156\u0157\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158")
        buf.write("\3\2\2\2\u0158@\3\2\2\2\u0159\u015c\5C\"\2\u015a\u015c")
        buf.write("\5k\66\2\u015b\u0159\3\2\2\2\u015b\u015a\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e\u015f\3\2\2\2\u015f\u0160\5Y-\2\u0160\u0162\5=")
        buf.write("\37\2\u0161\u0163\5? \2\u0162\u0161\3\2\2\2\u0162\u0163")
        buf.write("\3\2\2\2\u0163\u0174\3\2\2\2\u0164\u0167\5C\"\2\u0165")
        buf.write("\u0167\5k\66\2\u0166\u0164\3\2\2\2\u0166\u0165\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3")
        buf.write("\2\2\2\u0169\u016b\3\2\2\2\u016a\u016c\5Y-\2\u016b\u016a")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u016e\5? \2\u016e\u0174\3\2\2\2\u016f\u0170\5Y-\2\u0170")
        buf.write("\u0171\5=\37\2\u0171\u0172\5? \2\u0172\u0174\3\2\2\2\u0173")
        buf.write("\u015b\3\2\2\2\u0173\u0166\3\2\2\2\u0173\u016f\3\2\2\2")
        buf.write("\u0174\u0175\3\2\2\2\u0175\u0176\b!\4\2\u0176B\3\2\2\2")
        buf.write("\u0177\u017e\t\b\2\2\u0178\u0179\5m\67\2\u0179\u017a\5")
        buf.write("G$\2\u017a\u017d\3\2\2\2\u017b\u017d\5G$\2\u017c\u0178")
        buf.write("\3\2\2\2\u017c\u017b\3\2\2\2\u017d\u0180\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017fD\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0181\u0184\5C\"\2\u0182\u0184\5k\66\2")
        buf.write("\u0183\u0181\3\2\2\2\u0183\u0182\3\2\2\2\u0184\u0185\3")
        buf.write("\2\2\2\u0185\u0186\b#\5\2\u0186F\3\2\2\2\u0187\u0188\t")
        buf.write("\t\2\2\u0188H\3\2\2\2\u0189\u018b\t\n\2\2\u018a\u0189")
        buf.write("\3\2\2\2\u018bJ\3\2\2\2\u018c\u018f\5I%\2\u018d\u018f")
        buf.write("\5m\67\2\u018e\u018c\3\2\2\2\u018e\u018d\3\2\2\2\u018f")
        buf.write("\u0195\3\2\2\2\u0190\u0194\5I%\2\u0191\u0194\5m\67\2\u0192")
        buf.write("\u0194\5G$\2\u0193\u0190\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write("\u0192\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2")
        buf.write("\u0195\u0196\3\2\2\2\u0196L\3\2\2\2\u0197\u0195\3\2\2")
        buf.write("\2\u0198\u019e\5\13\6\2\u0199\u019e\5A!\2\u019a\u019e")
        buf.write("\5E#\2\u019b\u019e\5\67\34\2\u019c\u019e\5K&\2\u019d\u0198")
        buf.write("\3\2\2\2\u019d\u0199\3\2\2\2\u019d\u019a\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019eN\3\2\2\2\u019f")
        buf.write("\u01a3\5M\'\2\u01a0\u01a2\7\"\2\2\u01a1\u01a0\3\2\2\2")
        buf.write("\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3")
        buf.write("\2\2\2\u01a4\u01a6\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01aa")
        buf.write("\5S*\2\u01a7\u01a9\7\"\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01ac")
        buf.write("\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab")
        buf.write("\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae\5O(\2\u01ae")
        buf.write("\u01b1\3\2\2\2\u01af\u01b1\5M\'\2\u01b0\u019f\3\2\2\2")
        buf.write("\u01b0\u01af\3\2\2\2\u01b1P\3\2\2\2\u01b2\u01b3\5c\62")
        buf.write("\2\u01b3\u01b4\5O(\2\u01b4\u01b5\5e\63\2\u01b5R\3\2\2")
        buf.write("\2\u01b6\u01b7\7.\2\2\u01b7T\3\2\2\2\u01b8\u01b9\7<\2")
        buf.write("\2\u01b9V\3\2\2\2\u01ba\u01bb\7=\2\2\u01bbX\3\2\2\2\u01bc")
        buf.write("\u01bd\7\60\2\2\u01bdZ\3\2\2\2\u01be\u01bf\7]\2\2\u01bf")
        buf.write("\\\3\2\2\2\u01c0\u01c1\7_\2\2\u01c1^\3\2\2\2\u01c2\u01c3")
        buf.write("\7*\2\2\u01c3`\3\2\2\2\u01c4\u01c5\7+\2\2\u01c5b\3\2\2")
        buf.write("\2\u01c6\u01c7\7}\2\2\u01c7d\3\2\2\2\u01c8\u01c9\7\177")
        buf.write("\2\2\u01c9f\3\2\2\2\u01ca\u01cb\7?\2\2\u01cbh\3\2\2\2")
        buf.write("\u01cc\u01cd\7$\2\2\u01cdj\3\2\2\2\u01ce\u01cf\7\62\2")
        buf.write("\2\u01cfl\3\2\2\2\u01d0\u01d1\7a\2\2\u01d1n\3\2\2\2\u01d2")
        buf.write("\u01d3\7-\2\2\u01d3p\3\2\2\2\u01d4\u01d5\7/\2\2\u01d5")
        buf.write("r\3\2\2\2\u01d6\u01d7\7,\2\2\u01d7t\3\2\2\2\u01d8\u01d9")
        buf.write("\7\61\2\2\u01d9v\3\2\2\2\u01da\u01db\7\'\2\2\u01dbx\3")
        buf.write("\2\2\2\u01dc\u01dd\7#\2\2\u01ddz\3\2\2\2\u01de\u01df\7")
        buf.write("(\2\2\u01df\u01e0\7(\2\2\u01e0|\3\2\2\2\u01e1\u01e2\7")
        buf.write("~\2\2\u01e2\u01e3\7~\2\2\u01e3~\3\2\2\2\u01e4\u01e5\7")
        buf.write("?\2\2\u01e5\u01e6\7?\2\2\u01e6\u0080\3\2\2\2\u01e7\u01e8")
        buf.write("\7#\2\2\u01e8\u01e9\7?\2\2\u01e9\u0082\3\2\2\2\u01ea\u01eb")
        buf.write("\7>\2\2\u01eb\u0084\3\2\2\2\u01ec\u01ed\7>\2\2\u01ed\u01ee")
        buf.write("\7?\2\2\u01ee\u0086\3\2\2\2\u01ef\u01f0\7@\2\2\u01f0\u0088")
        buf.write("\3\2\2\2\u01f1\u01f2\7@\2\2\u01f2\u01f3\7?\2\2\u01f3\u008a")
        buf.write("\3\2\2\2\u01f4\u01f5\7<\2\2\u01f5\u01f6\7<\2\2\u01f6\u008c")
        buf.write("\3\2\2\2\u01f7\u01f9\t\13\2\2\u01f8\u01f7\3\2\2\2\u01f9")
        buf.write("\u01fa\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2")
        buf.write("\u01fb\u01fc\3\2\2\2\u01fc\u01fd\bG\2\2\u01fd\u008e\3")
        buf.write("\2\2\2\u01fe\u01ff\13\2\2\2\u01ff\u0200\bH\6\2\u0200\u0090")
        buf.write("\3\2\2\2\u0201\u0202\7^\2\2\u0202\u0205\n\f\2\2\u0203")
        buf.write("\u0205\n\r\2\2\u0204\u0201\3\2\2\2\u0204\u0203\3\2\2\2")
        buf.write("\u0205\u0092\3\2\2\2\u0206\u020a\5i\65\2\u0207\u0209\5")
        buf.write("\t\5\2\u0208\u0207\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u0208")
        buf.write("\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020e\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020d\u020f\t\16\2\2\u020e\u020d\3\2\2")
        buf.write("\2\u020f\u0210\3\2\2\2\u0210\u0211\bJ\7\2\u0211\u0094")
        buf.write("\3\2\2\2\u0212\u0216\5i\65\2\u0213\u0215\5\t\5\2\u0214")
        buf.write("\u0213\3\2\2\2\u0215\u0218\3\2\2\2\u0216\u0214\3\2\2\2")
        buf.write("\u0216\u0217\3\2\2\2\u0217\u0219\3\2\2\2\u0218\u0216\3")
        buf.write("\2\2\2\u0219\u021a\5\u0091I\2\u021a\u021b\bK\b\2\u021b")
        buf.write("\u0096\3\2\2\2#\2\u009d\u00ab\u00b4\u00b8\u00be\u013e")
        buf.write("\u014e\u0152\u0157\u015b\u015d\u0162\u0166\u0168\u016b")
        buf.write("\u0173\u017c\u017e\u0183\u018a\u018e\u0193\u0195\u019d")
        buf.write("\u01a3\u01aa\u01b0\u01fa\u0204\u020a\u020e\u0216\t\b\2")
        buf.write("\2\3\6\2\3!\3\3#\4\3H\5\3J\6\3K\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_C = 1
    COMMENT_CPP = 2
    STR = 3
    AUTO = 4
    BREAK = 5
    BOOLEAN = 6
    DO = 7
    ELSE = 8
    FLOAT = 9
    FOR = 10
    FUNCTION = 11
    IF = 12
    INTEGER = 13
    RETURN = 14
    STRING = 15
    WHILE = 16
    VOID = 17
    OUT = 18
    CONTINUE = 19
    OF = 20
    INHERIT = 21
    ARRAY = 22
    MAIN = 23
    BOOL = 24
    FALSE = 25
    TRUE = 26
    FLO = 27
    INT = 28
    ID = 29
    ARR = 30
    COMA = 31
    COL = 32
    SEM = 33
    DOT = 34
    LSB = 35
    RSB = 36
    LB = 37
    RB = 38
    LCB = 39
    RCB = 40
    EQU = 41
    DB = 42
    ZERO = 43
    UNDE = 44
    PLUS = 45
    MINU = 46
    MUTI = 47
    DIVI = 48
    MODU = 49
    NOT = 50
    AND = 51
    OR = 52
    EQUL = 53
    NEQ = 54
    LESS = 55
    LOEQ = 56
    GREA = 57
    GOEQ = 58
    SCOPE = 59
    WS = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'main'", "'false'", "'true'", "','", "':'", "';'", 
            "'.'", "'['", "']'", "'('", "')'", "'{'", "'}'", "'='", "'\"'", 
            "'0'", "'_'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_C", "COMMENT_CPP", "STR", "AUTO", "BREAK", "BOOLEAN", 
            "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
            "STRING", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
            "ARRAY", "MAIN", "BOOL", "FALSE", "TRUE", "FLO", "INT", "ID", 
            "ARR", "COMA", "COL", "SEM", "DOT", "LSB", "RSB", "LB", "RB", 
            "LCB", "RCB", "EQU", "DB", "ZERO", "UNDE", "PLUS", "MINU", "MUTI", 
            "DIVI", "MODU", "NOT", "AND", "OR", "EQUL", "NEQ", "LESS", "LOEQ", 
            "GREA", "GOEQ", "SCOPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_C", "COMMENT_CPP", "ESCAPE", "STR_CHAR", "STR", 
                  "STRTYP", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                  "MAIN", "BOOL", "FALSE", "TRUE", "DECIMAL", "EXPONENT", 
                  "FLO", "POSINT", "INT", "DIGIT", "LETTER", "ID", "ARRTYPE", 
                  "ARRTYPES", "ARR", "COMA", "COL", "SEM", "DOT", "LSB", 
                  "RSB", "LB", "RB", "LCB", "RCB", "EQU", "DB", "ZERO", 
                  "UNDE", "PLUS", "MINU", "MUTI", "DIVI", "MODU", "NOT", 
                  "AND", "OR", "EQUL", "NEQ", "LESS", "LOEQ", "GREA", "GOEQ", 
                  "SCOPE", "WS", "ERROR_CHAR", "ESCAPE_ILLEGAL", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.STR_action 
            actions[31] = self.FLO_action 
            actions[33] = self.INT_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def FLO_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise IllegalEscape(self.text[1:])
     


