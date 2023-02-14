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

# RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

    Function        Description
    findall         Returns a list containing all matches
    search          Returns a Match object if there is a match anywhere in the string
    split           Returns a list where the string has been split at each match
    sub             Replaces one or many matches with a string


# Metacharecters 
Metacharecters are charecters with a special meaning:

    Charecter       Description                                      Example
    []              A set of charecters                              "[a-m]"    

    /               Signals a special sequence(can                     "\d"   
                    also be used to escap special charecters)   

    .               Any charecter (except newline                     "he..O"  
                    charecter)   

    ^               Starts with                                       "^hello"

    $               Ends with                                          "planet$"

    *               Zero or more occurences                             "he.*o"

    +               One more occurences                                 "he.?o"

    ?               Zero or one occurences                              "he.+o"

    {}              Exactly the specified number of occurences           "he.{2}o"

    |               Either or                                             "falls|stays"

    ()              Capture and Group                                                                                     
