Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if 1 <= int(S[0:2]) <= 12 and 1 <= int(S[2:4]) <= 12:
        print("AMBIGUOUS")
    elif 1 <= int(S[0:2]) <= 12:
        print("MMYY")
    elif 1 <= int(S[2:4]) <= 12:
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 2

def is_valid_month(month):
    if month >=1 and month <= 12:
        return True
    else:
        return False

=======
Suggestion 3

def is_month(m):
    return 1 <= m and m <= 12

=======
Suggestion 4

def check(s):
    if s[0] == '0' and s[1] == '0':
        return False
    elif s[2] == '0' and s[3] == '0':
        return False
    else:
        return True

=======
Suggestion 5

def checkMonth(month):
    if month < 1 or month > 12:
        return False
    return True

=======
Suggestion 6

def main():
    S = input()
    if S[0:2] in ['00','01','02','03','04','05','06','07','08','09'] and S[2:4] in ['01','02','03','04','05','06','07','08','09','10','11','12']:
        print('YYMM')
    elif S[0:2] in ['01','02','03','04','05','06','07','08','09','10','11','12'] and S[2:4] in ['00','01','02','03','04','05','06','07','08','09']:
        print('MMYY')
    elif S[0:2] in ['00','01','02','03','04','05','06','07','08','09'] and S[2:4] in ['00','01','02','03','04','05','06','07','08','09']:
        print('NA')
    else:
        print('AMBIGUOUS')

=======
Suggestion 7

def get_result(s):
    if int(s[0:2]) > 12 and int(s[2:4]) > 12:
        return 'NA'
    elif int(s[0:2]) > 12 and int(s[2:4]) <= 12:
        return 'MMYY'
    elif int(s[0:2]) <= 12 and int(s[2:4]) > 12:
        return 'YYMM'
    else:
        return 'AMBIGUOUS'

=======
Suggestion 8

def is_valid_month(m):
    return 1 <= m and m <= 12

s = input()
a = int(s[:2])
b = int(s[2:])

=======
Suggestion 9

def main():
    s = input()
    m1 = int(s[0:2])
    m2 = int(s[2:4])
    if 1 <= m1 <= 12 and 1 <= m2 <= 12:
        print('AMBIGUOUS')
    elif 1 <= m1 <= 12:
        print('MMYY')
    elif 1 <= m2 <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 10

def is_valid_month(n):
    return 1 <= n <= 12
