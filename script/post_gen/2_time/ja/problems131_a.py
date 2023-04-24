Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
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
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print('Bad')
    else:
        print('Good')

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
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            print("Bad")
            return
    print("Good")
