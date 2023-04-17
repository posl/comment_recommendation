Synthesizing 10/10 solutions

=======

def main():
    S = input()
    T = input()
    s = set(S)
    t = set(T)
    if len(s) >= len(t):
        print("Yes")
    else:
        print("No")

=======

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if sorted(S) != sorted(T):
        print("No")
        return
    print("Yes")

main()

=======

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            count += 1
    if count == len(s):
        print("Yes")
    else:
        print("No")

main()

問題文

英小文字のみからなる文字列 S, T が与えられます。 文字列 S に対して、次の操作を何度でも行うことができます。 操作: 2つの異なる英小文字 c_1, c_2 を選び、S に含まれる全ての c_1 を c_2 に、c_2 を c_1 に置き換える 0 回以上操作を行って、S を T に一致させられるか判定してください。

制約

1 ≦ |S| ≦ 2 × 10^5

|S| = |T|

S, T は英小文字のみからなる

入力

入力は以下の形式で標準入力から与えられる。

S
T

出力

S を T に一致させられる場合は Yes、そうでない場合は No を出力せよ。

入力例 1

azzel
apple

出力例 1

Yes
次のように操作を行えば、azzel を apple にできます。
c_1 として e を、c_2 として l を選ぶと、azzel が azzle になる
c_1 として z を、c_2 として p を選ぶと、azzle が apple になる

入力例 2

chokudai
redcoder

出力例 2

No
どのように操作を行っても chokudai を redcoder にできません。

入力例 3

abcdefghijklmnopqrstuvwxyz
ibyhqfrekavclxjstdwgpzmonu

出力例 3

Yes

=======

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if len(set(s)) < len(set(t)):
        print("No")
        return
    print("Yes")

=======

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if len(set(S)) < len(set(T)):
        print("No")
        return
    print("Yes")

=======

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    if s == t:
        print("Yes")
    else:
        print("No")
main()

=======

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    s = ''.join(s)
    t = ''.join(t)
    if s == t:
        print("Yes")
    else:
        print("No")

=======

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    if len(set(S)) != len(set(T)):
        print("No")
        return
    if len(set(S)) == 26:
        print("Yes")
        return
    for i in range(len(S)):
        if S[i] != T[i]:
            S = S.replace(S[i], T[i])
            if S == T:
                print("Yes")
                return
    print("No")

=======

def main():
    S = input()
    T = input()
    if len(S) < len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        if S[i] in T:
            print("Yes")
            return
    print("No")

=======

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return

    # 文字列を集合に変換
    s = set(S)
    t = set(T)

    # 文字列の集合の長さが同じなら、Yes
    if len(s) == len(t):
        print("Yes")
    else:
        print("No")
