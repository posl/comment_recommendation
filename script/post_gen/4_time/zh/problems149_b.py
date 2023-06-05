Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    if K <= A:
        print(A-K, B)
    elif K <= A+B:
        print(0, B-(K-A))
    else:
        print(0, 0)

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
    a, b, k = map(int, input().split())
    if a >= k:
        print(a-k, b)
    elif a+b >= k:
        print(0, b-(k-a))
    else:
        print(0, 0)

=======
Suggestion 4

def solve():
    A, B, K = map(int, input().split())
    if K <= A:
        print(A-K, B)
    elif K <= A+B:
        print(0, B-(K-A))
    else:
        print(0, 0)

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
    a,b,k = map(int,input().split())
    if k <= a:
        print(a-k,b)
    elif k <= a+b:
        print(0,b-(k-a))
    else:
        print(0,0)

=======
Suggestion 7

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
