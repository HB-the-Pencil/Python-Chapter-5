# I'm doing extra here: I'm going to take an input and make the default
# 0 points (in case you misspell something).
alien_color = input("What color of alien did you hit (green, red, yellow)? ")

# 5 points for green, 10 for yellow, 15 for red, 0 for anything else.
if alien_color == "green":
    points = 5
elif alien_color == "yellow":
    points = 10
elif alien_color == "red":
    points = 15
else:
    points = 0

print(f"+{points} points!")