from lark import Transformer

class Interpreter(Transformer):
    list = list
    pair = tuple
    dict = dict
    set = set
    def number(self, args):
        return float(args[0])
    def name(self, args):
        return str(args[0])
    def string(self, args):
        return args[0][1:-1]
    def boolean(self, args):
        return args[0]
    def seperator(self, args):
        return None
    def statement(self, args):
        return (args[0], args[-1])
    def block(self, args):
        return dict([pair for pair in args if pair])
    nothing = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False
