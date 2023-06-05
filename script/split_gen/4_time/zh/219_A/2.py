def get_grade(score):
    if score >= 90:
        return 'expert'
    elif score >= 70:
        return 'high'
    elif score >= 40:
        return 'middle'
    else:
        return 'newbie'
