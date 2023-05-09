Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, k = map(int, input().split())
    if k <= a:
        print(a - k, b)
    elif k <= a + b:
        print(0, b - (k - a))
    else:
        print(0, 0)

=======
Suggestion 2

def main():
    a, b, k = map(int, input().split())
    if a >= k:
        print(a - k, b)
    elif a + b >= k:
        print(0, b - (k - a))
    else:
        print(0, 0)

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    if K <= A:
        print(A - K, B)
    elif K <= A + B:
        print(0, B - (K - A))
    else:
        print(0, 0)

=======
Suggestion 4

def main():
    a, b, k = map(int, input().split())
    if k < a:
        print(a - k, b)
    elif k < a + b:
        print(0, b - (k - a))
    else:
        print(0, 0)

=======
Suggestion 5

def main():
    # input
    A, B, K = map(int, input().split())

    # compute

    # output
    if A >= K:
        print(A-K, B)
    elif A+B >= K:
        print(0, B-(K-A))
    else:
        print(0, 0)

=======
Suggestion 6

def main():
    a,b,k = map(int, input().split())
    if k > a:
        k -= a
        a = 0
        if k > b:
            b = 0
        else:
            b -= k
    else:
        a -= k
    print(a,b)

=======
Suggestion 7

def main():
    a, b, k = map(int, input().split())
    if k <= a:
        a -= k
    else:
        a = 0
        k -= a
        if k <= b:
            b -= k
        else:
            b = 0
    print(a, b)

=======
Suggestion 8

def solve():
    a,b,k = map(int, input().split())
    if a >= k:
        print(a-k, b)
    elif a+b >= k:
        print(0, b-(k-a))
    else:
        print(0, 0)

=======
Suggestion 9

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        print(A - K, B)
    elif A < K and A + B >= K:
        print(0, B - (K - A))
    else:
        print(0, 0)
