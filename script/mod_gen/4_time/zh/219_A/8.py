def calc_score(score):
    if score >= 0 and score < 40:
        return 40 - score
    elif score >= 40 and score < 70:
        return 70 - score
    elif score >= 70 and score < 90:
        return 90 - score
    else:
        return "expert"

if __name__ == '__main__':
    calc_score()