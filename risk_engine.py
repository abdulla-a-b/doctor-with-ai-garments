def back_pain_risk(age,bmi,work_type):

    score = 0

    if age > 40:
        score += 15

    if bmi >= 25 and bmi < 30:
        score += 15

    if bmi >= 30:
        score += 25

    if work_type == "sitting":
        score += 15

    if work_type == "lifting":
        score += 20

    return score


def risk_level(score):

    if score <=25:
        return "LOW"

    elif score <=50:
        return "MODERATE"

    elif score <=75:
        return "HIGH"

    else:
        return "SEVERE"
