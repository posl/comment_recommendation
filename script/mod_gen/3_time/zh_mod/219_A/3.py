def get_score(score):
    if score >= 0 and score < 40:
        return 40 - score
    elif score >= 40 and score < 70:
        return 70 - score
    elif score >= 70 and

if __name__ == '__main__':
    get_score()