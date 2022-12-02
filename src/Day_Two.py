from utils import read_file

values = read_file(2, str, False)

games = []

for v in values:
    tmp = []
    for g in v:
        if g != '\n':
            tmp.append(g)
    games.append(tmp)

total_score = 0

# Part 1
for game in games:
    opponent_pick = game[0]
    your_pick = game[2]
    # Rock
    if opponent_pick == 'A':
        # Rock
        if your_pick == 'X':
            total_score += (1 + 3)  # Draw
        # Paper
        if your_pick == 'Y':
            total_score += (2 + 6)  # Win
        # Scissors
        if your_pick == 'Z':
            total_score += (3 + 0)  # Lose
    # Paper
    if opponent_pick == 'B':
        # Rock
        if your_pick == 'X':
            total_score += (1 + 0)  # Lose
        # Paper
        if your_pick == 'Y':
            total_score += (2 + 3)  # Draw
        # Scissors
        if your_pick == 'Z':
            total_score += (3 + 6)  # Win
    # Scissors
    if opponent_pick == 'C':
        # Rock
        if your_pick == 'X':
            total_score += (1 + 6)  # Win
        # Paper
        if your_pick == 'Y':
            total_score += (2 + 0)  # Lose
        # Scissors
        if your_pick == 'Z':
            total_score += (3 + 3)  # Draw

# Part 2
for game in games:
    opponent_pick = game[0]
    your_pick = game[2]
    # Rock
    if opponent_pick == 'A':
        # Lose
        if your_pick == 'X':
            total_score += (3 + 0)
        # Draw
        if your_pick == 'Y':
            total_score += (1 + 3)
        # Win
        if your_pick == 'Z':
            total_score += (2 + 6)
    # Paper
    if opponent_pick == 'B':
        # Lose
        if your_pick == 'X':
            total_score += (1 + 0)
        # Draw
        if your_pick == 'Y':
            total_score += (2 + 3)
        # Win
        if your_pick == 'Z':
            total_score += (3 + 6)
    # Scissors
    if opponent_pick == 'C':
        # Lose
        if your_pick == 'X':
            total_score += (2 + 0)
        # Draw
        if your_pick == 'Y':
            total_score += (3 + 3)
        # Win
        if your_pick == 'Z':
            total_score += (1 + 6)

print(total_score)

# A = Rock, Score = 1
# B = Paper, Score = 2
# C = Scissors, Score = 3
# Lost = 0, Draw = 3, Win = 6
