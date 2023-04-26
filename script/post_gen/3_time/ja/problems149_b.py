Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        print(A - K, B)
    elif A + B >= K:
        print(0, A + B - K)
    else:
        print(0, 0)

=======
Suggestion 2

def main():
    A,B,K = map(int, input().split())
    if A >= K:
        A -= K
    else:
        K -= A
        A = 0
        if B >= K:
            B -= K
        else:
            B = 0
    print(A,B)

=======
Suggestion 3

def main():
    a, b, k = map(int, input().split())
    if k <= a:
        a -= k
    else:
        k -= a
        a = 0
        b -= k
        if b < 0:
            b = 0
    print(a, b)

=======
Suggestion 4

def main():
    a, b, k = map(int, input().split())
    if k <= a:
        print(a-k, b)
    elif k <= a+b:
        print(0, b-(k-a))
    else:
        print(0, 0)

=======
Suggestion 5

def solve():
    A, B, K = map(int, input().split())
    if A >= K:
        print(A-K, B)
    elif A+B >= K:
        print(0, A+B-K)
    else:
        print(0, 0)

=======
Suggestion 6

def main():
    a,b,k = map(int,input().split())
    if a > k:
        print(a-k,b)
    else:
        if b > (k-a):
            print(0,b-(k-a))
        else:
            print(0,0)

=======
Suggestion 7

def main():
    a,b,k = map(int,input().split())
    if a >= k:
        print(a-k,b)
    else:
        print(0, max(0,b-(k-a)))
