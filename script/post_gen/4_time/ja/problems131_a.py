Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] == s[2] or s[1] == s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 2

def main():
    S = input()
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] == s[2] or s[1] == s[2] == s[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 4

def main():
    S = input()
    if S[0] == S[1] == S[2] or S[1] == S[2] == S[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 5

def main():
    s = input()
    if (s[0] == s[1] and s[1] == s[2]) or (s[1] == s[2] and s[2] == s[3]):
        print("Bad")
    else:
        print("Good")

=======
Suggestion 6

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 7

def main():
    s = input()

    if (s[0] == s[1] == s[2]) or (s[1] == s[2] == s[3]):
        print('Bad')
    else:
        print('Good')

=======
Suggestion 8

def check_security_code(code):
    if code[0] == code[1] == code[2] or code[1] == code[2] == code[3]:
        return "Bad"
    else:
        return "Good"
