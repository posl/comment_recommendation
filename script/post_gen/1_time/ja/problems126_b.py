Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == '0' and s[1] == '0' and s[2] == '0' and s[3] == '0':
        print('NA')
    elif s[0] == '0' and s[1] == '0':
        print('NA')
    elif s[2] == '0' and s[3] == '0':
        print('NA')
    elif s[0] == '0' and s[1] == '1':
        print('YYMM')
    elif s[0] == '0' and s[1] == '2':
        print('YYMM')
    elif s[0] == '0' and s[1] == '3':
        print('YYMM')
    elif s[0] == '0' and s[1] == '4':
        print('YYMM')
    elif s[0] == '0' and s[1] == '5':
        print('YYMM')
    elif s[0] == '0' and s[1] == '6':
        print('YYMM')
    elif s[0] == '0' and s[1] == '7':
        print('YYMM')
    elif s[0] == '0' and s[1] == '8':
        print('YYMM')
    elif s[0] == '0' and s[1] == '9':
        print('YYMM')
    elif s[0] == '1' and s[1] == '0':
        print('YYMM')
    elif s[0] == '1' and s[1] == '1':
        print('YYMM')
    elif s[0] == '1' and s[1] == '2':
        print('YYMM')
    elif s[0] == '1' and s[1] == '3' and s[2] == '0' and s[3] == '1':
        print('YYMM')
    elif s[0] == '1' and s[1] == '3' and s[2] == '0' and s[3] == '2':
        print('YYMM')
    elif s[0] == '1' and s[1] == '

=======
Suggestion 2

def main():
    S = input()
    if S[0] == '0' and S[1] == '0' and S[2] == '0' and S[3] == '0':
        print('NA')
    elif S[0] == '0' and S[1] == '0' and S[2] == '0' and S[3] != '0':
        print('YYMM')
    elif S[0] == '0' and S[1] == '0' and S[2] != '0' and S[3] == '0':
        print('YYMM')
    elif S[0] == '0' and S[1] == '0' and S[2] != '0' and S[3] != '0':
        print('YYMM')
    elif S[0] == '0' and S[1] != '0' and S[2] == '0' and S[3] == '0':
        print('YYMM')
    elif S[0] == '0' and S[1] != '0' and S[2] == '0' and S[3] != '0':
        print('MMYY')
    elif S[0] == '0' and S[1] != '0' and S[2] != '0' and S[3] == '0':
        print('YYMM')
    elif S[0] == '0' and S[1] != '0' and S[2] != '0' and S[3] != '0':
        print('MMYY')
    elif S[0] != '0' and S[1] == '0' and S[2] == '0' and S[3] == '0':
        print('YYMM')
    elif S[0] != '0' and S[1] == '0' and S[2] == '0' and S[3] != '0':
        print('YYMM')
    elif S[0] != '0' and S[1] == '0' and S[2] != '0' and S[3] == '0':
        print('YYMM')
    elif S[0] != '0' and S[1] == '0' and S

=======
Suggestion 3

def main():
    s = input()
    if s[0] == '0' and s[1] == '0':
        if s[2] == '0' and s[3] == '0':
            print('NA')
        elif s[2] == '0' or s[3] == '0':
            print('AMBIGUOUS')
        else:
            print('MMYY')
    elif s[2] == '0' and s[3] == '0':
        print('YYMM')
    elif s[0] == '0' or s[1] == '0':
        if s[2] == '0' or s[3] == '0':
            print('AMBIGUOUS')
        else:
            print('MMYY')
    elif s[2] == '0' or s[3] == '0':
        print('YYMM')
    else:
        print('AMBIGUOUS')

=======
Suggestion 4

def main():
    s = input()
    if int(s[0:2]) in range(1,13) and int(s[2:4]) in range(1,13):
        print("AMBIGUOUS")
    elif int(s[0:2]) in range(1,13) and int(s[2:4]) in range(0,13):
        print("MMYY")
    elif int(s[0:2]) in range(0,13) and int(s[2:4]) in range(1,13):
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 5

def main():
    s = input()
    if int(s[0:2]) > 12 and int(s[2:4]) > 12:
        print("NA")
    elif int(s[0:2]) > 12 and int(s[2:4]) <= 12:
        print("YYMM")
    elif int(s[0:2]) <= 12 and int(s[2:4]) > 12:
        print("MMYY")
    else:
        print("AMBIGUOUS")

=======
Suggestion 6

def main():
    s = input()
    s1 = s[2:]
    s2 = s[:2]
    if 1 <= int(s1) <= 12 and 1 <= int(s2) <= 12:
        print('AMBIGUOUS')
    elif 1 <= int(s1) <= 12:
        print('YYMM')
    elif 1 <= int(s2) <= 12:
        print('MMYY')
    else:
        print('NA')

=======
Suggestion 7

def main():
    s = input()
    if s[0] in "01" and s[1] in "0123" and s[2] in "01" and s[3] in "0123":
        print("AMBIGUOUS")
    elif s[0] in "01" and s[1] in "0123" and s[2] in "0123" and s[3] in "0123":
        print("MMYY")
    elif s[0] in "0123" and s[1] in "0123" and s[2] in "01" and s[3] in "0123":
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 8

def main():
    S = input()
    YYMM = False
    MMYY = False
    if S[0] == '0' or S[0] == '1':
        if S[1] == '0' or S[1] == '1' or S[1] == '2':
            YYMM = True
    if S[2] == '0' or S[2] == '1':
        if S[3] == '0' or S[3] == '1' or S[3] == '2' or S[3] == '3':
            MMYY = True
    if YYMM and MMYY:
        print('AMBIGUOUS')
    elif YYMM:
        print('YYMM')
    elif MMYY:
        print('MMYY')
    else:
        print('NA')

=======
Suggestion 9

def main():

    s = input()

    # YYMM
    if 1 <= int(s[0:2]) <= 12 and 1 <= int(s[2:4]) <= 12:
        print('AMBIGUOUS')
    # YYMM
    elif 1 <= int(s[0:2]) <= 12:
        print('YYMM')
    # MMYY
    elif 1 <= int(s[2:4]) <= 12:
        print('MMYY')
    # NA
    else:
        print('NA')

=======
Suggestion 10

def main():
    s = input()
    ym = s[0:2]
    my = s[2:4]
    if ym == "00" or int(ym) > 12:
        ym = "00"
    if my == "00" or int(my) > 12:
        my = "00"
    if ym == "00" and my == "00":
        print("NA")
    elif ym == "00" or my == "00":
        print("MMYY" if my != "00" else "YYMM")
    else:
        print("AMBIGUOUS")
