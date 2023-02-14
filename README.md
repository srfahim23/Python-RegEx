# Python-RegEx
A RegEx, or Regular Expression, is a sequence of charecters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

    import re

# RegEx in Python
When you have imported the re, you can start using regular expressions:

Example:

Search the string to see if it starts with "The" and ends with "Spain":

    import re

    txt = "The rain in Spain"

    x = re.search("^The.*Spain$", txt)

    if x:
        print("YES! We have a match!")
    else:
        print("No match")    

