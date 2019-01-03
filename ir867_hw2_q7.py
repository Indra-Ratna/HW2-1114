# Indra 
# CS - UY 1114
# 24 Sept 2018
# Homework 2
user_kilo = float(input("Please enter weight in kilograms: "))
user_meter = float(input("Please enter height in meters: "))
BMI = user_kilo/(user_meter*user_meter)
print("BMI is " +str(BMI))
user_pound = float(input("Please enter weight in pounds: "))
user_inch= float(input("Please enter height in inches: "))
user_pound = user_pound*0.453592
user_inch = user_inch*0.0254 
BMI_customary = user_pound/(user_inch*user_inch)
print("BMI is "+ str(BMI_customary))
