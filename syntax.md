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
```

### If statement
```
x := if (a > 3) => b else => c -- single-line if (i.e. ternary operator)
fib := n -> if (n <= 1) => 1 else => fib(n-1) + fib(n-2) -- in function
-- using blocks
fib2 := n -> {
    if (n <= 1) => {
        return 1
    } else => {
        return fib(n-1) + fib(n-2)
    }
}
```
