Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        A -= K
    else:
        K -= A
        A = 0
        if B >= K:
            B -= K
    print(A, B)

=======
Suggestion 2

def main():
    a, b, k = map(int, input().split())
    if a >= k:
        a -= k
    else:
        k -= a
        a = 0
        if b >= k:
            b -= k
    print(a, b)

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    if A > K:
        A -= K
    else:
        K -= A
        A = 0
        if B > K:
            B -= K
        else:
            B = 0
    print(A, B)

main()

=======
Suggestion 4

def main():
    A, B, K = map(int, input().split())
    if A > K:
        A -= K
    else:
        K -= A
        A = 0
        if B > K:
            B -= K
        else:
            B = 0
    print(A, B)

=======
Suggestion 5

def main():
    a, b, k = map(int, input().split())
    if a < k:
        k -= a
        a = 0
        if b < k:
            b = 0
        else:
            b -= k
    else:
        a -= k
    print(a, b)

=======
Suggestion 6

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        A -= K
    elif A + B >= K:
        B -= (K - A)
        A = 0
    else:
        A = 0
        B = 0
    print(A, B)

=======
Suggestion 7

def main():
    a, b, k = map(int, input().split())
    if a >= k:
        print(a-k, b)
    elif a + b >= k:
        print(0, a+b-k)
    else:
        print(0, 0)

=======
Suggestion 8

def main():
    a, b, k = map(int, input().split())

    if a + b <= k:
        print(0, 0)
    elif a <= k:
        print(0, b - (k - a))
    else:
        print(a - k, b)

=======
Suggestion 9

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        print(A-K, B)
    else:
        print(0, B-(K-A) if B >= K-A else 0)
