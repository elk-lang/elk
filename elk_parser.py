from lark import Lark

parser = Lark(r"""
    block: [statement (seperator statement)*]

    seperator: /[;\n\f\r]+/

    name: /[a-zA-Z_]\w*/
    
    type: "Number"
        | "String"
        | "Boolean"
        | "Nothing"

    statement: name ":=" value
        | name ":" type ":=" value

    ?value: dict
         | set
         | list
         | string
         | number
         | boolean
         | nothing
    
    nothing: "Nothing"

    ws: /[ \t]+/

    string: ESCAPED_STRING

    number: SIGNED_NUMBER

    list : "[" [value ("," value)*] "]"

    set : "{" [value ("," value)*] "}"

    dict : "{" [pair ("," pair)*] "}"

    boolean: "True" -> true
        | "False" -> false

    pair : value ":" value

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='block')
