from utils import read_file

values = read_file(1, str, False)

elf_counts = []
elf_count = []
elf_totals = []


for v in values:
    if v != '':
        elf_count.append(int(v))
    else:
        elf_counts.append(elf_count)
        elf_count = []


for counts in elf_counts:
    total = 0
    for cal in counts:
        total += cal
    elf_totals.append(total)
# Part 1 68775
print(max(elf_totals))

# elf_totals_top_three = []
#
# for i in range(3):
#     elf_totals_top_three.append(max(elf_totals))

elf_totals = sorted(elf_totals, reverse=True)

print(elf_totals[0] + elf_totals[1] + elf_totals[2])


