Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S[0] == '0' and S[1] == '0' and S[2] == '0' and S[3] == '0':
        print('NA')
    elif S[0] == '0' and S[1] == '0' and S[2] != '0' and S[3] != '0':
        print('YYMM')
    elif S[0] == '0' and S[1] != '0' and S[2] == '0' and S[3] != '0':
        print('YYMM')
    elif S[0] == '0' and S[1] != '0' and S[2] != '0' and S[3] == '0':
        print('YYMM')
    elif S[0] == '0' and S[1] != '0' and S[2] != '0' and S[3] != '0':
        if int(S[2:4]) > 12:
            print('YYMM')
        else:
            print('AMBIGUOUS')
    elif S[0] != '0' and S[1] == '0' and S[2] == '0' and S[3] != '0':
        print('MMYY')
    elif S[0] != '0' and S[1] == '0' and S[2] != '0' and S[3] == '0':
        print('MMYY')
    elif S[0] != '0' and S[1] != '0' and S[2] == '0' and S[3] != '0':
        print('MMYY')
    elif S[0] != '0' and S[1] != '0' and S[2] != '0' and S[3] == '0':
        print('MMYY')
    elif S[0] != '0' and S[1] != '0' and S[2] != '0' and S[3] != '0':
        if int(S[0:2]) > 12:
            print('MMYY')
        else:
            print('AMBIGUOUS')
    else:
        print('NA')

=======
Suggestion 2

def main():
    S = input()
    if int(S[2:]) <= 12 and int(S[:2]) <= 12:
        print("AMBIGUOUS")
    elif int(S[2:]) <= 12:
        print("YYMM")
    elif int(S[:2]) <= 12:
        print("MMYY")
    else:
        print("NA")

=======
Suggestion 3

def main():
    S = input()
    YY = S[:2]
    MM = S[2:]
    if int(YY) >= 1 and int(YY) <= 12:
        if int(MM) >= 1 and int(MM) <= 12:
            print("AMBIGUOUS")
        else:
            print("YYMM")
    elif int(MM) >= 1 and int(MM) <= 12:
        print("MMYY")
    else:
        print("NA")

=======
Suggestion 4

def checkMMYY(s):
    if s[2:] == "00" or s[2:] == "01" or s[2:] == "02" or s[2:] == "03" or s[2:] == "04" or s[2:] == "05" or s[2:] == "06" or s[2:] == "07" or s[2:] == "08" or s[2:] == "09" or s[2:] == "10" or s[2:] == "11" or s[2:] == "12":
        return True
    else:
        return False

=======
Suggestion 5

def main():
    s = input()
    month = int(s[2:4])
    year = int(s[0:2])
    if (0 < month < 13) and (0 < year < 13):
        print('AMBIGUOUS')
    elif 0 < month < 13:
        print('MMYY')
    elif 0 < year < 13:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 6

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

=======
Suggestion 7

def checkYYMM(s):
    if (int(s[2:4]) > 12) or (int(s[2:4]) < 1):
        return False
    return True

=======
Suggestion 8

def is_month(month):
    if 0 < month <= 12:
        return True
    else:
        return False

=======
Suggestion 9

def main():
    # read the data
    s = input()
    # process the data
    # YYMM format
    if 1 <= int(s[2:4]) <= 12:
        if 1 <= int(s[0:2]) <= 12:
            ans = 'AMBIGUOUS'
        else:
            ans = 'YYMM'
    else:
        if 1 <= int(s[0:2]) <= 12:
            ans = 'MMYY'
        else:
            ans = 'NA'
    # print the answer
    print(ans)

=======
Suggestion 10

def month_check (month):
    if month in range(1,13):
        return True
    else:
        return False
