Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, X = map(int, input().split())
    N = 0
    if X >= A * 10**9 + B * 10:
        N = 10**9
    else:
        for i in range(9):
            if X >= A * 10**(8-i) + B * (9-i):
                N = 10**(8-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(7-i)) + B * (9-i):
                N += 10**(7-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(6-i)) + B * (9-i):
                N += 10**(6-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(5-i)) + B * (9-i):
                N += 10**(5-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(4-i)) + B * (9-i):
                N += 10**(4-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(3-i)) + B * (9-i):
                N += 10**(3-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(2-i)) + B * (9-i):
                N += 10**(2-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(1-i)) + B * (9-i):
                N += 10**(1-i)
                break
        for i in range(9):
            if X >= A * (N + 10**(0-i)) + B * (9-i):
                N += 10**(0-i)
                break
    print(N)

=======
Suggestion 2

def main():
    a, b, x = map(int, input().split())
    if a * 10**9 + b * 10 <= x:
        print(10**9)
        return
    if a * 1 + b * 1 > x:
        print(0)
        return
    left = 0
    right = 10**9
    while right - left > 1:
        mid = (left + right) // 2
        if a * mid + b * len(str(mid)) > x:
            right = mid
        else:
            left = mid
    print(left)

=======
Suggestion 3

def main():
    A, B, X = map(int, input().split())
    # 二分探索
    left = 0
    right = 10 ** 9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        # midの桁数を求める
        mid_digit = len(str(mid))
        # midの値段を求める
        mid_price = A * mid + B * mid_digit
        # midの値段がX円以下ならrightをmidにする
        if mid_price <= X:
            left = mid
        # midの値段がX円より大きいならleftをmidにする
        else:
            right = mid
    print(left)

=======
Suggestion 4

def main():
    A, B, X = map(int, input().split())
    N = 10**9
    while N > 0:
        if A*N + B*len(str(N)) <= X:
            print(N)
            return
        else:
            N = N//10

=======
Suggestion 5

def main():
    A, B, X = map(int, input().split())

    # 1 <= N <= 10^9
    # 1 <= A <= 10^9
    # 1 <= B <= 10^9
    # 1 <= X <= 10^18
    # A * N + B * d(N) <= X
    # N <= X / (A + B * d(N))
    # 1 <= d(N) <= 9
    # N <= X / (A + B * 9)

    # N <= 10^9
    # N <= X / (A + B * 9)
    # N <= X / (A + B * 9)
    # N <= 10^18 / (10^9 + 10^9 * 9)
    # N <= 10^18 / (10^9 + 10^10)
    # N <= 10^18 / 10^10
    # N <= 10^8
    # N <= 10^9

    # N = 10^9
    # N = 10^9

    # N = 10^8
    # N = 10^8

    # N = 10^7
    # N = 10^7

    # N = 10^6
    # N = 10^6

    # N = 10^5
    # N = 10^5

    # N = 10^4
    # N = 10^4

    # N = 10^3
    # N = 10^3

    # N = 10^2
    # N = 10^2

    # N = 10^1
    # N = 10^1

    # N = 10^0
    # N = 10^0

    # N = 1
    # N = 1

    # N = 0
    # N = 0

    # N = -1
    # N = -1

    # N = -2
    # N = -2

    # N = -3
    # N = -3

    # N = -4
    # N = -4

    # N = -5

=======
Suggestion 6

def main():
    A, B, X = map(int, input().split())
    # X = A * N + B * d(N)
    # N = (X - B * d(N)) / A
    # d(N) = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ...
    # d(N) = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ...
    # 10 ** d(N) = 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, ...
    # 10 ** d(N) = 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, ...
    # 10 ** (d(N) - 1) = 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, ...
    # 10 ** (d(N) - 1) = 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, ...
    # 10 ** (d(N) - 1) <= X / A < 10 ** d(N)
    # 1

=======
Suggestion 7

def main():
    A, B, X = map(int, input().split())
    # 1 <= N <= 10^9
    # 1 <= X <= 10^18
    # A * N + B * d(N) <= X
    # d(N) = len(str(N))
    # A * N + B * len(str(N)) <= X
    # A * N <= X - B * len(str(N))
    # N <= (X - B * len(str(N))) / A

=======
Suggestion 8

def main():
    A, B, X = map(int, input().split())
    if A * 10**9 + B * 10 > X:
        print(0)
        return

    # 二分探索
    left = 0
    right = 10**9
    while right - left > 1:
        mid = (left + right) // 2
        if A * mid + B * len(str(mid)) <= X:
            left = mid
        else:
            right = mid

    print(left)

=======
Suggestion 9

def main():
    A, B, X = map(int, input().split())
    #print(A, B, X)
    #print("A*X", A*X)
    #print("B*d(N)", B*d(N))
    #print("A*X+B*d(N)", A*X+B*d(N))
    #print("A*X+B*d(N) <= X", A*X+B*d(N) <= X)
    #print("A*X+B*d(N) <= X", A*X+B*d(N) <= X)

    if A*X < X:
        #print("A*X < X")
        print(0)
        return

    #print("A*X >= X")
    #print("X/(A+B)", X/(A+B))
    #print("int(X/(A+B))", int(X/(A+B)))
    N = int(X/(A+B))
    #print("N", N)
    while A*N+B*d(N) <= X:
        N += 1
    N -= 1
    print(N)

=======
Suggestion 10

def main():
    A,B,X = map(int,input().split())
    ans = 0
    # 1 <= N <= 10^9 なので、Nの最大値は10^9
    # 1 <= X <= 10^18 なので、Xの最大値は10^18
    # 10^18 < 10^9 * 10^9 なので、Nの最大値は10^9であることがわかる
    # また、Nの最小値は1であることもわかる
    # つまり、Nの値は10^9までの整数である
    # これを利用して、Nの値を二分探索で求める
    # 二分探索の範囲は、Nの最小値からNの最大値の間である
    # つまり、Nの最小値は1、Nの最大値は10^9である
    # また、Nは整数である
    # つまり、Nの最小値は1、Nの最大値は10^9である
    # また、Nは整数である
    # つまり、Nの最小値は1、Nの最大値は10^9である
    # また、Nは整数である
    # つまり、Nの最小値は1、Nの最大値は10^9である
    # また、Nは整数である
    # つまり、Nの最小値は1、Nの最大値は10^9である
    # また、Nは整数である
    # つまり、Nの最小値は1、Nの最大値は10^9である
    # また、Nは整数である
    # つまり、Nの最小値は1、Nの最大値は
