Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c, k = map(int, input().split())
    if k <= a:
        print(k)
    elif k <= a + b:
        print(a)
    else:
        print(a - (k - a - b))

=======
Suggestion 2

def main():
    A, B, C, K = map(int, input().split())
    if K <= A:
        print(K)
    elif K <= A + B:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 3

def main():
    a, b, c, k = map(int, input().split())
    if a >= k:
        print(k)
    elif a + b >= k:
        print(a)
    else:
        print(a - (k - a - b))

=======
Suggestion 4

def main():
    a,b,c,k = map(int, input().split())
    if a >= k:
        print(k)
    elif a+b >= k:
        print(a)
    else:
        print(a-(k-(a+b)))

=======
Suggestion 5

def main():
    a,b,c,k = map(int,input().split())
    if k <= a:
        print(k)
        return
    elif k <= a+b:
        print(a)
        return
    else:
        print(a-(k-a-b))
        return

=======
Suggestion 6

def main():
    # A B C K = map(int, input().split())
    # print(A+B+C-K)
    A, B, C, K = map(int, input().split())
    if A >= K:
        print(K)
    elif A+B >= K:
        print(A)
    else:
        print(A-(K-A-B))
