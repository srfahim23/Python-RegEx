# RegEx Module

# Import re
#Search the string to see if it starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")    

# The findall() Function
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Return an empty list if no match was found:
import re

txt = "The rain in Spain"

x = re.findall("Portugal", txt)
print(x)

if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")  


# Search for the first white-space charecter in the string:
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space charecter is located in position:", x.start())


# Make a search that returns no match:
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


#Splite at each white-space charecter:
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Split the string only at the first occurrence:
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# Replace every white-space charecter with the number 9:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Replace the first 2 occurrence
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#Do a search that will return a Match Object:
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  #this will print an object

#Print the  position (start-and end-position) of the first match occurence.
#The regular expression looks for any words that starts with an upper case "S":
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# Print the string passed into the function:
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


#Print the part of the string where there was a match.
# The regular expressoin looks for any words that starts with an upper case "S":
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

