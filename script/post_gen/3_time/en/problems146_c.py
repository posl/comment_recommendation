Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, X = map(int, input().split())
    if A * 10**9 + B * 10 <= X:
        print(10**9)
        return

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
Suggestion 2

def main():
    #input
    A, B, X = map(int, input().split())

    #compute
    if A * 10**9 + B * 10 <= X:
        ans = 10**9
    else:
        ans = 0
        for i in range(1, 10):
            if A * 10**(i-1) + B * i <= X:
                ans = max(ans, 10**(i-1) + (X - A * 10**(i-1) - B * i) // (A * 10**(i-1) + B * i))

    #output
    print(ans)

=======
Suggestion 3

def main():
    A, B, X = map(int, input().split())
    N = X // A
    if N >= 10**9:
        N = 10**9
    while A * N + B * len(str(N)) > X:
        N -= 1
    print(N)

=======
Suggestion 4

def main():
    A, B, X = map(int, input().split())
    if X < A:
        print(0)
        return
    X -= A
    if X / B > 10 ** 9:
        print(10 ** 9)
        return
    X = int(X / B)
    if X == 0:
        print(1)
        return
    print(X)

=======
Suggestion 5

def main():
    a, b, x = map(int, input().split())
    n = x // a
    if n > 10**9:
        n = 10**9
    for i in range(n, 0, -1):
        if a * i + b * len(str(i)) <= x:
            print(i)
            return
    print(0)

=======
Suggestion 6

def main():
    A, B, X = map(int, input().split())

    # 1桁の場合
    if X < A + B:
        print(0)
        return

    # 10^9桁の場合
    if X >= A * 10**9 + B * 10:
        print(10**9)
        return

    # 1桁から9桁までの場合
    left = 1
    right = 10**9
    while right - left > 1:
        mid = (left + right) // 2
        # A * mid + B * d(mid) <= X
        if A * mid + B * len(str(mid)) <= X:
            left = mid
        else:
            right = mid

    print(left)

=======
Suggestion 7

def main():
    A, B, X = map(int, input().split())
    if A == 1:
        print(X // B)
        return
    if A * (10 ** 9) + B * 10 < X:
        print(10 ** 9)
        return
    for i in range(1, 10):
        if A * (10 ** i) + B * (i + 1) > X:
            print(10 ** (i - 1) - 1)
            return
    print(10 ** 9)

=======
Suggestion 8

def num_digits(n):
    if n == 0:
        return 1
    return int(math.log10(n)) + 1

=======
Suggestion 9

def main():
    A,B,X = list(map(int, input().split()))
    if A > X:
        print(0)
        return
    if A == X:
        print(1)
        return
    if X >= A + B * 10:
        print(10 ** 9)
        return
    for i in range(1, 10):
        if A * (10 ** i) + B * (i + 1) > X:
            print(10 ** (i - 1))
            return

main()

=======
Suggestion 10

def d(N):
    return len(str(N))
