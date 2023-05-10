Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()

    a = int(s[0:2])
    b = int(s[2:4])

    if 1 <= a and a <= 12:
        if 1 <= b and b <= 12:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if 1 <= b and b <= 12:
            print("YYMM")
        else:
            print("NA")

=======
Suggestion 2

def main():
    S = input()
    S1 = int(S[0:2])
    S2 = int(S[2:4])
    if S1 >= 1 and S1 <= 12 and S2 >= 1 and S2 <= 12:
        print('AMBIGUOUS')
    elif S1 >= 1 and S1 <= 12:
        print('MMYY')
    elif S2 >= 1 and S2 <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 3

def main():
    S = input()
    if 1 <= int(S[0:2]) <= 12:
        if 1 <= int(S[2:4]) <= 12:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if 1 <= int(S[2:4]) <= 12:
            print("YYMM")
        else:
            print("NA")

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    S = input()
    s1 = int(S[0:2])
    s2 = int(S[2:4])
    if 0 < s1 and s1 < 13:
        if 0 < s2 and s2 < 13:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if 0 < s2 and s2 < 13:
            print("YYMM")
        else:
            print("NA")

=======
Suggestion 6

def is_month(mm):
    if 1 <= int(mm) <= 12:
        return True
    else:
        return False

s = input()

=======
Suggestion 7

def main():
    S = input()
    if 0 < int(S[:2]) < 13 and 0 < int(S[2:]) < 13:
        print("AMBIGUOUS")
    elif 0 < int(S[:2]) < 13:
        print("MMYY")
    elif 0 < int(S[2:]) < 13:
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 8

def main():
    S = input()
    if int(S[0:2]) > 12:
        if int(S[2:4]) > 12:
            print("NA")
        else:
            print("YYMM")
    else:
        if int(S[2:4]) > 12:
            print("MMYY")
        else:
            print("AMBIGUOUS")

=======
Suggestion 9

def main():
    s = input()
    a = int(s[0:2])
    b = int(s[2:4])
    if a == 0 and b == 0:
        print('NA')
    elif a == 0 and b != 0:
        print('YYMM')
    elif a != 0 and b == 0:
        print('MMYY')
    elif 1 <= a <= 12 and 1 <= b <= 12:
        print('AMBIGUOUS')
    elif 1 <= a <= 12 and not(1 <= b <= 12):
        print('MMYY')
    elif not(1 <= a <= 12) and 1 <= b <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 10

def main():
    s = input()
    a = int(s[:2])
    b = int(s[2:])

    if 1 <= a <= 12 and 1 <= b <= 12:
        print("AMBIGUOUS")
    elif 1 <= a <= 12:
        print("MMYY")
    elif 1 <= b <= 12:
        print("YYMM")
    else:
        print("NA")
