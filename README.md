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


# Special Sequences
A special sequence is a / followed by one of the charecters in the list below, 
and has a special meaning:

    Charecter       Description                                                   Example 
    \A              Returns a match if the specified                                "\AThe"
                    charecters are at the beginning of 
                    the string

    \b              Returns a match where the                                       r"\bain"
                    Specified charecters are at the                                 r"ain\b"
                    beginning or at the end of a word
                    (the "r" in the beginning is 
                    making sure that the string is 
                    being treated as a "raw string")   

    \B              Returns a match where the 
                    specified charecters are present,
                    but NOT at the beginning(or at
                    the end) of a word
                    (the "r" in the beginning is 
                    making sure that the string is 
                    being treated as a "raw string")  

    \d              Returns a match where the string                                 "\d"
                    contains digit (numbers from 0-9)                                 

    \D              Returns a match where the string                                 "\D"
                    DOES NOT contain digit

    \s              Returns a match where the string                                 "\s"
                    contains a white  space charecter

    \S              Returns a match where the string                                  "\S"
                    DOES NOT contain a white  space charecter                           

    \w              Returns a match where the string                                   "\w"
                    contains any word charecters 
                    (charecters from a to Z, digits
                    from 0-9, and the underscore_charecter)                

    \W              Returns a match where the string                                   "\W"
                    DOES NOT contain any word
                    charecters

    \Z              Returns a match if the specified                                    "Spain\Z"
                    charecters are at the end of the 
                    string     
                    


# Sets
A set is a set of charecters inside a pair of square brackets [] with a special meaning:

    Set         Description

    [arn]       Returns a match where one of the specified
                charecters(a, r or n) is present

    [a-n]       Returns a match for any lower case charecter,
                alphabetically  between a and n

    [^arn]      Returns a match for any charecter EXCEPT a, r, and n

    [0123]      Returns a match where any of the specified digits 
                (0, 1, 2, or 3) are present

    [0-9]       Returns a match for any digit between 0 and 9

    [0-5][0-9]  Returns a match for any two-digit numbers from
                00 and 59

    [a-zA-Z]    Returns a match for any charecter alphabetically 
                between a and z, lower case OR upper case

    [+]         In sets, +, *, ., |, (),$, {} has no special
                meaning, so[+] means: return a match for any 
                + charecter in the string


# The findall() Function
The findall() function returns a list containg all matches.

Example:

Print a list of all matches:

    import re

    txt = "The rain  in Spain"
    x = re.findall("ai", txt)
    print(x)

The list contains the matches in the order they are found.
If no matches are found, and empty list is returned:

Example:

Return an empty lit if no match was found:

    import re

    txt = "The rain in Spain"
    x = re.findall("Portugal", txt)
    print(x)

# The search() Function
The search() function searches the string for a match, and returns a Match 
object if there is a match.

If there is moe than one match, only the first occurence of the match will be 
returned:

Example:

Search for the first white-space charecter in the string:

    import re

    txt = "The rain in Spain"
    x = re.search("\s", txt)

    print("The first white-space charecter is located in position:",x.start())


If no matches are found, the value None is returned:

Example:

Make search that returns no match:

    import re

    txt = "The rain in  Spain"
    x = re.search("Portugal", txt)
    print(x)

# The split() Function
The split() function returns a list where the string has been split at each 
match:

Example:

Split at each white-space charecter:

    import re

    txt = "The rain  in Spain"
    x = re.split("\s", txt)
    print(x)

You can control the number of occurences by specifying the maxsplit
parameter:

Example:

Split the string only at the first occurence:

    import re

    txt = "The rain in  Spain"
    x = re.split("\s", txt, 1)
    print(x)

