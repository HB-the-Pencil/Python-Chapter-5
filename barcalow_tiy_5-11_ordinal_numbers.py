# Create a list of numbers, 1-99. (They said 1-9, but I want a challenge :D)
nums = list(range(1,100))
nums = [str(num) for num in nums]

# Loop through the list.
for num in nums:
    # Check if the number is one digit long.
    if len(num) == 1:
        # Append the proper ending.
        if num[-1] == "1":
            print(num + "st")
        elif num[-1] == "2":
            print(num + "nd")
        elif num[-1] == "3":
            print(num + "rd")
        else:
            print(num + "th")
    # Check if the number is in the teens (they all end in th).
    elif num[-2] != "1":
        # Append the proper ending.
        if num[-1] == "1":
            print(num + "st")
        elif num[-1] == "2":
            print(num + "nd")
        elif num[-1] == "3":
            print(num + "rd")
        else:
            print(num + "th")
    # If it's in the teens, print the ending as th.
    else:
        print(num + "th")

# My list actually scales, so you can use it for 1000 numbers if you wanted,
# or even 1000 000!