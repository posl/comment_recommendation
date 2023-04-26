Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S[0] == "0" and S[1] == "0" and S[2] == "0" and S[3] == "0":
        print("NA")
    elif S[0] == "0" and S[1] == "0" and S[2] == "0" and S[3] != "0":
        print("NA")
    elif S[0] == "0" and S[1] == "0" and S[2] != "0" and S[3] == "0":
        print("NA")
    elif S[0] == "0" and S[1] == "0" and S[2] != "0" and S[3] != "0":
        print("NA")
    elif S[0] == "0" and S[1] != "0" and S[2] == "0" and S[3] == "0":
        print("NA")
    elif S[0] == "0" and S[1] != "0" and S[2] == "0" and S[3] != "0":
        print("NA")
    elif S[0] == "0" and S[1] != "0" and S[2] != "0" and S[3] == "0":
        print("NA")
    elif S[0] == "0" and S[1] != "0" and S[2] != "0" and S[3] != "0":
        if S[2] == "0" and S[3] == "0":
            print("NA")
        elif S[2] == "0" and S[3] != "0":
            print("NA")
        elif S[2] != "0" and S[3] == "0":
            print("NA")
        elif S[2] != "0" and S[3] != "0":
            print("YYMM")
    elif S[0] != "0" and S[1] == "0" and S[2] == "0" and S[3] == "0":
        print("NA")
    elif S[0] != "0" and S[1] == "0" and S[2

=======
Suggestion 2

def main():
    s = input()
    if s[0] == '0' and s[1] == '0' and s[2] == '0' and s[3] == '0':
        print("NA")
    elif s[0] == '0' and s[1] == '0' and s[2] != '0' and s[3] != '0':
        print("YYMM")
    elif s[0] != '0' and s[1] != '0' and s[2] == '0' and s[3] == '0':
        print("YYMM")
    elif s[0] != '0' and s[1] != '0' and s[2] != '0' and s[3] != '0':
        print("AMBIGUOUS")
    else:
        print("MMYY")

=======
Suggestion 3

def main():
    s = input()
    if s[0] == "0" and s[1] == "0":
        if s[2] == "0" and s[3] == "0":
            print("NA")
        else:
            print("YYMM")
    elif s[2] == "0" and s[3] == "0":
        print("MMYY")
    elif int(s[0]) > 1:
        if int(s[2]) > 1:
            print("NA")
        else:
            print("YYMM")
    elif int(s[2]) > 1:
        if int(s[0]) > 1:
            print("NA")
        else:
            print("MMYY")
    else:
        print("AMBIGUOUS")

=======
Suggestion 4

def main():
    s = input()
    a = int(s[:2])
    b = int(s[2:])
    if 1 <= a <= 12 and 1 <= b <= 12:
        print('AMBIGUOUS')
    elif 1 <= a <= 12:
        print('MMYY')
    elif 1 <= b <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 5

def main():
    S = input()
    if S[0] == "0" and S[1] == "0":
        if S[2] == "0" and S[3] == "0":
            print("NA")
        elif 1 <= int(S[2]) and int(S[2]) <= 9 and 0 <= int(S[3]) and int(S[3]) <= 9:
            print("YYMM")
        elif 1 <= int(S[3]) and int(S[3]) <= 9 and 0 <= int(S[2]) and int(S[2]) <= 9:
            print("MMYY")
        else:
            print("NA")
    elif 1 <= int(S[0]) and int(S[0]) <= 9 and 0 <= int(S[1]) and int(S[1]) <= 9:
        if S[2] == "0" and S[3] == "0":
            print("YYMM")
        elif 1 <= int(S[2]) and int(S[2]) <= 9 and 0 <= int(S[3]) and int(S[3]) <= 9:
            print("AMBIGUOUS")
        elif 1 <= int(S[3]) and int(S[3]) <= 9 and 0 <= int(S[2]) and int(S[2]) <= 9:
            print("AMBIGUOUS")
        else:
            print("YYMM")
    elif 1 <= int(S[1]) and int(S[1]) <= 9 and 0 <= int(S[0]) and int(S[0]) <= 9:
        if S[2] == "0" and S[3] == "0":
            print("MMYY")
        elif 1 <= int(S[2]) and int(S[2]) <= 9 and 0 <= int(S[3]) and int(S[3]) <= 9:
            print("MMYY")
        elif 1 <= int(S[3]) and int(S[3]) <= 9 and 0 <= int(S[2]) and int(S[2]) <= 9:
            print("AMBIGUOUS")
        else:
            print("NA")
    else:
        print("NA")

=======
Suggestion 6

def main():
    s = input()
    if s[0] in "01" and s[1] in "0123456789" and s[2] in "01" and s[3] in "0123456789":
        print("AMBIGUOUS")
    elif s[0] in "01" and s[1] in "0123456789" and s[2] in "0" and s[3] in "0123456789":
        print("YYMM")
    elif s[0] in "0" and s[1] in "0123456789" and s[2] in "01" and s[3] in "0123456789":
        print("MMYY")
    else:
        print("NA")

=======
Suggestion 7

def main():
    s = input()
    yymm = int(s[:2]) <= 12 and int(s[2:]) <= 12
    mmyy = int(s[:2]) <= 12 and int(s[2:]) <= 12
    if yymm and mmyy:
        print("AMBIGUOUS")
    elif yymm:
        print("YYMM")
    elif mmyy:
        print("MMYY")
    else:
        print("NA")

=======
Suggestion 8

def main():
    s = input()
    if s[0] == '0':
        if s[1] == '0':
            print('NA')
        else:
            if s[2] == '0':
                if s[3] == '0':
                    print('NA')
                else:
                    print('YYMM')
            else:
                if s[3] == '0':
                    print('NA')
                else:
                    print('AMBIGUOUS')
    else:
        if s[1] == '0':
            if s[2] == '0':
                if s[3] == '0':
                    print('NA')
                else:
                    print('MMYY')
            else:
                if s[3] == '0':
                    print('NA')
                else:
                    print('AMBIGUOUS')
        else:
            if s[2] == '0':
                if s[3] == '0':
                    print('NA')
                else:
                    print('YYMM')
            else:
                if s[3] == '0':
                    print('NA')
                else:
                    print('AMBIGUOUS')

=======
Suggestion 9

def main():
    s = input()
    s1 = s[0:2]
    s2 = s[2:4]
    if int(s1) in range(1,13) and int(s2) in range(1,13):
        print("AMBIGUOUS")
    elif int(s1) in range(1,13) and int(s2) in range(13,99):
        print("MMYY")
    elif int(s1) in range(13,99) and int(s2) in range(1,13):
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 10

def main():
    S = input()
    S1 = S[0:2]
    S2 = S[2:4]
    if S1 == "00" or S1 == "01" or S1 == "02" or S1 == "03" or S1 == "04" or S1 == "05" or S1 == "06" or S1 == "07" or S1 == "08" or S1 == "09" or S1 == "10" or S1 == "11" or S1 == "12":
        if S2 == "00" or S2 == "01" or S2 == "02" or S2 == "03" or S2 == "04" or S2 == "05" or S2 == "06" or S2 == "07" or S2 == "08" or S2 == "09" or S2 == "10" or S2 == "11" or S2 == "12":
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if S2 == "00" or S2 == "01" or S2 == "02" or S2 == "03" or S2 == "04" or S2 == "05" or S2 == "06" or S2 == "07" or S2 == "08" or S2 == "09" or S2 == "10" or S2 == "11" or S2 == "12":
            print("YYMM")
        else:
            print("NA")
