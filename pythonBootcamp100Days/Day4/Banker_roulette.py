import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(',')

# num_items = len(names)
# random_choice = random.randint(0, num_items-1)
# who_will_pay = names[random_choice]
# print(names)
# print(f'Random number is: {random_choice}\n')
# print(f'{who_will_pay.title()} is going to buy the meal today!')

# OR shortcut

print(names)
who_will_pay = random.choice(names)
print(f'{who_will_pay.title()} is going to buy the meal today!')



