"""
Numbers are used quite often in programming to keep score in games,
represent data in visualizations, store information in web applications,
and so on. Python treats numbers in several different ways, depending on
how they’re being used. Let’s first look at how Python manages integers,
because they’re the simplest to work with.
"""
# Integers
integer_example_1 :int = 3
integer_example_2 :int = 6
binary_example_1 :int = 100
binary_example_2 :int = 524850
"""You can add (+), subtract (-), multiply (*), and divide (/) integers in Python. """
substract = integer_example_2 - integer_example_1
addition = integer_example_2 + binary_example_2
multiplication = binary_example_1 * integer_example_1
division = integer_example_2 / integer_example_1
"""uncomment the print example i.e. remove the # or press ctr+/:"""
print(substract)
# print(addition)
# print(multiplication)
# print(division)

"""Python uses two multiplication symbols to represent exponents"""
exponents = integer_example_2 ** integer_example_2
"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print(exponents)

"""
Python supports the order of operations too, so you can use multiple
operations in one expression. You can also use parentheses to modify the
order of operations so Python can evaluate your expression in the order
you specify
"""
integer_new_example_1 = 2
integer_new_example_2 = 3
integer_new_example_3 = 4

bodmas_expression_1 = integer_new_example_1 + integer_new_example_2*integer_new_example_3
bodmas_expression_2 = (integer_new_example_1 + integer_new_example_2) * integer_new_example_3
"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print(bodmas_expression_1)
# print(bodmas_expression_2)

"""
The spacing in these examples above has no effect on how Python evaluates
the expressions; it simply helps you more quickly spot the operations that
have priority when you’re reading through the code.
"""