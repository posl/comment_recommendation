Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    s = input()
    if s[0]==s[1] and s[1]==s[2] and s[2]==s[3]:
        print("Bad")
    elif s[0]==s[1] and s[1]==s[2] and s[2]!=s[3]:
        print("Bad")
    elif s[0]==s[1] and s[1]!=s[2] and s[2]==s[3]:
        print("Bad")
    elif s[0]!=s[1] and s[1]==s[2] and s[2]==s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 3

def main():
    S = input()
    #print(S)
    if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
        print('Bad')
    elif S[0] == S[1] and S[1] == S[2]:
        print('Bad')
    elif S[1] == S[2] and S[2] == S[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 4

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 5

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
Suggestion 6

def main():
    S = input()
    if S[0]==S[1] and S[1]==S[2] or S[1]==S[2] and S[2]==S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 7

def problem131_a():
    S = input()
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 8

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
        print('Bad')
    elif S[0] == S[1] and S[1] == S[2]:
        print('Bad')
    elif S[1] == S[2] and S[2] == S[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 9

def main():
    # 读取输入
    S = input()
    # 计算
    # 由于S是4位数，因此只需要比较第1位和第2位，第2位和第3位，第3位和第4位
    # 如果有相同的，就打印Bad，然后退出
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
        return
    # 如果没有相同的，就打印Good
    print("Good")
