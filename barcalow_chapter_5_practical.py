"""
[X] Using the file provided by Mr. McKinstry (change the name to reflect your
    name) take the two lists that are created from the file and sort the list
    in Alphabetical order (I recommend not changing the list)

[X] Then check for duplicate candy names in the list and print duplicate candy
    types in a statement. For example, Snickers has been duplicated.

[X] Take the last 5 items in each list and print out that the candy costs this
    much at Walmart.com.

[X] Finally sum the entire (full) price list

[X] Use the price list to count the number of different candies that are more
    than $3.00 then remove them from the price list. Print this list to show
    that all the candy costs over $3.00 have been removed.

[X] Finally sum the new price list
"""

import csv
# Pull in the CSV file
filename = 'candy_type.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Loop through the csv file and create two lists
    candy_type = []
    candy_price = []

    for row in reader:
        candy = row[1]
        price = float(row[2])
        candy_type.append(candy)
        candy_price.append(price)
    print(candy_type)
    print(candy_price)

# Clean the data as much as I know how. Strip it and make it lowercase for
# easier comparison.
candy_type = [candy.lower().strip() for candy in candy_type]

# I could say candy_type = candy_type.sorted, but the prices wouldn't match.
print(sorted(candy_type))

# Make a list of candies that are already there.
candy_exists = []

# This data is horribly unclean. I hope we learn an efficient way to clean it
# soon. This goes through the list to tell us of any duplicates.
for candy in candy_type:
    if candy in candy_exists:
        print(f"{candy.title()} is a duplicate value")
    else:
        candy_exists.append(candy)

# Print the last 5 items and their costs.
for i in range(-5, 0):
    print(f"{candy_type[i].title()} costs ${candy_price[i]} at Walmart.")

# Print the sum of the full price list.
print(f"To buy all the candy here would cost ${sum(candy_price)}.")

print("Let's remove all the candies that cost more than three dollars.")

# Remove any items that cost over three dollars. Going through the list
# backwards ensures that we don't get an index error.
for i in range(-len(candy_price), 0):
    if candy_price[i] > 3:
        del candy_price[i]
        del candy_type[i]

print(candy_price)
print(candy_type)

print(f"To buy all the candies that cost less than three dollars would cost "
      f"${round(sum(candy_price), 2)} at Walmart.")