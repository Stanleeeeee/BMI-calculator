#Simple BMI calculator using python

def bodymassindex(height, weight):
    return round((weight / height**2),2)

name = input("Enter your name ")
h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))


print("Welcome to the BMI calculator.")

bmi = bodymassindex(h, w)
print("Your BMI is: ", bmi)

if bmi <= 18.5:  
    print("Oops! You are underweight.")  
elif bmi <= 24.9:  
    print("Awesome! You are healthy.")  
elif bmi <= 29.9:  
    print("Eee! You are overweight.")  
else:
    print("Seesh! You are obese.")