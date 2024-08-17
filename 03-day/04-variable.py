"""
Python calls any number with a decimal point a float. This term is used
in most programming languages, and it refers to the fact that a decimal
point can appear at any position in a number. Every programming language must be carefully designed to properly manage decimal numbers
so numbers behave appropriately no matter where the decimal point
appears.
"""
# floats
float_example_1 :float = 0.1
float_example_2 :float = 0.2
"""You can add (+), subtract (-), and multiply (*) floats in Python.
But be aware that you can sometimes get an arbitrary number of decimal places in your answer:
 """
substract = float_example_2 - float_example_1
addition = float_example_2 + float_example_1
multiplication = float_example_2 * float_example_1
"""uncomment the print example i.e. remove the # or press ctr+/:"""
print(substract)
# print(addition)
# print(multiplication)

"""
When you divide any two numbers, even if they are integers that result in a
whole number, you’ll always get a float:
"""
integer_example_1 :int = 2
integer_example_2 :int = 4
division = integer_example_2 / integer_example_1
"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print(division)

"""
If you mix an integer and a float in any other operation, you’ll get a
float as well:
"""
mix_addition = integer_example_1 + float_example_1
"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print(mix_addition)
