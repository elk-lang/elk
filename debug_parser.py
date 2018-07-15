from elk_parser import parser
from elk_interpreter import Interpreter

text = """
    a := 3
    b : Number := 2
    c : String := "hello world"; d := {"text", "arrow"}"""

print(parser.parse(text))
print(parser.parse(text).pretty())
print(Interpreter().transform(parser.parse(text)))