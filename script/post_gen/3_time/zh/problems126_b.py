Synthesizing 10/10 solutions

=======
Suggestion 1

def check(s):
    if int(s[:2]) > 12:
        return False
    if int(s[2:]) > 12:
        return False
    return True

=======
Suggestion 2

def main():
    s = input()
    if 1 <= int(s[:2]) <= 12 and 1 <= int(s[2:]) <= 12:
        print('AMBIGUOUS')
    elif 1 <= int(s[:2]) <= 12:
        print('MMYY')
    elif 1 <= int(s[2:]) <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 3

def main():
    S = input()
    S1 = int(S[:2])
    S2 = int(S[2:])
    if S1 in range(1, 13) and S2 in range(1, 13):
        print('AMBIGUOUS')
    elif S1 in range(1, 13):
        print('MMYY')
    elif S2 in range(1, 13):
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 4

def main():
    S = input()
    s1 = int(S[0:2])
    s2 = int(S[2:4])
    if 1 <= s1 <= 12 and 1 <= s2 <= 12:
        print("AMBIGUOUS")
    elif 1 <= s1 <= 12:
        print("MMYY")
    elif 1 <= s2 <= 12:
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 5

def main():
    S = input()
    #print(S)
    if (int(S[0:2]) > 0 and int(S[0:2]) <= 12) and (int(S[2:4]) > 0 and int(S[2:4]) <= 12):
        print("AMBIGUOUS")
    elif (int(S[0:2]) > 0 and int(S[0:2]) <= 12) and (int(S[2:4]) > 12 and int(S[2:4]) <= 99):
        print("MMYY")
    elif (int(S[0:2]) > 12 and int(S[0:2]) <= 99) and (int(S[2:4]) > 0 and int(S[2:4]) <= 12):
        print("YYMM")
    elif (int(S[0:2]) > 12 and int(S[0:2]) <= 99) and (int(S[2:4]) > 12 and int(S[2:4]) <= 99):
        print("NA")

=======
Suggestion 6

def main():
    S = input()
    if (1 <= int(S[0:2]) <= 12) and (1 <= int(S[2:4]) <= 12):
        print('AMBIGUOUS')
    elif (1 <= int(S[0:2]) <= 12) and (1 <= int(S[2:4]) <= 99):
        print('MMYY')
    elif (1 <= int(S[0:2]) <= 99) and (1 <= int(S[2:4]) <= 12):
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 7

def main():
    s = input()
    s1 = s[:2]
    s2 = s[2:]
    if s1[0] == '0' and s1[1] == '0':
        if s2[0] == '0' and s2[1] == '0':
            print('NA')
        else:
            print('MMYY')
    elif s2[0] == '0' and s2[1] == '0':
        if s1[0] == '0' and s1[1] == '0':
            print('NA')
        else:
            print('YYMM')
    elif s1[0] == '0' and s1[1] != '0':
        if s2[0] == '0' and s2[1] != '0':
            print('NA')
        else:
            print('MMYY')
    elif s2[0] == '0' and s2[1] != '0':
        if s1[0] == '0' and s1[1] != '0':
            print('NA')
        else:
            print('YYMM')
    else:
        print('AMBIGUOUS')

=======
Suggestion 8

def check(s):
    if int(s[0:2]) > 0 and int(s[0:2]) < 13:
        return True
    else:
        return False

s = input()

=======
Suggestion 9

def isMonth(month):
    if month > 0 and month < 13:
        return True
    else:
        return False

=======
Suggestion 10

def check_yymm(s):
    if int(s[2:]) <= 12 and int(s[2:]) >= 1:
        return True
    else:
        return False
