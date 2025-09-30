num_days = int(input())
danger_threshold = float(input())
danger_days = 0
total_temperature = 0

for days_num in range (num_days):
    temperatures = float(input())

    total_temperature += temperatures 


    if temperatures > danger_threshold:
        danger_days += 1


average_temp = total_temperature / num_days

print(danger_days)
print(f"{average_temp:.1f}")