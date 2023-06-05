Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if len(s) == 4:
        if len(set(s)) == 2:
            for i in set(s):
                if s.count(i) != 2:
                    print('No')
                    break
            else:
                print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if s.count(s[0]) == 2 and s.count(s[1]) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    if len(s) == 4 and s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def solve():
    S = input()
    if len(set(S)) == 2:
        if S.count(S[0]) == 2 and S.count(S[1]) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

solve()

=======
Suggestion 5

def main():
    S = input()
    print(S)
    if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
        print("Yes")
    elif S[0] == S[2] and S[1] == S[3] and S[0] != S[1]:
        print("Yes")
    elif S[0] == S[3] and S[1] == S[2] and S[0] != S[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    # 读取输入
    s = input()
    # 用set去重
    s = set(s)
    # 判断长度是否为2
    if len(s) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    S = input()
    S = sorted(S)
    if S[0] == S[1] and S[2] == S[3] and S[1] != S[2]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s = input()
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        print("Yes")
    elif s[0] == s[2] and s[1] == s[3] and s[0] != s[1]:
        print("Yes")
    elif s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    S = input()
    if len(S) != 4:
        print("No")
        return
    if len(set(S)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def solve():
    s = input()
    if len(set(s)) == 2:
        if s.count(s[0]) == 2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
solve()
