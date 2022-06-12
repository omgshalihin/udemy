#create a program to tell us how many days, weeks, months you have left if we live until 90 years old.

#Don't change below
from calendar import month


age = int(input('What is your current age? '))
#Don't change above

# 1 year = 365 days = 52 weeks = 12 months

max_year = 90

years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f'You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.')
