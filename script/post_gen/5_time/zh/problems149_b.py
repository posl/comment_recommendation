Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(a, b, k):
    if a >= k:
        a -= k
    else:
        b -= (k - a)
        a = 0
        if b < 0:
            b = 0
    return a, b

=======
Suggestion 2

def main():
    A, B, K = map(int, input().split())
    if K <= A:
        print(A - K, B)
    elif K <= A + B:
        print(0, B - (K - A))
    else:
        print(0, 0)


main()

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        A -= K
    else:
        B -= (K - A)
        A = 0
        if B < 0:
            B = 0
    print(A, B)

=======
Suggestion 4

def main():
    A, B, K = map(int, input().split())
    if A >= K:
        A = A - K
    else:
        B = B - (K - A)
        A = 0
        if B < 0:
            B = 0
    print(A, B)

=======
Suggestion 5

def solve(A, B, K):
    if K <= A:
        return (A-K, B)
    else:
        return (0, max(0, B-(K-A)))

=======
Suggestion 6

def main():
    a, b, k = map(int, input().split())
    if k > a:
        b -= k - a
        a = 0
    else:
        a -= k
    if b < 0:
        b = 0
    print(a, b)

=======
Suggestion 7

def main():
    A,B,K = map(int,input().split())

    if K == 0:
        print(A,B)
    else:
        if A >= K:
            print(A-K,B)
        else:
            if A+B >= K:
                print(0,B-(K-A))
            else:
                print(0,0)

=======
Suggestion 8

def main():
    A,B,K = map(int,input().split())
    if K <= A:
        A -= K
    else:
        K -= A
        A = 0
        if K <= B:
            B -= K
        else:
            B = 0
    print(A,B)

=======
Suggestion 9

def solve():
    A,B,K=map(int,input().split())
    if A>=K:
        print(A-K,B)
    elif A+B>=K:
        print(0,B-(K-A))
    else:
        print(0,0)
solve()

=======
Suggestion 10

def main():
    a,b,k = map(int, input().split())
    if k <= a:
        print(a-k, b)
    elif k <= a+b:
        print(0, b-(k-a))
    else:
        print(0, 0)
