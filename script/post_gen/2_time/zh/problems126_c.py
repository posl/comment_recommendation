Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if 1<=int(s[0:2])<=12 and 1<=int(s[2:4])<=12:
        print("AMBIGUOUS")
    elif 1<=int(s[0:2])<=12:
        print("MMYY")
    elif 1<=int(s[2:4])<=12:
        print("YYMM")
    else:
        print("NA")

main()

=======
Suggestion 2

def is_valid_month(month):
    return 1 <= month <= 12

=======
Suggestion 3

def main():
    S = input()
    m1 = int(S[0:2])
    m2 = int(S[2:4])
    if m1 < 1 or m1 > 12:
        if m2 < 1 or m2 > 12:
            print('NA')
        else:
            print('YYMM')
    else:
        if m2 < 1 or m2 > 12:
            print('MMYY')
        else:
            print('AMBIGUOUS')

=======
Suggestion 4

def check(s):
    if 1 <= s <= 12:
        return True
    else:
        return False

=======
Suggestion 5

def check(s):
    if int(s[0:2]) > 12 or int(s[0:2]) == 0:
        return False
    if int(s[2:]) > 12 or int(s[2:]) == 0:
        return False
    return True

s = input()

=======
Suggestion 6

def main():
    s = input()
    # print(s)
    # print(s[0:2])
    # print(s[2:4])
    # print(s[0:2] in range(1,13))
    # print(s[2:4] in range(1,13))
    if 1 <= int(s[0:2]) <= 12 and 1 <= int(s[2:4]) <= 12:
        print('AMBIGUOUS')
    elif 1 <= int(s[0:2]) <= 12 and not 1 <= int(s[2:4]) <= 12:
        print('MMYY')
    elif not 1 <= int(s[0:2]) <= 12 and 1 <= int(s[2:4]) <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 7

def check(s):
    if int(s) > 0 and int(s) <= 12:
        return True
    else:
        return False

=======
Suggestion 8

def main():
    S = input()
    s1 = S[:2]
    s2 = S[2:]
    if (int(s1) in range(1, 13)) and (int(s2) in range(1, 13)):
        print("AMBIGUOUS")
    elif (int(s1) in range(1, 13)) and (int(s2) not in range(1, 13)):
        print("MMYY")
    elif (int(s1) not in range(1, 13)) and (int(s2) in range(1, 13)):
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 9

def check(s):
    if 1 <= int(s[2:]) <= 12 and 1 <= int(s[:2]) <= 12:
        return "AMBIGUOUS"
    elif 1 <= int(s[2:]) <= 12:
        return "YYMM"
    elif 1 <= int(s[:2]) <= 12:
        return "MMYY"
    else:
        return "NA"

=======
Suggestion 10

def main():
    S = input()
    S1 = int(S[0:2])
    S2 = int(S[2:4])
    if 1 <= S1 <= 12 and 1 <= S2 <= 12:
        print("AMBIGUOUS")
    elif 1 <= S1 <= 12 and not 1 <= S2 <= 12:
        print("MMYY")
    elif not 1 <= S1 <= 12 and 1 <= S2 <= 12:
        print("YYMM")
    else:
        print("NA")
