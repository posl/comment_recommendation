Synthesizing 10/10 solutions

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
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    elif s[0] == s[1] and s[1] == s[2] and s[2] != s[3]:
        print("Bad")
    elif s[0] == s[1] and s[1] != s[2] and s[2] == s[3]:
        print("Bad")
    elif s[0] != s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 3

def main():
    S = input()
    if S[0] == S[1] == S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 4

def main():
    S = input()
    if S[0] == S[1] == S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] and S[2] == S[3]:
        print("Bad")
    elif S[0] == S[2] and S[1] == S[3]:
        print("Bad")
    elif S[0] == S[3] and S[1] == S[2]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 5

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    elif S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] and S[1] == S[2]:
        print("Bad")
    elif S[0] == S[1] and S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 6

def isDifficultToInput(password):
    if password[0] == password[1] and password[1] == password[2] and password[2] == password[3]:
        return True
    elif password[0] != password[1] and password[1] != password[2] and password[2] != password[3]:
        return True
    else:
        return False

=======
Suggestion 7

def main():
    S = input()
    if S[0]==S[1] or S[1]==S[2] or S[2]==S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 8

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] and S[2] == S[3]:
        print("Bad")
    elif S[0] == S[2] and S[1] == S[3]:
        print("Bad")
    elif S[0] == S[3] and S[1] == S[2]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 9

def main():
    S = input()
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 10

def main():
    # 读取输入
    S = input()
    # 判断是否有两个连续的数字是相同的
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    else:
        print("Good")
