Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, x = map(int, input().split())
    if a > x:
        print(0)
        return
    if a * 10**9 + b * 10 <= x:
        print(10**9)
        return
    l = 0
    r = 10**9
    while r - l > 1:
        m = (l + r) // 2
        if a * m + b * len(str(m)) > x:
            r = m
        else:
            l = m
    print(l)

=======
Suggestion 2

def main():
    A, B, X = map(int, input().split())
    ans = 0
    for i in range(1, 10**9):
        if A*i + B*len(str(i)) <= X:
            ans = i
    print(ans)

=======
Suggestion 3

def d(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

=======
Suggestion 4

def main():
    A, B, X = map(int, input().split())

    # 10^9 以下の整数 N を買うためには A × N + B × d(N) 円が必要
    # d(N) は N の十進表記での桁数
    # X 円のとき、買うことのできる最も大きい整数を求める

    # 1 以上 10^9 以下の整数 N を買うためには A × N + B × d(N) 円が必要
    # d(N) は N の十進表記での桁数
    # X 円のとき、買うことのできる最も大きい整数を求める

    # 1 以上 10^9 以下の整数 N を買うためには A × N + B × d(N) 円が必要
    # d(N) は N の十進表記での桁数
    # X 円のとき、買うことのできる最も大きい整数を求める

    # 1 以上 10^9 以下の整数 N を買うためには A × N + B × d(N) 円が必要
    # d(N) は N の十進表記での桁数
    # X 円のとき、買うことのできる最も大きい整数を求める

    # 1 以上 10^9 以下の整数 N を買うためには A × N + B × d(N) 円が必要
    # d(N) は N の十進表記での桁数
    # X 円のとき、買うことのできる最も大きい整数を求める

    # 1 以上 10^9 以下の整数 N を買うためには A × N + B × d(N) 円が必要
    # d(N

=======
Suggestion 5

def d(n):
    if n == 0:
        return 1
    else:
        return len(str(n))

a, b, x = map(int, input().split())
ans = 0
for i in range(1, 10**9+1):
    if a*i + b*d(i) > x:
        break
    else:
        ans = i
print(ans)

=======
Suggestion 6

def main():
    A, B, X = map(int, input().split())
    # X = A * N + B * d(N)
    # N = (X - B * d(N)) / A
    # X = A * (X - B * d(N)) / A + B * d(N)
    # X = (X - B * d(N)) + B * d(N)
    # X = (X - B * d(N)) + B * d(N)
    # X - B * d(N) = 0
    # X - B * d(N) = 0
    # X = B * d(N)
    # (X / B) = d(N)
    # (X / B) = d(N)

=======
Suggestion 7

def main():
    A, B, X = map(int, input().split())
    max = 0
    for i in range(1, 10):
        if (A * (10 ** (i - 1)) + B * i) <= X:
            max = 10 ** (i - 1)

    if A * max + B * len(str(max)) <= X:
        print(max * 10 + (X - (A * max + B * len(str(max)))) // A)
    else:
        print(max)

=======
Suggestion 8

def main():
    #入力
    A,B,X = map(int,input().split())

    #処理
    #整数屋さんで買うことのできる最大の整数を求める
    #買うことのできる最大の整数は、X円で買うことのできる最大の整数を求める。
    #X円で買うことのできる最大の整数は、X円で買うことのできる最大の整数の桁数を求める。
    #X円で買うことのできる最大の整数の桁数は、X円で買うことのできる最大の整数の桁数を求める。
    #X円で買うことのできる最大の整数の桁数は、X円で買うことのできる最大の整数を求める。
    #X円で買うことのできる最大の整数は、X円で買うことのできる最大の整数を求める。
    #X円で買うことのできる最大の整数は、X円で買うことのできる最大の整数を求める。
    #X円で買うことのできる最大の整数は、X円で買うことのできる最大の整数を求める。
    #X円で買うことのできる最大の整数は、X円で買うことのできる最大の整数を求める。
    #X円で買うことのできる最大の整数は、X円で買うことのできる最大の整数を求める。
    #X円で買うことのできる最大の整数は、X円で買うことのできる最大の整数を求める。
    #X円で

=======
Suggestion 9

def main():
    A,B,X = map(int,input().split())
    #print(A,B,X)
    N = 0
    for i in range(1,10):
        if X >= A * (10**i) + B * (i+1):
            N = 10**i
        else:
            break
    #print(N)
    if N == 0:
        print(0)
        return
    for j in range(1,N+1):
        if X >= A * (N-j) + B * (len(str(N-j))+1):
            print(N-j)
            return

=======
Suggestion 10

def main():
    A, B, X = map(int, input().split())

    # 一番高い値段を買えるか？
    if A + B > X:
        print(0)
        return

    # 一番高い値段を買う
    N = X // (A + B)
    # 一番高い値段を買った後の金額
    X -= N * (A + B)

    # 一番高い値段を買った後の金額を使って、一番高い値段を買えるか？
    if A > X:
        print(N)
        return

    # 一番高い値段を買った後の金額を使って、一番高い値段を買う
    N = X // A
    # 一番高い値段を買った後の金額を使って、一番高い値段を買った後の金額
    X -= N * A

    # 一番高い値段を買った後の金額を使って、一番高い値段を買った後の金額を使って、一番高い値段を買えるか？
    if A + B > X:
        print(N)
        return

    # 一番高い値段を買った後の金額を使って、一番高い値段を買った後の金額を使って、一番高い値段を買う
    N = X // (A + B)
    # 一番高い値段を買った後の金額を使って、一番高い値段を買った後の金額を使って、一番高い値段を買った後の金額
    X -= N * (A + B)

    # 一番高い値段を買った後の金額を使って、一番高い値段を買った後の
