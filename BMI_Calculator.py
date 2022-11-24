weight = int(input("Your weight (example: 80): "))

height = float(input("Your height (example: 1.70): "))

bmi = weight / (height * height)

if bmi < 18.5:
    print('You are in the category of "underweight".')

elif bmi >= 18.5 and bmi < 25:
    print('You are in the category of "normal".')

elif bmi >= 25 and bmi < 30:
    print('You are in the category of "overweight".')

elif bmi >= 30:
    print('You are in the category of "obesity".')