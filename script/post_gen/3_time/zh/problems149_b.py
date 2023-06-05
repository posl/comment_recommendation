Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,k = map(int,input().split())
    if k <= a:
        print(a-k,b)
    elif k <= a+b:
        print(0,b-(k-a))
    else:
        print(0,0)

=======
Suggestion 2

def main():
    a,b,k = map(int,input().split())
    if a >= k:
        a = a - k
    else:
        b = b - (k - a)
        a = 0
        if b < 0:
            b = 0
    print(a,b)

=======
Suggestion 3

def main():
    a,b,k = map(int,input().split())
    if k < a:
        print(a-k,b)
    elif k <= a+b:
        print(0,b-(k-a))
    else:
        print(0,0)

=======
Suggestion 4

def main():
    a,b,k = map(int, input().split())
    if k <= a:
        print(a-k,b)
    elif k <= a+b:
        print(0,b-(k-a))
    else:
        print(0,0)
main()

=======
Suggestion 5

def main():
    A,B,K = map(int,input().split())
    if A >= K:
        print(A-K,B)
    else:
        print(0,max(0,B-(K-A)))

=======
Suggestion 6

def solve():
    a, b, k = map(int, input().split())
    if k <= a:
        print(a - k, b)
    elif k <= a + b:
        print(0, b - (k - a))
    else:
        print(0, 0)

=======
Suggestion 7

def solve(A, B, K):
    if K <= A:
        return A - K, B
    elif K <= A + B:
        return 0, B - (K - A)
    else:
        return 0, 0

=======
Suggestion 8

def get_ints():
    return [int(x) for x in input().split()]
