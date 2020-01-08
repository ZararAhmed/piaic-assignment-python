import numpy, scipy, os
#############################
# Datatypes, variables, operations, Operator Precedence
"""
/*
This is supposed to be a multiline comment
But, it isn't if you remove the quotes above and below
*/
"""

# This is a function
def sum(a,b):
    return a + b    # operation with operator: +
"""
Calling the function
and printing the values
"""
print(sum(2,13123)) #passing operands as arguments

# PEMDAS - Parantheses, Exponent, Multiplication, Division, Addition, Subtraction
print(8 * 7 + 3 / 2 - 4)

a = "7"
b = 20.7
c = True
# List
#       0   1      2 
d = ["assa",34, True ]
#      -3   -2   -1
# Tuple
#       0   1      2 
e = ("assa",34, True, 34 )
#      -3   -2   -1  
# Set
#       0   1      2 
f = {"assa",34, True, 34 }
#      -3   -2   -1  

print('\n---------\n')
print(id(a))
print(a)
print(type(a), '\n---------\n')

print(b)
print(id(b))
print(type(b), '\n---------\n')

print(c)
print(id(c))
print(type(c), '\n---------\n')

print(d)
print(id(d))
print(type(d), '\n---------\n')

print(e)
print(id(e))
print(type(e), '\n---------\n')
print("Second value on list e", e[3],"")

print(f)
print(id(f))
print(type(f), '\n---------\n')

# typecasting
f = list(f)
print(f)
print(id(f))
print(type(f), '\n---------\n')
print("Second value on list f", f[1],"")


