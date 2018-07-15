from elk_parser import parser

text = """
    a := 3
    b : int := 2
    c : string := "hello world"; d := {"text", "arrow"}"""

print(parser.parse(text).pretty())