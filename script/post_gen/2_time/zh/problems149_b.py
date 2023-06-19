Synthesizing 10/10 solutions

=======
Suggestion 1

def problem149_b():
    a,b,k = map(int,input().split())
    if k <= a:
        print(a-k,b)
    elif k > a and k <= a+b:
        print(0,b-(k-a))
    elif k > a+b:
        print(0,0)

=======
Suggestion 2

def main():
    A,B,K = map(int,input().split())
    if K >= A:
        K -= A
        A = 0
    else:
        A -= K
        K = 0
    if K >= B:
        K -= B
        B = 0
    else:
        B -= K
        K = 0
    print(A,B)

=======
Suggestion 3

def main():
    a,b,k = map(int,input().split())
    if k <= a:
        print(a-k,b)
    elif k > a and k <= a+b:
        print(0,b-(k-a))
    else:
        print(0,0)

=======
Suggestion 4

def main():
    a,b,k = map(int,input().split())
    if k <= a:
        print(a-k,b)
    elif k <= a+b:
        print(0,b-(k-a))
    else:
        print(0,0)

=======
Suggestion 5

def main():
    a, b, k = map(int, input().split())
    if a >= k:
        print(a - k, b)
    elif a + b >= k:
        print(0, b - (k - a))
    else:
        print(0, 0)

=======
Suggestion 6

def main():
    a,b,k=map(int,input().split())
    for i in range(k):
        if i%2==0:
            if a%2==1:
                a-=1
            b+=a//2
            a=a//2
        else:
            if b%2==1:
                b-=1
            a+=b//2
            b=b//2
    print(a,b)

=======
Suggestion 7

def main():
    A,B,K = map(int,input().split())
    if K == 0:
        print(A,B)
    elif A == 0:
        print(0,B-K)
    elif B == 0:
        print(A-K,0)
    elif A+B <= K:
        print(0,0)
    elif A <= K:
        print(0,B-(K-A))
    else:
        print(A-K,B)

=======
Suggestion 8

def solve(A, B, K):
    if K <= A:
        return (A - K, B)
    else:
        return (0, B - (K - A))

A, B, K = map(int, input().split())
print(*solve(A, B, K))

=======
Suggestion 9

def solve():
    a,b,k = map(int,input().split())
    if k <= a:
        print(a-k,b)
    elif k <= a+b:
        print(0,b-(k-a))
    else:
        print(0,0)

=======
Suggestion 10

def main():
    a,b,k = map(int, input().split())
    if a >= k:
        a -= k
    else:
        b -= (k-a)
        a = 0
        if b < 0:
            b = 0
    print(a,b)
