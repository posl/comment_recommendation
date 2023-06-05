Synthesizing 10/10 solutions

=======
Suggestion 1

def is_valid_month(month):
    return month >= 1 and month <= 12

=======
Suggestion 2

def main():
    n = input()
    if 1 <= int(n[0:2]) <= 12:
        if 1 <= int(n[2:4]) <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    elif 1 <= int(n[2:4]) <= 12:
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

def main():
    S = input()
    if S[0:2] >= "01" and S[0:2] <= "12" and S[2:4] >= "01" and S[2:4] <= "12":
        print("AMBIGUOUS")
    elif S[0:2] >= "01" and S[0:2] <= "12":
        print("MMYY")
    elif S[2:4] >= "01" and S[2:4] <= "12":
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 5

def check(s):
    if s[0] == '0' and s[1] == '0':
        return False
    if s[2] == '0' and s[3] == '0':
        return False
    return True

=======
Suggestion 6

def isMonth(s):
    if s[0] == '0':
        return False
    elif s[0] == '1':
        if ord(s[1]) >= ord('0') and ord(s[1]) <= ord('2'):
            return True
        else:
            return False
    elif s[0] == '2':
        if ord(s[1]) >= ord('0') and ord(s[1]) <= ord('2'):
            return True
        else:
            return False
    else:
        return False

=======
Suggestion 7

def main():
    S = input()
    a = S[0:2]
    b = S[2:4]
    if 1 <= int(a) <= 12 and 1 <= int(b) <= 12:
        print("AMBIGUOUS")
    elif 1 <= int(a) <= 12 and (int(b) == 0 or int(b) > 12):
        print("MMYY")
    elif (int(a) == 0 or int(a) > 12) and 1 <= int(b) <= 12:
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 8

def test():
    s = input()
    a = int(s[:2])
    b = int(s[2:])
    if a in range(1,13) and b in range(1,13):
        print("AMBIGUOUS")
    elif a in range(1,13) and b not in range(1,13):
        print("MMYY")
    elif a not in range(1,13) and b in range(1,13):
        print("YYMM")
    else:
        print("NA")

test()

=======
Suggestion 9

def check(s):
    if 1 <= int(s[0:2]) <= 12 and 1 <= int(s[2:4]) <= 12:
        return "AMBIGUOUS"
    elif 1 <= int(s[0:2]) <= 12:
        return "MMYY"
    elif 1 <= int(s[2:4]) <= 12:
        return "YYMM"
    else:
        return "NA"

=======
Suggestion 10

def main():
    s = input()
    s1 = s[0:2]
    s2 = s[2:4]

    if (1 <= int(s1) <= 12) and (1 <= int(s2) <= 12):
        print("AMBIGUOUS")
    elif (1 <= int(s1) <= 12) and (1 > int(s2) or int(s2) > 12):
        print("MMYY")
    elif (1 > int(s1) or int(s1) > 12) and (1 <= int(s2) <= 12):
        print("YYMM")
    else:
        print("NA")
