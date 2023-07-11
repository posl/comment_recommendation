def get_grade(x):
    if 0 <= x < 40:
        return 40 - x
    elif 40 <= x < 70:
        return 70 - x
    elif 70 <= x < 90:
        return 90 - x
    else:
        return 'expert'

if __name__ == '__main__':
    get_grade()