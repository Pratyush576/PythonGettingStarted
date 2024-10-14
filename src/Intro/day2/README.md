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
* Python - Slicing Strings
    > b = "Hello, World!"

    > print(b[2:5]) # 2nd to 5th char --> llo

    > print(b[:5]) # 0th to 5th charecter --> Hello

    > print(b[-5:-2]) # orl