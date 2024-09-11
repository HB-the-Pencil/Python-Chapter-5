# Define a list of users. +20 cool points if you get all of them.
users = ["johnny", "joshua", "hal", "skynet", "admin", "big_brother", "neo",
         "halliday", "floyd"]

# Go through the list to test if a user is an admin or not.
for user in users:
    if user == "admin":
        print("Greetings, Admin. What shenanigans will we be getting up to "
              "today?")
    else:
        print(f"Welcome back, {user.title()}.")