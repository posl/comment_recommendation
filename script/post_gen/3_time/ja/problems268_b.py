Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T[:len(S)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if S == T[0:len(S)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if S == T[:len(S)]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if T.startswith(S):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t[:len(s)]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                print('No')
                break
        else:
            print('Yes')

=======
Suggestion 8

def main():
    # 入力
    s = input()
    t = input()
    # 処理
    if t.startswith(s):
        ans = "Yes"
    else:
        ans = "No"
    # 出力
    print(ans)
