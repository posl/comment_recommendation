def checkdate(S):
    if (int(S[2:4]) >= 1 and int(S[2:4]) <= 12) and (int(S[0:2]) >= 1 and int(S[0:2]) <= 12):
        return "AMBIGUOUS"
    elif (int(S[2:4]) >= 1 and int(S[2:4]) <= 12):
        return "YYMM"
    elif (int(S[0:2]) >= 1 and int(S[0:2]) <= 12):
        return "MMYY"
    else:
        return "NA"
S = input()
print(checkdate(S))

if __name__ == '__main__':
    checkdate()