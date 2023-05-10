Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    A, B, C, K = map(int, input().split())
    if K <= A:
        print(K)
    elif K <= A + B:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 2

def main():
    A, B, C, K = map(int, input().split())
    ans = 0
    if A >= K:
        ans = K
    else:
        ans = A
        K -= A
        if B >= K:
            pass
        else:
            K -= B
            ans -= K
    print(ans)

=======
Suggestion 3

def main():
    a, b, c, k = map(int, input().split())
    if k <= a:
        print(k)
    elif k <= a + b:
        print(a)
    else:
        print(a - (k - a - b))

=======
Suggestion 4

def main():
    A, B, C, K = map(int, input().split())
    if (A >= K):
        print(K)
        return
    elif (A + B >= K):
        print(A)
        return
    else:
        print(A - (K - A - B))

=======
Suggestion 5

def main():
    A,B,C,K = map(int,input().split())
    if K <= A:
        print(K)
    elif K <= A+B:
        print(A)
    else:
        print(A-(K-A-B))

main()

=======
Suggestion 6

def main():
    A, B, C, K = map(int, input().split())
    if K <= A:
        print(K)
    elif K <= A + B:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 7

def max_sum(a, b, c, k):
    if a >= k:
        return k
    elif a + b >= k:
        return a
    else:
        return a - (k - a - b)

=======
Suggestion 8

def main():
    a,b,c,k = map(int,input().split())
    if a >= k:
        print(k)
    elif a+b >= k:
        print(a)
    else:
        print(a-(k-a-b))
