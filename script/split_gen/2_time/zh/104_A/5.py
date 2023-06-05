def next_contest(R):
    if R < 1200:
        return "ABC"
    elif R < 2800:
        return "ARC"
    else:
        return "AGC"
