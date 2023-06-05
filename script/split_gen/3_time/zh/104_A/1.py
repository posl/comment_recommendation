def get_next_contest_name(r):
    if r < 1200:
        return "ABC"
    elif r < 2800:
        return "ARC"
    else:
        return "AGC"
