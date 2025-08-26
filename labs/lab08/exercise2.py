main_dishes = 25 * 3
appetizers = 12 * 2 
drink = 8 * 4 
delivery_fee = 5 
service_tax = 0.1

total_price = (main_dishes + appetizers + drink) + delivery_fee
total_bill = (total_price * service_tax ) + (total_price)


amount_each = (total_bill // 6)
print(amount_each)