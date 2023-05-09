Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if 1 <= int(S[0:2]) <= 12 and 1 <= int(S[2:4]) <= 12:
        print("AMBIGUOUS")
    elif 1 <= int(S[0:2]) <= 12:
        print("MMYY")
    elif 1 <= int(S[2:4]) <= 12:
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 2

def main():
    S = input()
    if 1 <= int(S[0:2]) <= 12 and 1 <= int(S[2:4]) <= 12:
        print('AMBIGUOUS')
    elif 1 <= int(S[0:2]) <= 12:
        print('MMYY')
    elif 1 <= int(S[2:4]) <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 3

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
Suggestion 4

def main():
    S = input()
    if int(S[0:2]) in range(1,13) and int(S[2:4]) in range(1,13):
        print("AMBIGUOUS")
    elif int(S[0:2]) in range(1,13):
        print("MMYY")
    elif int(S[2:4]) in range(1,13):
        print("YYMM")
    else:
        print("NA")

=======
Suggestion 5

def check(s):
    if int(s[0:2]) >= 1 and int(s[0:2]) <= 12:
        if int(s[2:4]) >= 1 and int(s[2:4]) <= 12:
            return "AMBIGUOUS"
        else:
            return "MMYY"
    else:
        if int(s[2:4]) >= 1 and int(s[2:4]) <= 12:
            return "YYMM"
        else:
            return "NA"

s = input()
print(check(s))

=======
Suggestion 6

def main():
	s = input()
	if int(s[:2]) in range(1,13) and int(s[2:]) in range(1,13):
		print('AMBIGUOUS')
	elif int(s[:2]) in range(1,13):
		print('MMYY')
	elif int(s[2:]) in range(1,13):
		print('YYMM')
	else:
		print('NA')

=======
Suggestion 7

def main():
    s = input()
    first = int(s[:2])
    second = int(s[2:])
    if 0 < first <= 12:
        if 0 < second <= 12:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if 0 < second <= 12:
            print("YYMM")
        else:
            print("NA")

=======
Suggestion 8

def check_year_month_format(s):
    if s[0] == '0':
        return False
    if s[0] == '1':
        if s[1] in ['0','1','2']:
            return True
    if s[0] == '2':
        if s[1] in ['0','1','2','3']:
            return True
    return False

=======
Suggestion 9

def check_yymm(mm):
    if (mm >= 1 and mm <= 12):
        return True
    else:
        return False
