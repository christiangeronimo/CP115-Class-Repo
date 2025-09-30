age = int(input())
accident_count = int(input())
penalty = 0 

if age <= 25:
    base_premium = 2400
elif age >= 25 or age <= 50:
    base_premium = 1800
elif age > 50:
    base_premium = 2000

if accident_count == 0:
    penalty = 0 
elif accident_count >= 1 and accident_count <= 2:
    penalty = 300 
elif accident_count >= 3:
    penalty = 600

final_premium = base_premium + penalty 
discount_amount=0

if accident_count == 0:
    discount_amount = final_premium * 0.1
    final_premium = final_premium * 0.9




print(base_premium)
print(final_premium)
print(discount_amount)