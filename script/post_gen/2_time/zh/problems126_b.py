Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    a = int(s[0:2])
    b = int(s[2:4])
    if 0 < a < 13 and 0 < b < 13:
        print("AMBIGUOUS")
    elif 0 < a < 13 and 0 <= b < 100:
        print("MMYY")
    elif 0 <= a < 100 and 0 < b < 13:
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 2

def is_valid_month(month):
    if month > 0 and month < 13:
        return True
    else:
        return False

=======
Suggestion 3

def main():
    s = input()
    if s[0] == '0' and s[1] == '0':
        print('NA')
    elif s[0] == '0' and s[1] != '0':
        if int(s[2:4]) >= 1 and int(s[2:4]) <= 12:
            print('YYMM')
        else:
            print('NA')
    elif s[0] != '0' and s[1] == '0':
        if int(s[0:2]) >= 1 and int(s[0:2]) <= 12:
            print('MMYY')
        else:
            print('NA')
    else:
        if int(s[0:2]) >= 1 and int(s[0:2]) <= 12:
            if int(s[2:4]) >= 1 and int(s[2:4]) <= 12:
                print('AMBIGUOUS')
            else:
                print('MMYY')
        else:
            if int(s[2:4]) >= 1 and int(s[2:4]) <= 12:
                print('YYMM')
            else:
                print('NA')

=======
Suggestion 4

def problem126_b():
    s = input()
    if 1 <= int(s[0:2]) <= 12:
        if 1 <= int(s[2:4]) <= 12:
            print('AMBIGUOUS')
            return
        else:
            print('MMYY')
            return
    elif 1 <= int(s[2:4]) <= 12:
        print('YYMM')
        return
    else:
        print('NA')
        return

problem126_b()

=======
Suggestion 5

def main():
    S = input()
    S1 = S[0:2]
    S2 = S[2:4]
    if 1 <= int(S1) <= 12:
        if 1 <= int(S2) <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if 1 <= int(S2) <= 12:
            print('YYMM')
        else:
            print('NA')

=======
Suggestion 6

def checkYear(x):
    if x >= 0 and x <= 99:
        return True
    return False

=======
Suggestion 7

def main():
    s = input()
    s1 = s[0:2]
    s2 = s[2:4]
    if int(s1) > 12 or int(s1) == 0:
        if int(s2) > 12 or int(s2) == 0:
            print("NA")
        else:
            print("YYMM")
    elif int(s2) > 12 or int(s2) == 0:
        if int(s1) > 12 or int(s1) == 0:
            print("NA")
        else:
            print("MMYY")
    else:
        print("AMBIGUOUS")

=======
Suggestion 8

def main():
    S = input()
    #print(S)
    S1 = S[0:2]
    S2 = S[2:4]
    #print(S1)
    #print(S2)
    if(int(S1) > 12 and int(S2) > 12):
        print("NA")
    elif(int(S1) > 12 and int(S2) <= 12):
        print("YYMM")
    elif(int(S1) <= 12 and int(S2) > 12):
        print("MMYY")
    elif(int(S1) <= 12 and int(S2) <= 12):
        print("AMBIGUOUS")

=======
Suggestion 9

def main():
    S = input()
    if S[0] == "0" and S[1] == "0" and S[2] == "0" and S[3] == "0":
        print("NA")
    elif S[0] == "0" and S[1] == "0" and S[2] == "0" and S[3] != "0":
        print("NA")
    elif S[0] == "0" and S[1] == "0" and S[2] != "0" and S[3] == "0":
        print("NA")
    elif S[0] == "0" and S[1] == "0" and S[2] != "0" and S[3] != "0":
        print("MMYY")
    elif S[0] == "0" and S[1] != "0" and S[2] == "0" and S[3] == "0":
        print("NA")
    elif S[0] == "0" and S[1] != "0" and S[2] == "0" and S[3] != "0":
        print("NA")
    elif S[0] == "0" and S[1] != "0" and S[2] != "0" and S[3] == "0":
        print("NA")
    elif S[0] == "0" and S[1] != "0" and S[2] != "0" and S[3] != "0":
        print("AMBIGUOUS")
    elif S[0] != "0" and S[1] == "0" and S[2] == "0" and S[3] == "0":
        print("NA")
    elif S[0] != "0" and S[1] == "0" and S[2] == "0" and S[3] != "0":
        print("NA")
    elif S[0] != "0" and S[1] == "0" and S[2] != "0" and S[3] == "0":
        print("NA")
    elif S[0] != "0" and S[1] == "0" and S[2] != "0

=======
Suggestion 10

def main():
    S = input()
    S = [int(i) for i in S]
    if S[0] == 0:
        if S[1] == 0:
            if S[2] == 0:
                print("NA")
            else:
                if S[3] == 0:
                    print("NA")
                else:
                    print("YYMM")
        else:
            if S[2] == 0:
                if S[3] == 0:
                    print("NA")
                else:
                    print("YYMM")
            else:
                if S[3] == 0:
                    print("NA")
                else:
                    print("YYMM")
    else:
        if S[1] == 0:
            if S[2] == 0:
                if S[3] == 0:
                    print("NA")
                else:
                    print("MMYY")
            else:
                if S[3] == 0:
                    print("NA")
                else:
                    print("MMYY")
        else:
            if S[2] == 0:
                if S[3] == 0:
                    print("NA")
                else:
                    print("MMYY")
            else:
                if S[3] == 0:
                    print("NA")
                else:
                    print("MMYY")
