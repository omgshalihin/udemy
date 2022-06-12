print("Welcome to the tip calculator.")
total = (input('What was the total bill? $'))
tip = input('What percentage tip would you like to give? 10, 12, or 15? ')
split = input('How many people to split the bill? ')

total_as_float = float(total)
tip_as_int = int(tip)
split_as_int = int(split)

net_total = total_as_float * ((tip_as_int + 100)/100)
each_person_bill = net_total / split_as_int
final_amt = "{:.2f}".format(each_person_bill)
print(f'Each person should pay: ${final_amt}')