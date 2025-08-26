import math

# Getting user input (always returns a string)
price1= float(input("Enter your price1: "))
item_name1 = str(input("Enter your item1: "))
price2 = float(input("Enter your price2: "))
item_name2 = str(input("Enter your item2: "))
price3 = float(input("Enter your price3: "))
item_name3 = str(input("Enter your item3: "))

sub_total = price1 + price2 + price3 
tax_amount = sub_total * 0.06
total_amount = sub_total + tax_amount

# Formatted output using string concatenation
print()
print("Sub Total: " + str(sub_total))
print("Tax Amount: " + str(tax_amount))
print("Total Amount: " + str(total_amount))