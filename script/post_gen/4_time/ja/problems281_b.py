Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def check(s):
    if s[0].isupper() and s[-1].isupper():
        if len(s) == 6:
            if s[1:6].isdecimal():
                return True
    return False

s = input()

=======
Suggestion 2

def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

S = input()

=======
Suggestion 3

def check(s):
    if s[0].isupper():
        if s[-1].isupper():
            if len(s) == 6:
                if s[1:5].isdecimal():
                    return True
    return False

s = input()

=======
Suggestion 4

def main():
    S = input()
    #print(S)
    if S[0].isupper():
        if S[-1].isupper():
            if S[1:-1].isdecimal():
                if 100000 <= int(S[1:-1]) <= 999999:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 5

def isUpper(s):
    if s.isupper():
        return True
    else:
        return False

=======
Suggestion 6

def is_upper_alphabet(s):
    if s.isupper():
        return True
    else:
        return False

=======
Suggestion 7

def is_upper_alphabet(char):
    return 'A' <= char <= 'Z'

=======
Suggestion 8

def is_upper(s):
    return s == s.upper()

=======
Suggestion 9

def is_uppercase(char):
    return char.isupper()
