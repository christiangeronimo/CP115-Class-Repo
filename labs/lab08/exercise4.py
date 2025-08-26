base_membership = 120
training_session = 80
total_training = 6
locker_rental = 25
towel_service = 15
registration_fee = 50 

training_fee = training_session * total_training
first_month = (registration_fee + locker_rental + towel_service + training_fee + base_membership )
following_month = ( locker_rental + towel_service + training_fee + base_membership )
annual_cost = first_month + following_month
print(first_month)
print(following_month)
print(annual_cost)

