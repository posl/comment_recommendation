Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 2

def main():
    s = input()
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 3

def main():
    code = input()
    if code[0] == code[1] or code[1] == code[2] or code[2] == code[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 4

def main():
    S = input()
    for i in range(3):
        if S[i] == S[i+1]:
            print("Bad")
            return
    print("Good")

=======
Suggestion 5

def main():
    s = input()
    for i in range(3):
        if s[i] == s[i+1]:
            print('Bad')
            exit()
    print('Good')

=======
Suggestion 6

def isHardToEnter(S):
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            return True
    return False

=======
Suggestion 7

def main():
    #read input
    s = input()
    #check if any two consecutive digits are the same
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print("Bad")
    else:
        print("Good")
