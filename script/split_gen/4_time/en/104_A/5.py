def get_next_contest(rating):
    if rating < 1200:
        return 'ABC'
    elif rating < 2800:
        return 'ARC'
    else:
        return 'AGC'
