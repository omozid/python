"""
A list is a collection of items in a particular order. You can make a list that
includes the letters of the alphabet, the digits from 0–9, or the names of
all the people in your family. You can put anything you want into a list, and
the items in your list don’t have to be related in any particular way. Because
a list usually contains more than one element, it’s a good idea to make the
name of your list plural, such as letters, digits, or names.
In Python, square brackets ([]) indicate a list, and individual elements
in the list are separated by commas. Here’s a simple example of a list that
contains a few kinds of bicycles:
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)


"""
Lists are ordered collections, so you can access any element in a list by
telling Python the position, or index, of the item desired. To access an element in a list, write the name of the list followed by the index of the item
enclosed in square brackets.
For example, let’s pull out the first bicycle in the list bicycles: 
"""
"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print(bicycles[0])


"""
You can also use the string methods from Day 3(02-variable) on any element
in this list. For example, you can format the element 'trek' more neatly by
using the title() method:

"""
"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print(bicycles[0].title())


"""
Index Positions Start at 0, Not 1
Python considers the first item in a list to be at position 0, not position 1.
This is true of most programming languages, and the reason has to do with
how the list operations are implemented at a lower level. If you’re receiving
unexpected results, determine whether you are making a simple off-by-one
error.
The second item in a list has an index of 1. Using this counting system, you can get any element you want from a list by subtracting one from
its position in the list. For instance, to access the fourth item in a list, you
request the item at index 3.
The following asks for the bicycles at index 1 and index 3:
"""
"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print(bicycles[1])
# print(bicycles[3])


"""
Python has a special syntax for accessing the last element in a list. 
By asking for the item at index -1, Python always returns the last item in the list:
"""
"""uncomment the print example i.e. remove the # or press ctr+/:"""
# print(bicycles[-1])

cities = ["Goteborg", "stockholm", "Malmo"]

"Modifying Elements in a List"
# print(cities[0])
# print(cities[-2].title())
# print(cities[2])
# cities[0] = "Uppsala"
# print(cities[0])


"""
Appending Elements to the End of a List:
The simplest way to add a new element to a list is to append the item to the
list. When you append an item to a list, the new element is added to the end
of the list.
"""
# cities.append("Uppsala")
# print(cities)


"""
The append() method makes it easy to build lists dynamically. For
example, you can start with an empty list and then add items to the list
using a series of append() calls.
"""
motorcycles = []
motorcycles.append('volvo')
motorcycles.append('bmw')
motorcycles.append('mercedez')

# print(motorcycles)


"""
Building lists this way is very common, because you often won’t know
the data your users want to store in a program until after the program is
running. To put your users in control, start by defining an empty list that
will hold the users’ values. Then append each new value provided to the list
you just created.

Inserting Elements into a List
You can add a new element at any position in your list by using the insert()
method. You do this by specifying the index of the new element and the
value of the new item.
"""
# cities.insert(1, "Uppsala")
# print(cities)

"""
Removing Elements from a List:
Often, you’ll want to remove an item or a set of items from a list.

Removing an Item Using the del Statement
If you know the position of the item you want to remove from a list, you can
use the del statement.

The code below uses del to remove the first item, from the list of
cities:
"""
# del cities[0]
# print(cities)


"""
Removing an Item Using the pop() Method:
Sometimes you’ll want to use the value of an item after you remove it from a
list.

The pop() method removes the last item in a list, but it lets you work
with that item after removing it. The term pop comes from thinking of a
list as a stack of items and popping one item off the top of the stack.
"""
# cities.pop()
# print(cities)
"""Popping Items from any Position in a List"""
first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")


"""
Removing an Item by Value:
Sometimes you won’t know the position of the value you want to remove
from a list. If you only know the value of the item you want to remove, you
can use the remove() method.
"""
cities.remove("stockholm")

"""
Organizing a List:
Often, your lists will be created in an unpredictable order, because you can’t
always control the order in which your users provide their data. Although
this is unavoidable in most circumstances, you’ll frequently want to present
your information in a particular order. Sometimes you’ll want to preserve the
original order of your list, and other times you’ll want to change the original order. Python provides a number of different ways to organize your lists,
depending on the situation

1. Python’s sort() method makes it relatively easy to sort a list
2. Python’s sorted() function lets you display your list in a particular order but doesn’t affect the actual order of the list.
3. Python’s reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same
   list a second time.
4. Python’s len() is used to identify the number of items in a list
"""
cars = ['bmw', 'audi', 'tesla', 'volvo']
"1.Python’s sort()"
# cities.sort()
# print(cities)

# cities.sort(reverse=True)
# print(cities)

"2. Python’s sorted()"
# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)

"3. Python’s reverse()"
# print(cars)
# cars.reverse()
# print(cars)

"4. Python’s len()"
# print(len(cities))
# print(cities)