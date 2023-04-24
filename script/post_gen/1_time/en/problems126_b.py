Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if 1 <= int(s[0:2]) <= 12 and 1 <= int(s[2:4]) <= 12:
        print('AMBIGUOUS')
    elif 1 <= int(s[0:2]) <= 12:
        print('MMYY')
    elif 1 <= int(s[2:4]) <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 2

def main():
    S = input()
    if int(S[0:2]) > 0 and int(S[0:2]) < 13:
        if int(S[2:4]) > 0 and int(S[2:4]) < 13:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    elif int(S[2:4]) > 0 and int(S[2:4]) < 13:
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 3

def main():
    S = input()
    if S[0:2] >= '01' and S[0:2] <= '12':
        if S[2:4] >= '01' and S[2:4] <= '12':
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if S[2:4] >= '01' and S[2:4] <= '12':
            print('YYMM')
        else:
            print('NA')

=======
Suggestion 4

def main():
    S = input()
    a = int(S[0:2])
    b = int(S[2:4])
    if 1 <= a <= 12:
        if 1 <= b <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    elif 1 <= b <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 5

def main():
    s = input()
    if int(s[:2]) > 12:
        if int(s[2:]) > 12:
            print('NA')
        else:
            print('YYMM')
    else:
        if int(s[2:]) > 12:
            print('MMYY')
        else:
            print('AMBIGUOUS')

=======
Suggestion 6

def main():
    s = input()
    if (int(s[:2]) > 0 and int(s[:2]) < 13) and (int(s[2:]) > 0 and int(s[2:]) < 13):
        print('AMBIGUOUS')
    elif (int(s[:2]) > 0 and int(s[:2]) < 13):
        print('MMYY')
    elif (int(s[2:]) > 0 and int(s[2:]) < 13):
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 7

def main():
    s = input()
    s1 = s[0:2]
    s2 = s[2:4]
    if int(s1) > 0 and int(s1) < 13:
        if int(s2) > 0 and int(s2) < 13:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    elif int(s2) > 0 and int(s2) < 13:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 8

def main():
    S = input()
    S1 = S[0:2]
    S2 = S[2:4]
    if int(S1) > 0 and int(S1) < 13:
        if int(S2) > 0 and int(S2) < 13:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if int(S2) > 0 and int(S2) < 13:
            print("YYMM")
        else:
            print("NA")

=======
Suggestion 9

def check_yymm(s):
    year = int(s[0:2])
    month = int(s[2:4])
    if month >= 1 and month <= 12:
        return True
    else:
        return False

=======
Suggestion 10

def main():
    S = input()
    S = list(S)
    S1 = S[:2]
    S2 = S[2:]
    S1 = int("".join(S1))
    S2 = int("".join(S2))
    if (S1 < 13 and S1 > 0) and (S2 < 13 and S2 > 0):
        print("AMBIGUOUS")
    elif (S1 < 13 and S1 > 0) and (S2 >= 13 or S2 == 0):
        print("MMYY")
    elif (S1 >= 13 or S1 == 0) and (S2 < 13 and S2 > 0):
        print("YYMM")
    else:
        print("NA")
