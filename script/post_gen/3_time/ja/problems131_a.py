Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] == s[2] or s[1] == s[2] == s[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 2

def main():
    S = input()
    if S[0] == S[1] == S[2] or S[1] == S[2] == S[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 4

def main():
    S = input()
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print('Bad')
    elif s[1] == s[2] and s[2] == s[3]:
        print('Bad')
    elif s[0] == s[1] and s[1] == s[2]:
        print('Bad')
    elif s[0] == s[1] and s[2] == s[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 6

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print('Bad')
    elif s[1] == s[2] == s[3]:
        print('Bad')
    elif s[0] == s[1] == s[2]:
        print('Bad')
    elif s[0] == s[1] == s[3]:
        print('Bad')
    elif s[0] == s[2] == s[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 7

def check_security_code(security_code):
    if security_code[0] == security_code[1] == security_code[2] or security_code[1] == security_code[2] == security_code[3]:
        return "Bad"
    else:
        return "Good"

=======
Suggestion 8

def check(S):
    if S[0] == S[1] == S[2] or S[1] == S[2] == S[3]:
        return "Bad"
    else:
        return "Good"

S = input()
print(check(S))

=======
Suggestion 9

def is_bad(s):
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        return True
    else:
        return False

=======
Suggestion 10

def check(s):
    for i in range(3):
        if s[i] == s[i+1]:
            return "Bad"
    return "Good"

s = input()
print(check(s))
