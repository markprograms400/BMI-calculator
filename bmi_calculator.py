weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

BMI = weight / height ** 2

if BMI < 18.5: 
    print(f"Your BMI is {BMI:.2f}, you are underweight.")
elif 18.5 <= BMI <= 24.9:
    print(f"Your BMI is {BMI:.2f}, you are normal weight.")
elif 25.0 <= BMI <= 29.9: 
    print(f"Your BMI is {BMI:.2f}, you are overweight.")
else: 
    print(f"Your BMI is {BMI:.2f}, you are obese.")