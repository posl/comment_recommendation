Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if 1 <= int(s[2:4]) <= 12 and 1 <= int(s[0:2]) <= 12:
        print("AMBIGUOUS")
    elif 1 <= int(s[2:4]) <= 12:
        print("YYMM")
    elif 1 <= int(s[0:2]) <= 12:
        print("MMYY")
    else:
        print("NA")

=======
Suggestion 2

def main():
    S = input()
    if int(S[0:2]) >= 1 and int(S[0:2]) <= 12:
        if int(S[2:4]) >= 1 and int(S[2:4]) <= 12:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if int(S[2:4]) >= 1 and int(S[2:4]) <= 12:
            print("YYMM")
        else:
            print("NA")

=======
Suggestion 3

def main():
    s = input()
    if int(s[2:4]) <= 12 and int(s[2:4]) > 0 and int(s[0:2]) <= 12 and int(s[0:2]) > 0:
        print("AMBIGUOUS")
    elif int(s[2:4]) <= 12 and int(s[2:4]) > 0:
        print("YYMM")
    elif int(s[0:2]) <= 12 and int(s[0:2]) > 0:
        print("MMYY")
    else:
        print("NA")

=======
Suggestion 4

def main():
    S = input()
    YY = int(S[0:2])
    MM = int(S[2:4])
    if (0 < MM and MM < 13) and (0 < YY and YY < 13):
        print("AMBIGUOUS")
    elif (0 < MM and MM < 13) and (not (0 < YY and YY < 13)):
        print("MMYY")
    elif (not (0 < MM and MM < 13)) and (0 < YY and YY < 13):
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 5

def check(s):
    if (s[0] == '0' and s[1] == '0') or (s[2] == '0' and s[3] == '0'):
        return 'NA'
    elif (s[0] == '0' or s[0] == '1') and (s[2] == '0' or s[2] == '1'):
        return 'AMBIGUOUS'
    elif s[0] == '0' or s[0] == '1':
        return 'YYMM'
    elif s[2] == '0' or s[2] == '1':
        return 'MMYY'
    else:
        return 'NA'

s = input()
print(check(s))

=======
Suggestion 6

def check_YYMM(S):
    YY = int(S[0:2])
    MM = int(S[2:4])
    if 1 <= YY <= 12 and 1 <= MM <= 12:
        return 'AMBIGUOUS'
    elif 1 <= YY <= 12 and 1 <= MM <= 12:
        return 'YYMM'
    elif 1 <= MM <= 12 and 1 <= YY <= 12:
        return 'MMYY'
    else:
        return 'NA'

S = input()
print(check_YYMM(S))

=======
Suggestion 7

def isYYMM(S):
    if int(S[2:]) <= 12 and int(S[2:]) >= 1:
        return True
    else:
        return False

=======
Suggestion 8

def   YYMM ( s ): 
     if   int ( s [ 0 : 2 ])   >   12 : 
         return   False 
     else : 
         return   True

=======
Suggestion 9

def is_valid_month(month):
    return int(month) > 0 and int(month) < 13

=======
Suggestion 10

def main():
    # Read input data
    S = input()
    # YYMM and MMYY are the two possible formats
    YYMM = "YYMM"
    MMYY = "MMYY"
    # Check if S is valid in YYMM format
    YYMM_valid = False
    if int(S[:2]) >= 1 and int(S[:2]) <= 12:
        if int(S[2:]) >= 1 and int(S[2:]) <= 99:
            YYMM_valid = True
    # Check if S is valid in MMYY format
    MMYY_valid = False
    if int(S[2:]) >= 1 and int(S[2:]) <= 12:
        if int(S[:2]) >= 1 and int(S[:2]) <= 99:
            MMYY_valid = True
    # Output the result
    if YYMM_valid and MMYY_valid:
        print("AMBIGUOUS")
    elif YYMM_valid:
        print(YYMM)
    elif MMYY_valid:
        print(MMYY)
    else:
        print("NA")

main()

Problem 127: B - Algae
