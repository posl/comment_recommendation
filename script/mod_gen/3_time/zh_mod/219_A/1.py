def get_level(score):
    if score < 40:
        return 'D'
    elif score < 70:
        return 'C'
    elif score < 90:
        return 'B'
    else:
        return 'A'

if __name__ == '__main__':
    get_level()