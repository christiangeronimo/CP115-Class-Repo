employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
if tax_status == "Single" and base_salary >= 5000:
    tax_rate= 22
else: 
    tax_rate = 18

if tax_status == "Married" and base_salary >= 6000:
    tax_rate = 0.20/100
else: 
    tax_rate = 0.15/100

if tax_status == "Head" and base_salary >= 5500:
    tax_rate = 0.25/100
else: 
    tax_rate = 0.19/100

EPF = 0.11/100
SOCSO = 0.005/100
net_salary = ((tax_rate + EPF + SOCSO) * base_salary)+ (35 * overtime_hours) 
 
print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")