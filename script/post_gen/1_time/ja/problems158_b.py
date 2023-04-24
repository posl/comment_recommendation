Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    if A + B == 0:
        print(0)
        return
    if A == 0:
        print(0)
        return
    if B == 0:
        print(N)
        return

    if A > B:
        A, B = B, A

    if N // (A + B) == 0:
        print(N // (A + B) * A + min(N % (A + B), A))
    else:
        print(N // (A + B) * A + min(N % (A + B), A))

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    # N, A, B = 8, 3, 4
    # N, A, B = 8, 0, 4
    # N, A, B = 6, 2, 4
    if A == 0:
        print(0)
    elif A == 0 and B == 0:
        print(0)
    elif A + B > N:
        print(N)
    else:
        print(A * (N // (A + B)) + min(A, N % (A + B)))

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B == 0:
        print(N)
    else:
        print(N // (A + B) * A + min(A, N % (A + B)))

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())

    if a == 0:
        print(0)
        return
    elif b == 0:
        print(n)
        return

    q, r = divmod(n, a + b)
    ans = a * q + min(a, r)
    print(ans)

=======
Suggestion 5

def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
        return
    if b == 0:
        print(n)
        return
    print((n // (a+b)) * a + min(a, n % (a+b)))

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B == 0:
        print(0)
    else:
        print(min(N, (N // (A + B)) * A + min(N % (A + B), A)))

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())

    if A == 0 or B == 0:
        print(0)
        return

    if A + B > N:
        print(0)
        return

    if A + B == N:
        print(A)
        return

    if A + B < N:
        if N % (A + B) == 0:
            print(A * (N // (A + B)))
            return
        else:
            print(A * (N // (A + B)) + min(A, N % (A + B)))
            return

=======
Suggestion 8

def main():
    #入力
    N, A, B = map(int, input().split())
    #処理
    if A == 0:
        print(0)
    elif A + B <= N:
        print(A * (N // (A + B)) + min(A, N % (A + B)))
    else:
        print(min(A, N))

=======
Suggestion 9

def main():
    # 入力
    n, a, b = map(int, input().split())
    # 処理
    if a == 0 or b == 0:
        print(0)
    else:
        if a > b:
            print((n//(a+b))*a + min(n%(a+b), a))
        else:
            print((n//(a+b))*b + min(n%(a+b), b))

=======
Suggestion 10

def main():
    N, A, B = map(int, input().split())
    print(min(N, A) - abs(A - B) // 2)
