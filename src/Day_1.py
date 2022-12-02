from utils import read_file

values = read_file(1, str, False) # Helper function to read text file

elf_counts = [] # Calorie Counts for meal that each elf has
elf_count = []  # Temp list for each elf's counts
elf_totals = [] # Total calorie counts for each elf


for v in values:
    # Appends the calorie value of the meal into the temp list
    if v != '':
        elf_count.append(int(v))
    # Each elf's inventory is seperated by a blank line
    else:
        # Append all values for the elf into the counts list
        elf_counts.append(elf_count)
        # Reset the temp list for the next elf
        elf_count = []

# Total each elf's inventory calorie counts into a totals list
for counts in elf_counts:
    total = 0
    for cal in counts:
        total += cal
    elf_totals.append(total)

# Part 1 wanted to find the elf with the largest calorie count so max() works well for this
print(max(elf_totals))

# Part 1 Answer: 68775

# For the second part they wanted the top three calorie counts
# The sorted function works well for this
elf_totals = sorted(elf_totals, reverse=True)

# Prints the total calorie count for the top three elfs
print(elf_totals[0] + elf_totals[1] + elf_totals[2])

# Part 2 Answer: 202585


