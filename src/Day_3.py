import string

from utils import read_file

values = read_file(3, str, False)


# Part 1

rucksacks = []

# Creates list of rucksacks each with two compartments
for value in values:
    compartments = []
    items = list(value)
    items_total = len(items)
    middle_index = int(items_total/2)
    compartments.append(items[:middle_index])  # First compartment
    compartments.append(items[middle_index:])  # Second compartment
    rucksacks.append(compartments)

duplicate_items = []

# Used the set function to find the duplicates
for rucksack in rucksacks:
    duplicate_items.append(list(set(rucksack[0]) & set(rucksack[1])))  # Converted the set back into a list

duplicate_items = [item for sublist in duplicate_items for item in sublist]  # List cleanup to flatten list

priority_total = 0

# Used the string.ascii_letters function to find the index and added one to the index to get the priority level
for duplicate in duplicate_items:
    priority_total += string.ascii_letters.index(duplicate) + 1

print("Part 1: " + str(priority_total))

# Part 1 = 8401

# Part 2

groups = []
group_rucksacks = []

for i in range(len(values) + 1):
    if i % 3 == 0 and i != 0:
        groups.append(group_rucksacks)
        group_rucksacks = []
        if i == len(values):
            continue
        group_rucksacks.append(list(values[i]))
    else:
        group_rucksacks.append(list(values[i]))

badges = []

for group in groups:
    badges.append(list(set(group[0]) & set(group[1]) & set(group[2])))

badges = [item for sublist in badges for item in sublist]

priority_total = 0

for badge in badges:
    priority_total += string.ascii_letters.index(badge) + 1

print("Part 2: " + str(priority_total))
# Part 2 = 2641
