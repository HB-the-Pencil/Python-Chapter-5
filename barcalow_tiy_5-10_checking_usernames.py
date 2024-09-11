# Turn the list of users from TIY 5-8 (Hello Admin) into a current users list,
# then convert all values to lowercase for comparison.
current_users = ["Johnny", "joshua", "Hal", "Skynet", "admin", "big_brother",
                 "Neo", "Halliday", "floyd"]
current_users = [user.lower() for user in current_users]

# Add a list of new users (also references, but to the same movies as above).
new_users = ["parzival", "trinity", "david", "floyd", "hal"]

# Loop through the new users to make sure there aren't any duplicates.
for user in new_users:
    if user.lower() in current_users:
        print(f"Username {user.title()} is already taken.")
    else:
        print(f"Thank you for joining us, {user.title()}.")