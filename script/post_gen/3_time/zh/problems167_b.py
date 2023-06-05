Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def max_sum(A,B,C,K):
    if A >= K:
        return K
    elif A + B >= K:
        return A
    else:
        return A - (K - A - B)

=======
Suggestion 2

def main():
    a,b,c,k = map(int, input().split())
    if a >= k:
        print(k)
    elif a + b >= k:
        print(a)
    else:
        print(a - (k - a - b))

=======
Suggestion 3

def main():
    a,b,c,k = map(int, input().split())
    if a >= k:
        print(k)
    elif a + b >= k:
        print(a)
    else:
        print(a - (k - a - b))
main()

=======
Suggestion 4

def main():
    a, b, c, k = map(int, input().split())
    print(a - b if k % 2 == 0 else b - a)

=======
Suggestion 5

def solve():
    A,B,C,K = map(int,input().split())
    if A >= K:
        print(K)
        return
    elif A+B >= K:
        print(A)
        return
    else:
        print(A-(K-A-B))

=======
Suggestion 6

def max_sum_card(A,B,C,K):
    if K <= A:
        return K
    elif K <= A + B:
        return A
    else:
        return A - (K - A - B)

=======
Suggestion 7

def solve():
    A,B,C,K = map(int, input().split())
    if A >= K:
        print(K)
    elif A+B >= K:
        print(A)
    else:
        print(A-(K-A-B))

=======
Suggestion 8

def main():
    A, B, C, K = map(int, input().split())

    if K <= A:
        print(K)
    elif K <= A + B:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 9

def max_sum(A, B, C, K):
    if K <= A:
        return K
    elif K <= A + B:
        return A
    else:
        return A - (K - A - B)

A, B, C, K = map(int, input().split())

print(max_sum(A, B, C, K))
