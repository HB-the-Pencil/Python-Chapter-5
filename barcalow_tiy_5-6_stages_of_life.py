# Using int(input()) again for easier testing.
age = int(input("How old are you? "))

if age < 0:
    stage = "input error"
elif age < 2:
    stage = "baby"
elif age < 4:
    stage = "toddler"
elif age < 13:
    stage = "kid"
elif age < 20:
    stage = "teenager"
elif age < 65:
    stage = "adult"
elif age >= 65:
    stage = "elder"
else:
    stage = "input error"

# It's not foolproof, but a pretty good way to check a/an.
vowels = ["a", "e", "i", "o", "u"]  # and sometimes y :D

print(f"You are {"an " + stage if stage[:1] in vowels else "a " + stage}.")