def get_grade(score):
    if score >= 90:
        return 'expert'
    elif score >= 70:
        return 'high'
    elif score >= 40:
        return 'middle'
    else:
        return 'newbie'

if __name__ == '__main__':
    get_grade()