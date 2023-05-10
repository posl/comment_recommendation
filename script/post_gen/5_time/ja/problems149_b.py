Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, k = map(int, input().split())
    if k > a:
        k -= a
        a = 0
        if k > b:
            b = 0
        else:
            b -= k
    else:
        a -= k
    print(a, b)

=======
Suggestion 2

def main():
    a,b,k = map(int,input().split())
    if k <= a:
        print(a-k,b)
    else:
        print(0,max(0,b-(k-a)))

=======
Suggestion 3

def main():
    a, b, k = map(int, input().split())

    if k < a:
        print(a - k, b)
    elif k < a + b:
        print(0, b - (k - a))
    else:
        print(0, 0)

=======
Suggestion 4

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
Suggestion 5

def main():
    a, b, k = map(int, input().split())
    if k <= a:
        print(a - k, b)
    elif k <= a + b:
        print(0, b - (k - a))
    else:
        print(0, 0)

=======
Suggestion 6

def main():
    A,B,K = map(int,input().split())
    if A >= K:
        A = A - K
    elif A < K and B >= (K - A):
        B = B - (K - A)
        A = 0
    else:
        A = 0
        B = 0
    print(A,B)

=======
Suggestion 7

def main():
    a,b,k=map(int,input().split())
    if k>=a:
        k=k-a
        a=0
    else:
        a=a-k
        k=0
    if k>=b:
        k=k-b
        b=0
    else:
        b=b-k
        k=0
    print(a,b)
main()

=======
Suggestion 8

def solve():
    A, B, K = map(int, input().split())
    if K <= A:
        print(A-K, B)
    elif K <= A+B:
        print(0, B-(K-A))
    else:
        print(0, 0)
