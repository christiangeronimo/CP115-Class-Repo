passing_count = 0
failing_count = 0

score_input = input()

while score_input != "end":
    score = int(score_input)  
    if score >= 60:
        passing_count += 1
    else:
        failing_count += 1
    score_input = input()

total = passing_count + failing_count

if total > 0:
    pass_rate = (passing_count / total) * 100
else:
    pass_rate = 0


print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")
