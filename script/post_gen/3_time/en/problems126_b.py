Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if 1 <= int(s[0:2]) <= 12:
        if 1 <= int(s[2:4]) <= 12:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if 1 <= int(s[2:4]) <= 12:
            print("YYMM")
        else:
            print("NA")

=======
Suggestion 2

def main():
    s = input()
    s1 = s[0:2]
    s2 = s[2:4]
    if 1 <= int(s1) <= 12 and 1 <= int(s2) <= 12:
        print('AMBIGUOUS')
    elif 1 <= int(s1) <= 12:
        print('MMYY')
    elif 1 <= int(s2) <= 12:
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 3

def main():
    S = input()
    if int(S[:2]) in range(1,13) and int(S[2:]) in range(1,13):
        print('AMBIGUOUS')
    elif int(S[:2]) in range(1,13):
        print('MMYY')
    elif int(S[2:]) in range(1,13):
        print('YYMM')
    else:
        print('NA')

=======
Suggestion 4

def main():
    s = input()
    if (int(s[0:2]) >= 1) and (int(s[0:2]) <= 12):
        if (int(s[2:4]) >= 1) and (int(s[2:4]) <= 12):
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if (int(s[2:4]) >= 1) and (int(s[2:4]) <= 12):
            print("YYMM")
        else:
            print("NA")

=======
Suggestion 5

def main():
    s = input()
    yy = int(s[0:2])
    mm = int(s[2:4])
    if 1 <= mm <= 12:
        if 1 <= yy <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if 1 <= yy <= 12:
            print('YYMM')
        else:
            print('NA')

=======
Suggestion 6

def main():
  S = input()
  s1 = S[0:2]
  s2 = S[2:4]
  if 1 <= int(s1) <= 12:
    if 1 <= int(s2) <= 12:
      print("AMBIGUOUS")
    else:
      print("MMYY")
  elif 1 <= int(s2) <= 12:
    print("YYMM")
  else:
    print("NA")

=======
Suggestion 7

def check(s):
    if s[0] == '0':
        if s[1] in ['0','1','2','3','4','5','6','7','8','9']:
            return True
        else:
            return False
    elif s[0] == '1':
        if s[1] in ['0','1','2']:
            return True
        else:
            return False
    else:
        return False

s = input()

=======
Suggestion 8

def is_valid_month(month):
    return 1 <= month <= 12

=======
Suggestion 9

def valid_month(m):
    return 1 <= m <= 12

=======
Suggestion 10

def is_valid_month(num):
    return 0 < num <= 12
