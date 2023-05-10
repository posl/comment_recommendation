def check(s):
    if int(s[0:2]) >= 1 and int(s[0:2]) <= 12:
        if int(s[2:4]) >= 1 and int(s[2:4]) <= 12:
            return "AMBIGUOUS"
        else:
            return "MMYY"
    else:
        if int(s[2:4]) >= 1 and int(s[2:4]) <= 12:
            return "YYMM"
        else:
            return "NA"
s = input()
print(check(s))

if __name__ == '__main__':
    check()