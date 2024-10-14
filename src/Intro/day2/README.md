### Built-in Data Types
    Python has the following data types built-in by default, in these categories:
        Text Type:	str
        Numeric Types:	int, float, complex
        Sequence Types:	list, tuple, range
        Mapping Type:	dict
        Set Types:	set, frozenset  
        Boolean Type:	bool
        Binary Types:	bytes, bytearray, memoryview
        None Type:	NoneType

### Type Casting 
    * int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
    * float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
    * str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
### Python String 
* 'hello' is the same as "hello".
* You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
    > print("It's alright")

    > print("He is called 'Johnny'")

    > print('He is called "Johnny"')
#### Python - Slicing Strings
    > b = "Hello, World!"

    > print(b[2:5]) # 2nd to 5th char --> llo

    > print(b[:5]) # 0th to 5th charecter --> Hello

    > print(b[-5:-2]) # orl

#### Modify Strings
    > The  `upper()` method returns the string in upper case

    > The `lower()` method returns the string in lower case

    > The `strip()` method removes any whitespace from the beginning or the end

    > The `replace()` method replaces a string with another string

    > The `split()` method splits the string into substrings if it finds instances of the separator

#### Concatination
    > Merge variable   `a` with variable `b` into variable `c`: e.g. c = a + b


#### Format - Strings
    # String Format
    age = 36
    txt = "My name is John, I am " + age
    print(txt)

    # F-Strings
    F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
    
    age = 36
    txt = f"My name is John, I am {age}"
    print(txt)

    # A placeholder can include a modifier to format the value.
    price = 59
    txt = f"The price is {price:.2f} dollars"
    print(txt)

#### String methods
    capitalize()	Converts the first character to upper case
    casefold()	Converts string into lower case
    center()	Returns a centered string
    count()	Returns the number of times a specified value occurs in a string
    encode()	Returns an encoded version of the string
    endswith()	Returns true if the string ends with the specified value
    expandtabs()	Sets the tab size of the string
    find()	Searches the string for a specified value and returns the position of where it was found
    format()	Formats specified values in a string
    format_map()	Formats specified values in a string
    index()	Searches the string for a specified value and returns the position of where it was found
    isalnum()	Returns True if all characters in the string are alphanumeric
    isalpha()	Returns True if all characters in the string are in the alphabet
    isascii()	Returns True if all characters in the string are ascii characters
    isdecimal()	Returns True if all characters in the string are decimals
    isdigit()	Returns True if all characters in the string are digits
    isidentifier()	Returns True if the string is an identifier
    islower()	Returns True if all characters in the string are lower case
    isnumeric()	Returns True if all characters in the string are numeric
    isprintable()	Returns True if all characters in the string are printable
    isspace()	Returns True if all characters in the string are whitespaces
    istitle()	Returns True if the string follows the rules of a title
    isupper()	Returns True if all characters in the string are upper case
    join()	Joins the elements of an iterable to the end of the string
    ljust()	Returns a left justified version of the string
    lower()	Converts a string into lower case
    lstrip()	Returns a left trim version of the string
    maketrans()	Returns a translation table to be used in translations
    partition()	Returns a tuple where the string is parted into three parts
    replace()	Returns a string where a specified value is replaced with a specified value
    rfind()	Searches the string for a specified value and returns the last position of where it was found
    rindex()	Searches the string for a specified value and returns the last position of where it was found
    rjust()	Returns a right justified version of the string
    rpartition()	Returns a tuple where the string is parted into three parts
    rsplit()	Splits the string at the specified separator, and returns a list
    rstrip()	Returns a right trim version of the string
    split()	Splits the string at the specified separator, and returns a list
    splitlines()	Splits the string at line breaks and returns a list
    startswith()	Returns true if the string starts with the specified value
    strip()	Returns a trimmed version of the string
    swapcase()	Swaps cases, lower case becomes upper case and vice versa
    title()	Converts the first character of each word to upper case
    translate()	Returns a translated string
    upper()	Converts a string into upper case
    zfill()	Fills the string with a specified number of 0 values at the beginning
    
Ref : https://www.w3schools.com/python/python_strings_methods.asp