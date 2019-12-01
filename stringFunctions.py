my_name = "i åm A PIAIC Student"

# print list of all functions available for variable "name"
#print(dir(name))    # Since the variable "name" is a string type, this function shows all functions available for string types   

# Below is a list of all the functions available for string types along with their implementations


# Template
# <Function No>. <Function Name>
# Implementation

#"In-place" function i.e does not change the value of the original variable
#"In-memory" function i.e changes the value of the original variable

# 1. capitalize     in-place - Capitalizes only the first character of the whole string and keeps all other characters small
new_name = my_name.capitalize()    
print("Capitalized: " + new_name + "\n")

# 2. casefold       in-place - Converts whole string into lower case
new_name = my_name.casefold()    
print("Casefolded (All Small Letters): "+ new_name + "\n")

# 3. center         in-place - Center the string in a specified space
new_name = my_name.center(30)       # Take space of 40 chacacters and center the string in it. Leaving 5 spaces on each side
print("Centralized in 30 characters: "+ new_name + "\n")

# 4. count          in-place - Count the number of times a specified value occurs in the string (Case-sensitive)
new_name = my_name.count('I')       # Count the number of times capital letter 'I' is in the string        
print("Count of Capital \"I\" in the string: "+ str(new_name) + "\n")

# 5. encode         in-place - Returns an encoded version of the string
new_name = my_name.encode()
print("Encoded string: "+str(new_name) + "\n")

# 6. endswith       in-place - Returns true if the string ends with the specified value
new_name = my_name.endswith('t')
print("The given string ends with t: " + str(new_name))
new_name = my_name.endswith('a')
print("The given string ends with a: " + str(new_name) + "\n")

# 7. expandtabs     in-place - Sets the tab size of the string
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
# 8. find           in-place - Searches the string for a specified value and returns the position of where it was found
# 9. format         in-place - Formats specified values in a string
# 10. format_map    in-place - Formats specified values in a string
# 11. index         in-place - Searches the string for a specified value and returns the position of where it was found
# 12. isalnum       in-place - Returns True if all characters in the string are alphanumeric
# 13. isalpha       in-place - Returns True if all characters in the string are in the alphabet
# 14. isascii       in-place - Returns True if all characters in the string are ascii
# 15. isdecimal     in-place - Returns True if all characters in the string are decimals
# 16. isdigit       in-place - Returns True if all characters in the string are digits
# 17. isidentifier  in-place - Returns True if the string is an identifier
# 18. islower       in-place - Returns True if all characters in the string are lower case
# 19. isnumeric     in-place - Returns True if all characters in the string are numeric
# 20. isprintable   in-place - Returns True if all characters in the string are printable
# 21. isspace       in-place - Returns True if all characters in the string are whitespaces
# 22. istitle       in-place - Returns True if the string follows the rules of a title
# 23. isupper       in-place - Returns True if all characters in the string are upper case
# 24. join          in-place - Joins the elements of an iterable to the end of the string
# 25. ljust         in-place - Returns a left justified version of the string
# 26. lower         in-place - Converts a string into lower case
# 27. lstrip        in-place - Returns a left trim version of the string
# 28. maketrans     in-place - Returns a translation table to be used in translations
# 29. partition     in-place - Returns a tuple where the string is parted into three parts
# 30. replace       in-place - Returns a string where a specified value is replaced with a specified value
# 31. rfind         in-place - Searches the string for a specified value and returns the last position of where it was found
# 32. rindex        in-place - Searches the string for a specified value and returns the last position of where it was found
# 33. rjust         in-place - Returns a right justified version of the string
# 34. rpartition    in-place - Returns a tuple where the string is parted into three parts
# 35. rsplit        in-place - Splits the string at the specified separator, and returns a list
# 36. rstrip        in-place - Returns a right trim version of the string
# 37. split         in-place - Splits the string at the specified separator, and returns a list
# 38. splitlines    in-place - Splits the string at line breaks and returns a list
# 39. startswith    in-place - Returns true if the string starts with the specified value
# 40. strip         in-place - Returns a trimmed version of the string
# 41. swapcase      in-place - Swaps cases, lower case becomes upper case and vice versa
# 42. title         in-place - Converts the first character of each word to upper case
# 43. translate     in-place - Returns a translated string
# 44. upper         in-place - Converts a string into upper case
# 45. zfill         in-place - Fills the string with a specified number of 0 values at the beginning


# The original string is untouched
print("Length of the original string \""+my_name+"\" is: "+str(len(my_name)))