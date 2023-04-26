Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print(1)
    elif S[0] == S[1] or S[1] == S[2] or S[2] == S[0]:
        print(3)
    else:
        print(6)

=======
Suggestion 2

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print(1)
    elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
        print(3)
    else:
        print(6)

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print(1)
    elif s[0] != s[1] and s[1] != s[2] and s[0] != s[2]:
        print(6)
    else:
        print(3)

=======
Suggestion 4

def main():
    S = input()
    S = list(S)
    S.sort()
    ans = 1
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    #print(s)
    #print(len(s))
    if len(s) == 3:
        if s[0] == s[1] and s[1] == s[2]:
            print(1)
        elif s[0] == s[1] or s[1] == s[2] or s[2] == s[0]:
            print(3)
        else:
            print(6)
    else:
        print('error')

=======
Suggestion 6

def main():
    S = input()
    print(len(set(S)))

=======
Suggestion 7

def main():
    # 入力
    S = input()
    # 処理
    # 文字列をソート
    S = sorted(S)
    # 文字列を結合
    S = ''.join(S)
    # 出力
    print(S)

=======
Suggestion 8

def main():
    s = input()
    print(len(set(s)))
