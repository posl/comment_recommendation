def check(s):
    if 1 <= int(s[0:2]) <= 12 and 1 <= int(s[2:4]) <= 12:
        return "AMBIGUOUS"
    elif 1 <= int(s[0:2]) <= 12:
        return "MMYY"
    elif 1 <= int(s[2:4]) <= 12:
        return "YYMM"
    else:
        return "NA"
