Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    S = input()
    # 请在此添加您的代码
    if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    else:
        print("Good")
    return

=======
Suggestion 2

def solve(s):
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    elif s[0] == s[1] and s[1] == s[2]:
        print("Bad")
    elif s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 3

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
Suggestion 4

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print('Bad')
    elif s[0] == s[1] and s[1] == s[2]:
        print('Bad')
    elif s[1] == s[2] and s[2] == s[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 5

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] and S[1] == S[2]:
        print("Bad")
    elif S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 6

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print("Bad")
    elif s[0] == s[1] and s[2] == s[3]:
        print("Bad")
    elif s[0] == s[2] and s[1] == s[3]:
        print("Bad")
    elif s[0] == s[3] and s[1] == s[2]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 7

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    elif s[0] == s[1] and s[1] == s[2]:
        print("Bad")
    elif s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 8

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] or s[1] == s[2] and s[2] == s[3]:
        print('Bad')
    else:
        print('Good')
