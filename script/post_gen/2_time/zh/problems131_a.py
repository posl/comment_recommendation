Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print("Bad")
    elif s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 2

def solve():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    elif s[0] == s[1] and s[2] == s[3]:
        print("Bad")
    elif s[0] == s[2] and s[1] == s[3]:
        print("Bad")
    elif s[0] == s[3] and s[1] == s[2]:
        print("Bad")
    else:
        print("Good")
solve()

=======
Suggestion 3

def main():
    S = input()
    #print(S[0],S[1],S[2],S[3])
    if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] and S[1] == S[2] and S[2] != S[3]:
        print("Bad")
    elif S[0] == S[1] and S[1] != S[2] and S[2] == S[3]:
        print("Bad")
    elif S[0] != S[1] and S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 4

def solve():
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
    # 读取输入
    S = input()
    # print(S)
    # print(S[0])
    # print(S[1])
    # print(S[2])
    # print(S[3])
    # print(S[0] == S[1])
    # print(S[1] == S[2])
    # print(S[2] == S[3])
    # print(S[0] == S[1] or S[1] == S[2] or S[2] == S[3])
    # print(S[0] == S[1] and S[1] == S[2] and S[2] == S[3])
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 6

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    elif S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] and S[1] == S[2]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 7

def main():
    s = input()
    if s[0] == s[1] == s[2] or s[1] == s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 8

def main():
    s = input()
    if s[0]==s[1] and s[1]==s[2] and s[2]==s[3]:
        print("Bad")
    elif s[0]==s[1] and s[1]==s[2]:
        print("Bad")
    elif s[1]==s[2] and s[2]==s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 9

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
Suggestion 10

def main():
    s = input()
    if s[0]==s[1] and s[1]==s[2] and s[2]==s[3]:
        print('Bad')
    elif s[0]==s[1] and s[1]==s[2]:
        print('Bad')
    elif s[1]==s[2] and s[2]==s[3]:
        print('Bad')
    else:
        print('Good')

main()
