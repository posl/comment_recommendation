def print_contest_name(rating):
    if rating < 1200:
        return "ABC"
    elif rating < 2800:
        return "ARC"
    else:
        return "AGC"

if __name__ == '__main__':
    print_contest_name()