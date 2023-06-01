Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #input
    A, B, K = map(int, input().split())
    #calc
    if A >= K:
        A = A - K
    elif A < K:
        B = B - (K - A)
        A = 0
        if B < 0:
            B = 0
    #output
    print(A, B)

=======
Suggestion 2

def main():
    a,b,k = map(int,input().split())
    if a >= k:
        a = a - k
    elif a + b >= k:
        b = b - (k - a)
        a = 0
    else:
        a = 0
        b = 0
    print(a,b)

=======
Suggestion 3

def main():
    A,B,K = map(int,input().split())
    if K <= A:
        print(A-K,B)
    elif K > A and K <= A+B:
        print(0,B-(K-A))
    else:
        print(0,0)

=======
Suggestion 4

def main():
    a,b,k = map(int, input().split())
    if k > a:
        b = b - (k - a)
        a = 0
        if b < 0:
            b = 0
    else:
        a = a - k
    print(a,b)

=======
Suggestion 5

def solve():
    a,b,k = map(int,input().split())
    if k <= a:
        print(a-k,b)
    elif k <= a+b:
        print(0,b-(k-a))
    else:
        print(0,0)

=======
Suggestion 6

def main():
    a, b, k = map(int, input().split())
    if k <= a:
        print(a - k, b)
    elif k <= a + b:
        print(0, b - (k - a))
    else:
        print(0, 0)

=======
Suggestion 7

def main():
    A,B,K = map(int,input().split())
    if K <= A:
        A -= K
    else:
        B -= K - A
        A = 0
        if B < 0:
            B = 0
    print(A,B)

=======
Suggestion 8

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        A -= K
    else:
        B -= K - A
        A = 0
        if B < 0:
            B = 0
    print(A, B)

=======
Suggestion 9

def main():
    a,b,k = map(int,input().split())

    if a >= k:
        print(a-k,b)
    elif a+b >= k:
        print(0,b-(k-a))
    else:
        print(0,0)

=======
Suggestion 10

def solve():
    A,B,K = map(int,input().split())
    if A >= K:
        A -= K
    else:
        B -= (K - A)
        A = 0
        if B < 0:
            B = 0
    print(A,B)
