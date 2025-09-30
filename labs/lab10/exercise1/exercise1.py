position = input()
overtime_hours = int(input())
is_weekend = input()

<<<<<<< HEAD
if position == "Manager":
    hourly_rate = 35 
=======
# Define base hourly rates
if position == "Manager":
    hourly_rate = 35
>>>>>>> 1fed0c66c3713a088812b3d84e818e9d831ec42a
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18

<<<<<<< HEAD

overtime_pay = (hourly_rate * overtime_hours) * 1.5

if is_weekend == "Yes":
    overtime_pay += overtime_hours * 5


=======
# Calculate overtime pay (1.5x base rate)
overtime_rate = hourly_rate * 1.5
overtime_pay = overtime_hours * overtime_rate

# Add weekend bonus if applicable
if is_weekend.lower() == "yes":
    weekend_bonus = overtime_hours * 6
    overtime_pay += weekend_bonus

# Total pay is same as overtime pay
>>>>>>> 1fed0c66c3713a088812b3d84e818e9d831ec42a
total_pay = overtime_pay

print(hourly_rate)
print(overtime_pay)
print(total_pay)
