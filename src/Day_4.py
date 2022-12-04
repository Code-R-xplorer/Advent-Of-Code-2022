from utils import read_file

values = read_file(4, str, False)

elf_pairs_ids = []
for value in values:
    pairs = value.split(',')  # Splits the line into two pairs
    # Splits the pairs into the two values for each elf
    first_elf = pairs[0].split('-')
    second_elf = pairs[1].split('-')
    # Gets the lower and upper bounds of each elf's assignment ids
    first_elf_lower = int(first_elf[0])
    first_elf_upper = int(first_elf[1])
    second_elf_lower = int(second_elf[0])
    second_elf_upper = int(second_elf[1])
    # Gets the range of assignment ids for each elf
    first_elf_ids = []
    second_elf_ids = []
    for i in range(first_elf_lower, first_elf_upper + 1):
        first_elf_ids.append(i)
    for i in range(second_elf_lower, second_elf_upper + 1):
        second_elf_ids.append(i)
    # Appends the final list to the master list
    tmp = [first_elf_ids, second_elf_ids]
    elf_pairs_ids.append(tmp)

total_duplicate_pairs = 0
# Part 1
for elf_pair_id in elf_pairs_ids:
    # Gets a set of the two assignment ids for the elf pair
    # This returns any duplicates in the list
    common_ids = set(elf_pair_id[0]) & set(elf_pair_id[1])
    # If the length of the set is equal to either of the pair's list increase the total duplicate pairs
    if len(common_ids) == len(elf_pair_id[0]) or len(common_ids) == len(elf_pair_id[1]):
        total_duplicate_pairs += 1

print("Part 1: " + str(total_duplicate_pairs))
# Part 1 - 595

total_duplicate_pairs = 0

for elf_pair_id in elf_pairs_ids:
    common_ids = set(elf_pair_id[0]) & set(elf_pair_id[1])
    if len(common_ids) > 0:  # Much the same as part 1 apart from only needing to check if any duplicate was found
        total_duplicate_pairs += 1

print("Part 2: " + str(total_duplicate_pairs))
# Part 2 - 952
