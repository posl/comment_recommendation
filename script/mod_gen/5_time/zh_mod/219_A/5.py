def get_score_level(score):
    if score >= 0 and score < 40:
        return 'D'
    elif score >= 40 and score < 70:
        return 'C'
    elif score >= 70 and score < 90:
        return

if __name__ == '__main__':
    get_score_level()