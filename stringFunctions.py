 
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
print("\nCapitalized: " + new_name + "\n")


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
another_name = "i åm A\tPIAIC\tStudent"
new_name = another_name.expandtabs(15)
print("Expanded tab size in \"i åm tA\\tPIAIC\\tStudent\" where \\t are tabs, by 15:\"" + new_name  + "\"\n")


# 8. find           in-place - Searches the string for a specified value and returns the position of where it was found
new_name = my_name.find("Stud")
print("Position of \"Stud\" in given string: "+str(new_name) + "\n")


# 9. format         in-place - Formats specified values in a string
new_name = "\"I am {age:2d} years old\""
print("Formatted string:" +new_name.format(age = 25) + " Through format function\n");


# 10. format_map    in-place - Formats specified values in a string
format_input_dict = {'age':25} 
print("Formatted string:" +new_name.format_map(format_input_dict)  + " Through formatmap function\n");


# 11. index         in-place - Searches the string for a specified value and returns the index of where it was found
new_name = my_name.index("udent")
print("Index of \"u\" in given string: "+str(new_name) + "\n")


# 12. isalnum       in-place - Returns True if all characters in the string are alphanumeric
print("String is AlphaNumeric: " + str(my_name.isalnum()) + "\n")

# 13. isalpha       in-place - Returns True if all characters in the string are in the alphabet
print("String is Alphabetic Only: " + str(my_name.isalpha()))
another_name = "iamastudent"
print(another_name + " is Alphabetic Only: " + str(another_name.isalpha()) + "\n")

# 14. isascii       in-place - Returns True if all characters in the string are ascii
print("String is ASCII: " + str(my_name.isascii()))
print(another_name + " is ASCII: " + str(another_name.isascii()) + "\n")

# 15. isdecimal     in-place - Returns True if all characters in the string are decimals
print("String is Decimal Only: " + str(my_name.isdecimal()) + "\n")

# 16. isdigit       in-place - Returns True if all characters in the string are digits
print("String is Digits Only: " + str(my_name.isdigit()) + "\n")

# 17. isidentifier  in-place - Returns True if the string is an identifier
print("String is an Identifier: " + str(my_name.isidentifier()) + "\n")

# 18. islower       in-place - Returns True if all characters in the string are lower case
print("String is in Lower case: " + str(my_name.islower()) + "\n")

# 19. isnumeric     in-place - Returns True if all characters in the string are numeric
print("String is numeric Only: " + str(my_name.isnumeric()) + "\n")

# 20. isprintable   in-place - Returns True if all characters in the string are printable
print("String is Printable: " + str(my_name.isprintable()) + "\n")

# 21. isspace       in-place - Returns True if all characters in the string are whitespaces
print("String has whitespaces only: " + str(my_name.isspace()) + "\n")


# 22. istitle       in-place - Returns True if the string follows the rules of a title
print("String is formatted as a title: " + str(my_name.istitle()) + "\n")
another_name = "This Is A Title"
print(another_name + " is formatted as a title: " + str(another_name.istitle()) + "\n")


# 23. isupper       in-place - Returns True if all characters in the string are upper case
print("String is all uppercase: " + str(my_name.isupper()) + "\n")

# 24. join          in-place - Joins the elements of an iterable to the end of the string
another_name = ("AI", "Cloud Native", "IoT", "BlockChain")
another_name = "-".join(another_name)
print(another_name + "\n")

# 25. ljust         in-place - Returns a left justified version of the string
print("\""+ my_name.ljust(50) + "\":This is left Justified in 50 spaces" + "\n")

# 26. lower         in-place - Converts a string into lower case
print("Lower case: " + my_name.lower() + "\n")

# 27. lstrip        in-place - Returns a left trim version of the string
another_name = "     a piaic student     "
another_name = another_name.lstrip()
print("This is left stripped of all whitespace: \"" + another_name + "\"\n")

# # 28. maketrans     in-place - Returns a translation table to be used in translations
# from string import maketrans, translate    #maketrans function to be imported from string
# intab = "aeiou"
# outtab = "12345"
# trantab = maketrans(intab, outtab)
# str = "this is string example....wow!!!"
# print str.translate(trantab)


# 29. partition     in-place - Returns a tuple where the string is parted into three parts
new_name = my_name.partition("PIAIC")
print("String partitioned in three parts:" + str(new_name) + "\n")

# 30. replace       in-place - Returns a string where a specified value is replaced with a specified value
new_name = my_name.replace("I", "e")
print("I replaced in string with e: " + new_name + "\n")

# 31. rfind         in-place - Searches the string for a specified value and returns the last position of where it was found
new_name = my_name.rfind("t")
print("Last position of \"t\" in string: " + str(new_name) + "\n")
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