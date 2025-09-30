monthly_usage = float(input())
discount = 0
total_bill = 0

if monthly_usage < 50:
    print("No Discount")
    total_bill = monthly_usage
elif monthly_usage <= 100:
    total_bill = monthly_usage * 0.95
elif monthly_usage > 100:
    total_bill = monthly_usage * 0.80

print(f"Total bill : {total_bill}")