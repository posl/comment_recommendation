Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y, N = map(int, input().split())
    ans = 0
    while N > 0:
        if N >= 3:
            ans += Y
            N -= 3
        else:
            ans += X
            N -= 1
    print(ans)

=======
Suggestion 2

def main():
    X, Y, N = map(int, input().split())
    ans = 0
    while N > 0:
        if N >= 3:
            N -= 3
            ans += Y
        else:
            N -= 1
            ans += X
    print(ans)

=======
Suggestion 3

def main():
    x, y, n = map(int, input().split())
    ans = 0
    ans = (n//3) * y + (n%3) * x
    print(ans)

=======
Suggestion 4

def main():
    #入力
    X, Y, N = map(int, input().split())
    # 処理
    ans = 0
    while N > 0:
        if N % 3 == 0:
            ans += Y * (N // 3)
            N -= N // 3 * 3
        else:
            ans += X
            N -= 1
    #出力
    print(ans)

=======
Suggestion 5

def main():
    x,y,n = map(int,input().split())
    #print(x,y,n)
    ans = 0
    while n > 0:
        if n%3 == 0:
            ans += y
            n -= 3
        else:
            ans += x
            n -= 1
    print(ans)

=======
Suggestion 6

def main():
    x, y, n = map(int, input().split())
    print((n//3)*min(x*3,y) + (n%3)*x)

=======
Suggestion 7

def main():
    # 入力
    X, Y, N = map(int, input().split())
    # 処理
    # 1個のりんごを買うのに必要な金額
    A = X
    # 3個のりんごを買うのに必要な金額
    B = Y
    # 1個のりんごを買うのに必要な金額を3個のりんごを買うのに必要な金額で割った商
    C = (B - A) // 2
    # 1個のりんごを買うのに必要な金額を3個のりんごを買うのに必要な金額で割った余り
    D = (B - A) % 2
    # 1個のりんごを買うのに必要な金額を3個のりんごを買うのに必要な金額で割った商をNで割った商
    E = N // C
    # 1個のりんごを買うのに必要な金額を3個のりんごを買うのに必要な金額で割った商をNで割った余り
    F = N % C
    # 1個のりんごを買うのに必要な金額を3個のりんごを買うのに必要な金額で割った商をNで割った商に3個のりんごを買うのに必要な金額を掛けた金額
    G = E * B
    # 1個のりんごを買うのに必要な金額を3個のりんごを買うのに必要な金額で割った商をNで割った余りに1個のりんごを買うのに必

=======
Suggestion 8

def main():
    x,y,n = map(int,input().split())
    a = x
    b = y
    c = 0
    for i in range(n):
        a += x
        b += y
        if a <= b:
            c = a
        else:
            c = b
    print(c)

=======
Suggestion 9

def main():
    x,y,n = map(int,input().split())
    print(n*x if n%2==1 else n*y if n%3==0 else n//3*y+(n%3)*x)

=======
Suggestion 10

def main():
    x, y, n = map(int, input().split())
    # ループの回数
    loop = n // 3
    # 余り
    mod = n % 3
    # 答え
    ans = 0
    # 3個買う場合
    if mod == 0:
        ans = loop * y
    # 1個買う場合
    elif mod == 1:
        ans = loop * y + x
    # 2個買う場合
    else:
        ans = loop * y + x * 2
    print(ans)
