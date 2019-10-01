# Broad but simple description of data types and data structures for mandatory assignment 1


print("Hello Claus! This is my presentation on the first mandatory assignment in Python!\n-----")


# Method to explain strings
def simple_types():
    print("\n-----\nSTRINGS:\n-----\n")

    string1 = "Hello Claus. "
    print(type(string1))
    string2 = "I just concatenated two strings!"
    string3 = string1 + string2  # Concatenation
    print(string3)
    print("Here's the length of that string: " + str(len(string3)))  # Length checking
    print("I can also print out part of a string - like your name: " + string1[6:11])  # String slicing
    print("Or I can print the string backwards: " + string3[::-1])
    print(".. How about every second letter in 'concatenated'?: " + string2[7:19:3])  # String slicing with stride
    print("I can also check if something is in a string - let's check for your name: ", end='')
    print("Claus" in string1)  # Using the 'in' keyword (boolean return)
    print("Let's check for my name: ", end='')
    print("Henrik" in string1)
    print("We can also play around with f-strings:")
    a = 4
    b = 5
    print(f"{a} times {b} is 20!")  # Printing f-strings (Formatted String Literal)
    print("You can change strings by overwriting them (because they're mutable), but changing specific chars is hard: ")
    print("\"s[3] = 'x'\" would cause an error, but \"s = s[:3] + 'x' + s[4:]\" would work:")
    s = "Hello World!"
    print(s)
    s = s[:3] + 'x' + s[4:]
    print(s)
    # .count() .upper() .lower() .find() .isalnum() .isalpha() .isdigit() ???

    print("\n-----\nBOOLEANS:\n-----\n")

    bool1 = True
    print(type(bool1))
    print("Booleans return either true or false.")
    print("Is 2 + 2 = 4: " + str(2 + 2 == 4))
    print("Is 2 - 2 = 4: " + str(2 - 2 == 4))
    print("Booleans are used to assert results in conditional statements, and execute the relevant code.")

    print("\n-----\nNUMBERS:\n-----\n")

    num1 = 1
    print(type(num1))
    print("Integers (whole numbers) are commonly used in programming.")
    num2 = 4.2
    print(type(num2))
    print("Floating point numbers (decimal numbers) have their own data type (float).", end='')
    num2 = 4.2e7
    print("They can also be defined with scientific notation (4.2e7): ", end='')
    print(num2)
    num3 = 2+3j
    print(type(num3))
    print("Complex numbers (like 2+3j) are specified as (real number)+(imaginary number)")

    print("\n-----\nARITHMETIC OPERATORS:\n-----\n")

    a = 8
    b = 5
    print("Examples of the primary arithmetic operators:")
    print("8 + 5 = " + str(a + b))
    print("8 - 5 = " + str(a - b))
    print("8 * 5 = " + str(a * b))
    print("8 / 5 = " + str(a / b))
    print("8 % 5 = " + str(a % b))


# Method to explain lists
def lists():
    print("\n-----\nLISTS:\n-----\n")
    print("Lists can contain elements of any type, and is not restricted to containing elements of a single type:")
    list1 = [1, 2, "345", True, (1, 2, 3)]
    print(list1)
    print("Lists are ordered, and elements can therefore be accessed by their index - let's get the third element:")
    print(list1[2])  # Zero-based, obviously
    print("Lists can also be nested - yes, even lists in lists:")
    list2 = [1, 2, 3, [4, 5, 6], 7, 8, 9]
    print(list2)
    print("We can also change an element in our list, because lists as a type is mutable:")
    list2[2] = "Hej Claus!"
    print(list2)
    print(".. Or even change multiple elements in the list at once:")
    list2[3][0:2] = ["Let's", "try", "this"]
    print(list2)
    print("Because lists are dynamic, we can also just remove elements, and the list remains:")
    del list2[0]
    print(list2)
    list2[3:5] = []
    print(list2)


# Method to explain tuples
def tuples():
    print("\n-----\nTUPLES:\n-----\n")

    print("Tuples are much like lists, and can contain elements of multiple types")
    tuple1 = (1, 2, 3, "Hej", "med", "dig", True, None, ["Og", "en", "liste"])
    print(tuple1)
    print("However, a tuple can not be modified in any way - it is immutable")
    print("tuple1[0] = \"Test\" would cause a TypeError")


# Method to explain sets
def sets():
    print("\n-----\nSETS:\n-----\n")

    print("Sets can only contain unique elements, and are unordered")
    set1 = {1, 2, 3, "4", "5", "6", 6, 7, 8, 8}
    print(set1)
    print("The set itself is mutable, but the elements are immutable:")
    set1.update([9, ("Hello", "World!")])
    print(set1)
    set1.add("Woohoo!")
    print(set1)
    print("set1.update([[1, 2]]) returns a TypeError - lists and dicts can not be added to sets are they are mutable!")
    print("We can also perform certain methods on multiple sets, e.g. to see what they have in common: ")
    set2 = {1, 2, 3, 10, 11, 12}
    print(set1 & set2)
    print(".. Or their union (all unique elements from both sets put together: ")
    print(set1 | set2)
    print(".. Or subtract elements from one set from another!")
    print(set1 - set2)
    print("Or their symmetric difference - meaning all elements that is present in only one of the sets but not both:")
    print(set1 ^ set2)
    # pop() remove() discard() clear()
    # Frozen sets immutable (only non-modifying methods)


# Method to explain dicts
def dicts():
    print("\n-----\nDICTS:\n-----\n")

    # Mutable
    # Dynamic
    # Nested
    # Dictionaries are accessed via keys, not indexing by position
    print("Dictionaries is a data structure that contains key-value pairs:")
    dict1 = {
        1: "Hello ",
        2: "World! ",
        3: "This ",
        4: "is ",
        5: "a ",
        6: "dictionary!"
    }
    print(dict1)
    print("To access the value in a dict, you specify the key - whereas in lists you reference the position (indexing)")
    print(dict1[1])
    print("Dictionaries cannot return a slice value, so \"dict1[1:2]\" would return a TypeError!")
    print("We can also add to our dict (e.g. \"dict1[7] = \"Test\"): ")
    dict1[7] = "Test"
    print(dict1)
    print(dict1[7])
    print("There are few restrictions on dicts - keys have to be unique (but new values can be assigned to a key):")
    dict1[7] = "New value here!"
    print(dict1)
    print("Furthermore, a dict key has to be immutable - numbers, strings, booleans, or even tuples can be used as key")
    print("Lists or another dictionary can not be used, as they are mutable")
    # clear() (empties dict), get() (retrieves value for a given key), items() (returns a list of key-value pairs)
    # keys() (returns a list of keys), values() (returns a list of values), pop() (removes a key and returns its value)


# Did not include special types / JSON as of yet
# Run methods
simple_types()
lists()
tuples()
sets()
dicts()
