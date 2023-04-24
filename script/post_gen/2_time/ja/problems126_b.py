Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if int(s[0:2]) <= 12 and int(s[2:4]) <= 12:
        print('AMBIGUOUS')
    elif int(s[0:2]) <= 12:
        print('MMYY')
    elif int(s[2:4]) <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 2

def main():
    s = input()
    if s[0] == '0' and s[1] == '0':
        if s[2] == '0' or s[3] == '0':
            print('NA')
        else:
            print('MMYY')
    elif s[0] == '0' or s[1] == '0':
        if s[2] == '0' and s[3] == '0':
            print('NA')
        else:
            print('YYMM')
    else:
        if s[2] == '0' or s[3] == '0':
            print('YYMM')
        else:
            print('AMBIGUOUS')

=======
Suggestion 3

def main():
    s = input()
    if int(s[:2]) > 12 and int(s[2:]) > 12:
        print("NA")
    elif int(s[:2]) > 12:
        print("YYMM")
    elif int(s[2:]) > 12:
        print("MMYY")
    else:
        print("AMBIGUOUS")

=======
Suggestion 4

def main():
    s = input()
    if (s[0] == "0" and s[1] == "0") or (s[2] == "0" and s[3] == "0"):
        print("NA")
    elif (s[0] == "0" and s[1] == "0") and (s[2] == "0" and s[3] == "0"):
        print("NA")
    elif (s[0] == "0" and s[1] == "0") and (s[2] == "0" and s[3] != "0"):
        print("MMYY")
    elif (s[0] == "0" and s[1] == "0") and (s[2] != "0" and s[3] == "0"):
        print("MMYY")
    elif (s[0] == "0" and s[1] == "0") and (s[2] != "0" and s[3] != "0"):
        print("MMYY")
    elif (s[0] != "0" and s[1] == "0") and (s[2] == "0" and s[3] == "0"):
        print("YYMM")
    elif (s[0] != "0" and s[1] == "0") and (s[2] == "0" and s[3] != "0"):
        print("MMYY")
    elif (s[0] != "0" and s[1] == "0") and (s[2] != "0" and s[3] == "0"):
        print("AMBIGUOUS")
    elif (s[0] != "0" and s[1] == "0") and (s[2] != "0" and s[3] != "0"):
        print("AMBIGUOUS")
    elif (s[0] != "0" and s[1] != "0") and (s[2] == "0" and s[3] == "0"):
        print("YYMM")
    elif (s[0] != "0" and s[1] != "0") and (s[2] == "0" and s[3] != "0"):
        print

=======
Suggestion 5

def main():
    S = input()
    Y = int(S[0:2])
    M = int(S[2:4])
    if Y >= 1 and Y <= 12 and M >= 1 and M <= 12:
        print('AMBIGUOUS')
    elif Y >= 1 and Y <= 12:
        print('YYMM')
    elif M >= 1 and M <= 12:
        print('MMYY')
    else:
        print('NA')

=======
Suggestion 6

def main():
    S = input()
    if (int(S[2:4]) >= 1) and (int(S[2:4]) <= 12) and (int(S[0:2]) >= 1) and (int(S[0:2]) <= 12):
        print("AMBIGUOUS")
    elif (int(S[2:4]) >= 1) and (int(S[2:4]) <= 12):
        print("YYMM")
    elif (int(S[0:2]) >= 1) and (int(S[0:2]) <= 12):
        print("MMYY")
    else:
        print("NA")

=======
Suggestion 7

def main():
    s = input()
    yymm = s[0:2]
    mmyy = s[2:4]
    if 0 < int(yymm) <= 12 and 0 < int(mmyy) <= 12:
        print("AMBIGUOUS")
    elif 0 < int(yymm) <= 12:
        print("YYMM")
    elif 0 < int(mmyy) <= 12:
        print("MMYY")
    else:
        print("NA")

=======
Suggestion 8

def main():
    S = input()
    S1 = S[0:2]
    S2 = S[2:4]

    if(1 <= int(S1) <= 12 and 1 <= int(S2) <= 12):
        print("AMBIGUOUS")
    elif(1 <= int(S1) <= 12 and not(1 <= int(S2) <= 12)):
        print("MMYY")
    elif(not(1 <= int(S1) <= 12) and 1 <= int(S2) <= 12):
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 9

def main():
    s = input()
    #YYMM
    if int(s[0:2]) <= 12 and int(s[0:2]) >= 1 and int(s[2:4]) <= 12 and int(s[2:4]) >= 1:
        print("AMBIGUOUS")
    elif int(s[0:2]) <= 12 and int(s[0:2]) >= 1:
        print("MMYY")
    elif int(s[2:4]) <= 12 and int(s[2:4]) >= 1:
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 10

def is_valid_month(month):
    if 0 < int(month) <= 12:
        return True
    else:
        return False
