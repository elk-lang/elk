# Elk Syntax Brainstorming
This is incomplete and will be expanded upon and changed heavily as the language develops
The goals for the language style in order of importance:
* Pleasant and easy to read 
* Not likely to be misinterpreted when reading
* Quick to write
* Easy for human to spot syntax errors in code
* Simple to parse

### Assignment
Types are optional, inferred if not specified
```
a := 5
b : int := 10
c := "hello"
c : str := "hello"
array := []
array : int [] := [1, 2, 3]
map := {}
map : str,int {} := {"a":1, "b":2}
```

### Comment
Haven't decided how to do block comments yet, something like Lua or Haskell style
```
-- single line comment
```

### Function
Argument types are optional - inferred if not specified
```
square := x -> x*x
-- {} blocks result in value that is returned, assuming they aren't structs
square2 := x : int -> {
    return x*x
}

c := square(10.0) -- results in 100.0
d := square2(10.0) -- type error

helloworld -> return "hello world" -- convention for if no argument needed


```

### If statement
```
x := if (a > 3) -> b else -> c -- single-line if (i.e. ternary operator)
fib := n -> if (n <= 1) -> 1 else -> fib(n-1) + fib(n-2) -- in function
-- using blocks
fib2 := n -> {
    if (n <= 1) -> {
        return 1
    } else -> {
        return fib(n-1) + fib(n-2)
    }
}
```

### For loop
```
for x in 0..9 -> print x
for x in 0..1..9 -> print x --basically the middle argument indicates the amount of increment of each step in the loop
```

### While loop
```
while i < 5 => i = i + 1
    
```

### Object
```
class book => 
    self :=title => -- for constructor
        my.title := title, my.owned = True 
    getTitle => return title
    





```
    
