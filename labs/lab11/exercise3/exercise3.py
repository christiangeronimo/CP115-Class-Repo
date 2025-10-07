target_points = int(input())
total_points = 0
rounds_played = 0

# Keep playing rounds until total_points reaches or exceeds target_points
while total_points < target_points:
    points = int(input())
    total_points += points
    rounds_played += 1

print(total_points)
print(rounds_played)
