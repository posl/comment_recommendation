def check(s):
    if 1 <= int(s[2:]) <= 12 and 1 <= int(s[:2]) <= 12:
        return "AMBIGUOUS"
    elif 1 <= int(s[2:]) <= 12:
        return "YYMM"
    elif 1 <= int(s[:2]) <= 12:
        return "MMYY"
    else:
        return "NA"

if __name__ == '__main__':
    check()