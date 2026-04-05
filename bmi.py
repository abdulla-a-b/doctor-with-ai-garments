def calculate_bmi(weight, height_cm):
    height = height_cm / 100
    bmi = weight / (height * height)
    return round(bmi,1)
