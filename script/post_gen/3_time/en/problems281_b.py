Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S[0].isupper() and S[1:7].isdigit() and S[7].isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if len(s) != 10:
        print('No')
        return
    if s[0].isupper() and s[1:7].isdigit() and int(s[1:7]) >= 100000 and int(s[1:7]) <= 999999 and s[7].isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    if len(s) != 10:
        print("No")
        return
    if s[0].isupper() and s[9].isupper():
        if s[1:7].isdecimal():
            if 100000 <= int(s[1:7]) <= 999999:
                print("Yes")
                return
    print("No")

=======
Suggestion 4

def check(s):
    if s[0].isupper() and s[7].isupper() and s[1:7].isdigit() and len(s[1:7])==6 and 100000<=int(s[1:7])<=999999:
        return "Yes"
    else:
        return "No"

s = input()
print(check(s))

=======
Suggestion 5

def check(s):
    if s[0].isupper() and s[-1].isupper() and s[1:-1].isdecimal() and 100000 <= int(s[1:-1]) <= 999999:
        return "Yes"
    else:
        return "No"

s = input()
print(check(s))

=======
Suggestion 6

def main():
    S = input()
    if S[0] == S[-1] and S[0].isupper() and S[-1].isupper() and S[1:7].isdigit() and 100000 <= int(S[1:7]) <= 999999:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    #input
    S = input()
    #output
    if S[0].isupper() and S[1:7].isdigit() and int(S[1:7]) >= 100000 and int(S[1:7]) <= 999999 and S[7].isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def check_string(S):
    if len(S) != 10:
        return False
    if S[0].isupper() and S[9].isupper():
        if S[1:7].isdigit() and 100000 <= int(S[1:7]) <= 999999:
            return True
    return False

=======
Suggestion 9

def main():
    #input
    S = input()

    #compute
    if S[0].isupper() and S[-1].isupper() and len(S)==8 and S[1:7].isdigit() and 100000<=int(S[1:7])<=999999:
        print('Yes')
    else:
        print('No')

    #output

=======
Suggestion 10

def isUpperAlpha(c):
  return c.isupper()
