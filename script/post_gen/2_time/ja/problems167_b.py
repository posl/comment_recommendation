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
    A, B, C, K = map(int, input().split())
    if K <= A:
        print(K)
    elif K <= A + B:
        print(A)
    else:
        print(A - (K - A - B))

main()

=======
Suggestion 4

def main():
    A, B, C, K = map(int, input().split())
    if A >= K:
        print(K)
    elif A + B >= K:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 5

def solve():
    a, b, c, k = map(int, input().split())
    if a >= k:
        print(k)
    elif a + b >= k:
        print(a)
    else:
        print(a - (k - a - b))
    return 0

=======
Suggestion 6

def main():
    A, B, C, K = map(int, input().split())
    ans = 0
    if A >= K:
        ans = K
    elif A + B >= K:
        ans = A
    else:
        ans = A - (K - A - B)
    print(ans)
    return

=======
Suggestion 7

def main():
    a,b,c,k = map(int,input().split())
    if a >= k:
        print(k)
    elif a + b >= k:
        print(a)
    else:
        print(a - (k - a - b))
