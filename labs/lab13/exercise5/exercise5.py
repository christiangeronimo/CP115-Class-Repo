amount = int(input())

# TODO: Your code here
valid_count = 0
total_withdrawn = 0

while amount != 0:
    if amount >= 200 and amount <= 500 and amount % 20 == 0:
        valid_count += 1
        total_withdrawn += amount
    
    
    amount = int(input())

    



print(valid_count)      # Number of valid withdrawals
print(total_withdrawn)  # Total amount from valid withdrawals only
