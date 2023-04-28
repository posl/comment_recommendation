Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c, k = map(int, input().split())
    if a >= k:
        print(k)
    elif a + b >= k:
        print(a)
    else:
        print(a - (k - a - b))

=======
Suggestion 2

def main():
    A, B, C, K = map(int, input().split())
    if A >= K:
        print(K)
    elif A + B >= K:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 3

def solve(A, B, C, K):
    if K <= A:
        return K
    elif K <= A + B:
        return A
    else:
        return A - (K - A - B)

=======
Suggestion 4

def main():
    a, b, c, k = map(int, input().split())
    if k <= a:
        print(k)
        return
    if k <= a + b:
        print(a)
        return
    print(a - (k - a - b))

=======
Suggestion 5

def main():
    a,b,c,k = map(int, input().split())
    if k <= a:
        print(k)
    elif k <= a+b:
        print(a)
    else:
        print(a-(k-a-b))

=======
Suggestion 6

def solve(a, b, c, k):
    if k <= a:
        return k
    if k <= a + b:
        return a
    return a - (k - a - b)

=======
Suggestion 7

def solve():
    A,B,C,K = map(int,input().split())
    if K<=A:
        print(K)
    elif K<=A+B:
        print(A)
    else:
        print(A-(K-A-B))
solve()

=======
Suggestion 8

def main():
    A,B,C,K = map(int,input().split())
    print(min(A,K)-min(max(0,K-A-B),C))
