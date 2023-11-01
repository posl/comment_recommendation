def get_next_grade_score(score):
    if score < 40:
        return 40 - score
    elif score < 70:
        return 70 - score
    elif score < 90:
        return 90 - score

if __name__ == '__main__':
    get_next_grade_score()