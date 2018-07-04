### if else statements:

--oneliner 

a := if a + 5 > b -> return a + 5 else - > return a

--blocks

if a = 5 -> 
  a = a + 4,
  return a
else -> return 0  -- note that new line is optional. 

### functions

function_name := x -> return x * x  

-- again new line/indent is optional. statement under a block can be specified by simply adding comma at the end of statement

function_name := x ->   
x = x * x,
return x
 
function_name := x, y -> return x * y

