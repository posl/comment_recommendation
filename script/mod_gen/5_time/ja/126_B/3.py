def judge(s):
    if 1 <= int(s[0:2]) <= 12 and 1 <= int(s[2:4]) <= 12:
        return "AMBIGUOUS"
    elif 1 <= int(s[0:2]) <= 12 and 1 > int(s[2:4]):
        return "MMYY"
    elif 1 > int(s[0:2]) and 1 <= int(s[2:4]) <= 12:
        return "YYMM"
    else:
        return "NA"
s = input()
print(judge(s))

if __name__ == '__main__':
    judge()