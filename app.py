import json
from bmi import calculate_bmi
from risk_engine import back_pain_risk, risk_level


# load disease list
with open("diseases.json") as f:
    diseases = json.load(f)


print("GARMENTS AI DOCTOR")
print("------------------")

name = input("Patient Name: ")
age = int(input("Age: "))
gender = input("Gender: ")
height = float(input("Height cm: "))
weight = float(input("Weight kg: "))
work_type = input("Work Type (sitting/lifting/standing): ")
symptom = input("Symptom: ")

bmi = calculate_bmi(weight,height)

score = back_pain_risk(age,bmi,work_type)
level = risk_level(score)

print("\n----- AI DOCTOR RESULT -----")
print("Patient:",name)
print("BMI:",bmi)
print("Symptom:",symptom)
print("Risk Score:",score)
print("Risk Level:",level)

print("\nMedicine:")
print("- Paracetamol")
print("- Ibuprofen")

print("\nExercise:")
print("- Back stretch")
print("- Walking")

print("\nFood:")
print("- Milk")
print("- Egg")
print("- Spinach")

print("\nRecommended Doctor:")
print("Orthopedic Specialist")
