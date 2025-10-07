score = float(input())
score_count = 0 
total_score = 0 
average_score = 0

# TODO: Your code here
while score > -1 and score < 101:
    score_count += 1
    total_score += score 
    score = float(input())

if score_count != 0:
    average_score = total_score / score_count
else:
    print(0)

print(score_count)
print(total_score)
print(f"{average_score:.2f}")
