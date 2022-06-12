#Don't change below
height = float(input('enter your height in m: '))
weight = int(input('enter your weight in kg: '))
#Don't change above

bmi = round((weight / (height**2)),2)
print(bmi)