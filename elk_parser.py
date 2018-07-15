import lark

parser = lark.Lark(r"""
    block: [statement (/[;\n\f\r]+/ statement)*]

    name: /[a-zA-Z_]\w*/

    variable: name
    type: name

    statement: variable ":=" value
        | variable ":" type ":=" value

    value: dict
         | set
         | list
         | string
         | number
         | bool
         | null
    
    null: "Null"

    ws: /[ \t]+/

    string: ESCAPED_STRING

    number: SIGNED_NUMBER

    list : "[" [value ("," value)*] "]"

    set : "{" [value ("," value)*] "}"

    dict : "{" [pair ("," pair)*] "}"

    bool: "True" -> true
        | "False" -> false

    pair : value ":" value

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='block')
