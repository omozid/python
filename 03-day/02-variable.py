"""
A string is a series of characters. Anything inside quotes is considered
a string in Python, and you can use single or double quotes around your
strings like this:

"This is a string."
'This is also a string.'

"""
name = "ada lovelace"
print(name.title())

"""
Several other useful methods are available for dealing with case as
well. For example, you can change a string to all uppercase or all lowercase
letters by uncommenting the print example i.e. remove the # or press ctr+/:
"""
# print(name.upper())
# print(name.lower())


"""
In some situations, you’ll want to use a variable’s value inside a string. For
example, you might want two variables to represent a first name and a last
name respectively, and then want to combine those values to display someone’s full name:
"""

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print(full_name)


"""
To insert a variable’s value into a string, place the letter f immediately
before the opening quotation mark. Put braces around the name or names
of any variable you want to use inside the string. Python will replace each
variable with its value when the string is displayed.
These strings are called f-strings. The f is for format, because Python
formats the string by replacing the name of any variable in braces with its
value.
"""

"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print(f"Hello, {full_name.title()}!")


"""
You can also use f-strings to compose a message, and then assign the
entire message to a variable:
"""
message = f"Hello, {full_name.title()}!"
"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print(message)

# Good way of writing variable name
string: str = " charles barbage" or 'Jon Doe'
first_name: str = "Jon"
last_name: str = "Doe"


"""
In programming, whitespace refers to any nonprinting character, such as
spaces, tabs, and end-of-line symbols. You can use whitespace to organize
your output so it’s easier for users to read.
To add a tab to your text, use the character combination \t as shown below
"""

"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print("Languages:\nPython\nC\nJavaScript")


"""
Extra whitespace can be confusing in your programs. To programmers
'python' and 'python ' look pretty much the same. But to a program, they
are two different strings. Python detects the extra space in 'python ' and
considers it significant unless you tell it otherwise.

To remove the whitespace from the string, you strip the whitespace
from the right side of the string and then associate this new value with the
original variable, as shown below

You can also strip whitespace from the left side of a string using the
lstrip() method, or from both sides at once using strip():
"""
favorite_language = ' python ' 
favorite_language.rstrip()
# favorite_language.lstrip()
# favorite_language.strip()
"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print(favorite_language)