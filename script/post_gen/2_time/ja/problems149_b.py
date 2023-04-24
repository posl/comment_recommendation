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
        else:
            B = 0
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
        else:
            b = 0
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

=======
Suggestion 4

def main():
    A, B, K = map(int, input().split())
    if A > K:
        print(A - K, B)
    elif A + B > K:
        print(0, A + B - K)
    else:
        print(0, 0)

main()

=======
Suggestion 5

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        A -= K
    elif A + B >= K:
        B -= K - A
        A = 0
    else:
        A = 0
        B = 0
    print(A, B)

=======
Suggestion 6

def main():
    a, b, k = map(int, input().split())
    if k <= a:
        print(a-k, b)
    elif k <= a+b:
        print(0, a+b-k)
    else:
        print(0, 0)

=======
Suggestion 7

def main():
    A, B, K = map(int, input().split())
    if A > K:
        A -= K
        print(A, B)
    else:
        K -= A
        A = 0
        if B > K:
            B -= K
            print(A, B)
        else:
            B = 0
            print(A, B)

=======
Suggestion 8

def main():
    A, B, K = map(int, input().split())
    print(max(0, A-K), max(0, B-max(0, K-A)))
