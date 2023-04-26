Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    ans = 0
    for s in S:
        if s == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    ans = 0
    for i in range(4):
        if s[i] == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    ans = 0
    for i in S:
        if i == "+":
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    ans = 0
    for i in S:
        if i == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    cnt = 0
    for i in s:
        if i == "+":
            cnt += 1
        else:
            cnt -= 1
    print(cnt)

=======
Suggestion 6

def main():
    # 入力
    S = input()
    # 初期値
    ans = 0
    # 計算
    for i in range(len(S)):
        if S[i] == '+':
            ans += 1
        else:
            ans -= 1
    # 出力
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    print(S.count("+") - S.count("-"))

=======
Suggestion 8

def main():
    # 文字列の入力
    S = input()

    # 出力
    print(S.count("+") - S.count("-"))

=======
Suggestion 9

def main():
    #input
    S = input()

    #output
    print(S.count("+") - S.count("-"))
