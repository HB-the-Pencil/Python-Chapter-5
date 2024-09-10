# Define a variable so we can check different things.
favorite_candy = "almond joy"
melody_favorite = "twizzlers"
mckinstry_favorite = "almond joy"

# Interestingly, in the TIYs I use snake_case, but in the practicals (and my
# personal code), I use mixedCase.

# Comparison 1
print("Is my favorite candy an almond joy? "
      "I predict True.")
print(favorite_candy == "almond joy")

# Comparison 2
print("Is my favorite candy the same as Melody's? "
      "I predict False.")
print(favorite_candy == melody_favorite)

# Comparison 3
print("Is my favorite candy the same as Mr. McKinstry's? "
      "I predict True.")
print(favorite_candy == mckinstry_favorite)

# Comparison 4
print("Is my favorite candy the same as either Mr. McKinstry OR Melody? "
      "I predict True.")
print(favorite_candy == mckinstry_favorite or
      favorite_candy == melody_favorite)

# Comparison 5
print("Is my favorite candy the same as Mr. McKinstry AND Melody? "
      "I predict False.")
print(favorite_candy == mckinstry_favorite and
      favorite_candy == melody_favorite)

# Comparison 6
print("Is my favorite candy a properly capitalized Almond Joy? "
      "I predict False.")
print(favorite_candy == "Almond Joy")

# Comparison 7
print("Is 0100 0101 the number 72 in binary? "
      "I predict False.")
print(0b01000101 == 72)

# Comparison 8
print("Is c5 the number 200 in hex? "
      "I predict True.")
print(0xc5 == 200)

# Comparison 9
print("Is a4 equal to the number 251 in octal and the number 169 in decimal? "
      "I predict True.")
print(0xa4 == 0o251 and 0xa4 == 169)

# I was way off! quick error check
print("My prediction was wrong... Let's see what these numbers actually are.")
print("0xa4 =",0xa4, "0o251 =", 0o251, "169 =", 169)
print("I see... a4 is 16*10, not 15*11! That makes sense!")

# Comparison 10
print("Let's fix it. Is a9 equal to 251 in octal and 169 in decimal? "
      "I predict True.")
print(0xa9 == 0o251 and 0xa9 == 169)

# Comparison 11
print("Lastly, have I printed enough comparisons yet? "
      "I predict True.")
print(11 >= 10)