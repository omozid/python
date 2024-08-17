"""
The boolean type variable is either True (1) or False (0)
"""

x: bool = True
y: bool = False

if x:
    print("This should print!!")
if y: 
    print("This would not print")
if x and y:
    print("This will not print as wel: Logic gate of 1 AND 0 = 0")
if x or y:
    print("This will print: Logic gate of 1 OR 0 = 1")