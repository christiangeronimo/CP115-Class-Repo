grade = float(input())
valid_count = 0 
average  = 0
# TODO: Your code here
while grade > -1 :
    
    if grade < 0 or grade > 100:
        continue 

    if grade > 0 or grade < 100:
        valid_count += 1
        grade += grade 
        grade = float(input()) 

    if grade < 0 :
        break

average = grade / valid_count



print(valid_count)
print(f"{average:.2f}")
