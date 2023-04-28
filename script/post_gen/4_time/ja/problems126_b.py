Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    a = int(s[:2])
    b = int(s[2:])
    if 1 <= a <= 12 and 1 <= b <= 12:
        print('AMBIGUOUS')
    elif 1 <= a <= 12 and (b == 0 or b > 12):
        print('MMYY')
    elif 1 <= b <= 12 and (a == 0 or a > 12):
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 2

def main():
    S = input()
    S1 = int(S[0:2])
    S2 = int(S[2:4])
    if 1 <= S1 <= 12 and 1 <= S2 <= 12:
        print('AMBIGUOUS')
    elif 1 <= S1 <= 12:
        print('MMYY')
    elif 1 <= S2 <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 3

def main():
    S = input()
    a = int(S[0:2])
    b = int(S[2:4])
    if 1 <= a <= 12:
        if 1 <= b <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if 1 <= b <= 12:
            print('YYMM')
        else:
            print('NA')

=======
Suggestion 4

def main():
    s = input()
    yy = int(s[:2])
    mm = int(s[2:])
    if 1 <= yy <= 12:
        if 1 <= mm <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if 1 <= mm <= 12:
            print('YYMM')
        else:
            print('NA')

=======
Suggestion 5

def main():
    S = input()
    S1 = S[0:2]
    S2 = S[2:4]
    if (1 <= int(S1) <= 12) and (1 <= int(S2) <= 12):
        print("AMBIGUOUS")
    elif (1 <= int(S1) <= 12) and (13 <= int(S2) <= 99):
        print("MMYY")
    elif (13 <= int(S1) <= 99) and (1 <= int(S2) <= 12):
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 6

def main():
    s = input()
    y1 = int(s[:2])
    y2 = int(s[2:])
    if y1 >= 1 and y1 <= 12 and y2 >= 1 and y2 <= 12:
        print('AMBIGUOUS')
    elif y1 >= 1 and y1 <= 12:
        print('MMYY')
    elif y2 >= 1 and y2 <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 7

def main():
    S = input()
    if S[0:2] in ['00','01','02','03','04','05','06','07','08','09']:
        if S[2:4] in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if S[2:4] in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            print('YYMM')
        else:
            print('NA')

=======
Suggestion 8

def is_yymm(s):
    if int(s[0:2]) >= 1 and int(s[0:2]) <= 12:
        return True
    else:
        return False

=======
Suggestion 9

def is_month(s):
    return 1 <= int(s) <= 12

s = input()
a = s[:2]
b = s[2:]

=======
Suggestion 10

def isMonth(n):
    return 1 <= n <= 12

s = input()
a = int(s[:2])
b = int(s[2:])
