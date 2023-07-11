def get_score(score):
    if score >= 90:
        return 'expert'
    elif score >= 70:
        return 90 - score
    elif score >= 40:
        return 70 - score
    else:
        return 40 - score
