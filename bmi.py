bmi = int(input("Enter BMI: "))
print(bmi)
if bmi < 18:
    print("Underweight")
elif (bmi >= 18) and (bmi <= 24):
    print("Normal")
elif (bmi >= 25) and (bmi <= 30):
    print("Overweight")
else:
    print("Obese")
