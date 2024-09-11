# Define an (empty) list of users. Code copied from TIY 5-8 (Hello Admin).
users = []

# Are there any users?
if users:
    # Go through the list to test if a user is an admin or not.
    for user in users:
        if user == "admin":
            print("Greetings, Admin. What shenanigans will we be getting up "
                  "to today?")
        else:
            print(f"Welcome back, {user.title()}.")
else:
    print("We need to find some users!")