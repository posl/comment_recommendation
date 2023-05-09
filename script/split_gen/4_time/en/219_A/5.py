def getRank(score):
    if score >= 0 and score < 40:
        return "D"
    elif score >= 40 and score < 70:
        return "C"
    elif score >= 70 and score < 90:
        return "B"
    elif score >= 90:
        return "A"
    else:
        return "Error"
