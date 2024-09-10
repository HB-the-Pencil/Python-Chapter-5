# Code copied from TIY 5-1 (Conditional Tests). New code at line 54.

favorite_candy = "almond joy"
melody_favorite = "twizzlers"
mckinstry_favorite = "almond joy"

print("Is my favorite candy an almond joy? "
      "I predict True.")
print(favorite_candy == "almond joy")

print("Is my favorite candy the same as Melody's? "
      "I predict False.")
print(favorite_candy == melody_favorite)

print("Is my favorite candy the same as Mr. McKinstry's? "
      "I predict True.")
print(favorite_candy == mckinstry_favorite)

print("Is my favorite candy the same as either Mr. McKinstry OR Melody? "
      "I predict True.")
print(favorite_candy == mckinstry_favorite or
      favorite_candy == melody_favorite)

print("Is my favorite candy the same as Mr. McKinstry AND Melody? "
      "I predict False.")
print(favorite_candy == mckinstry_favorite and
      favorite_candy == melody_favorite)

print("Is my favorite candy a properly capitalized Almond Joy? "
      "I predict False.")
print(favorite_candy == "Almond Joy")

print("Is 0100 0101 the number 72 in binary? "
      "I predict False.")
print(0b01000101 == 72)

print("Is c5 the number 200 in hex? "
      "I predict True.")
print(0xc5 == 200)

print("Is a4 equal to the number 251 in octal and the number 169 in decimal? "
      "I predict False.")
print(0xa4 == 0o251 and 0xa4 == 169)

print("Let's fix it. Is a9 equal to 251 in octal and 169 in decimal? "
      "I predict True.")
print(0xa9 == 0o251 and 0xa9 == 169)

print("Lastly, have I printed enough comparisons yet? "
      "I predict True.")
print(11 >= 10)


# New code begins here.

print("------------------------------")

# String-String Equality
print('Is "hello world" the same as "Hello world"? '
      'I predict False.')
print("hello world" == "Hello world")

# String-String Inequality
print('Is "hello world" NOT the same as "Hello world", then? '
      'I predict True.')
print("hello world" != "Hello world")

# String-String Equality with .lower()
print('Is "hello world" the same as "HeLlO wOrLd".lower()? '
      'I predict True.')
print("hello world" == "HeLlO wOrLd".lower())

# Numerical Equality
print("Is 45 - 26*2 equal to -7? "
      "I predict True.")
print(45 - 26*2 == -7)

# Numerical Inequality
print("Is three NOT equal to four? "
      "I predict True.")
print(3 != 4)

# Numerical Greater Than
print("Is three less than four? "
      "I predict True.")
print(3 < 4)

# Numerical Less Than
print("Is the 2 to the 3 less than 3 to the 2? "
      "I predict True.")
print(2 ** 3 < 3 ** 2)

# Numerical Greater Than or Equal To
print("Is 4 to the 3 greater than or equal to 3 to the 4? "
      "I predict False.")
print(4 ** 3 >= 3 ** 4)

# Numerical Less Than or Equal To
print("Is 10 in hex less than or equal to 10 in decimal? "
      "I predict False.")
print(0x10 <= 10)

# String Comparison Operators
print("Can I compare strings with a less than operator? "
      "I don't think I can.")
print("abc" < "def")

# String Comparison Operators (part 2)
print("How does this work??")
print("abc" > "def")
print("ab" < "def")
print("abc" > "de")
print("I think strings are assigned a number based on their characters.")
print("abcd" > "e")
# After looking it up, strings are ordered based on their ordinal values.
# These can be found with the ord command. They're basically the ASCII value.
# This comparison can be used for alphabetical orders (does item X come before
# item Y)? Pretty cool. Thanks to runestone.academy!

# And Comparisons
print("If I compare (True AND NOT True) AND True, what will the answer be? "
      "I predict False.")
print((True and not True) and True)

# Or Comparisons
print("If I compare (False OR NOT False) OR False, what will the answer be? "
      "I predict True.")
print((False or not False) or False)

# In List
small_list = ["small", "tiny", "miniature"]
print("Is tiny in the small list? "
      "I predict True.")
print("tiny" in small_list)

# Not In List
print("Is minuscule in the small list? "
      "I predict False.")
print("minuscule" in small_list)