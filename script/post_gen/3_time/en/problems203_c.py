Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A = [0] + A + [10**100]
    B = [0] + B + [0]
    A = sorted(A)
    B = sorted(B)
    ans = 0
    for i in range(N + 1):
        if K >= A[i + 1] - A[i]:
            K -= A[i + 1] - A[i]
            ans = A[i + 1]
        else:
            ans += K
            K = 0
            break
    for i in range(N + 1):
        if K >= B[i + 1] - B[i]:
            K -= B[i + 1] - B[i]
            ans = B[i + 1]
        else:
            ans += K
            K = 0
            break
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A = A + [10**100]
    B = B + [0]
    A = A + [10**100]
    B = B + [0]
    A, B = zip(*sorted(zip(A, B)))
    A = list(A)
    B = list(B)
    #print(A)
    #print(B)
    ans = 0
    for i in range(N + 1):
        if K < A[i] - ans:
            ans += K
            break
        else:
            K -= A[i] - ans
            ans = A[i]
            K += B[i]
    print(ans)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    L = K
    R = 10**18
    while L + 1 < R:
        M = (L + R) // 2
        cnt = K
        for i in range(N):
            if M >= A[i]:
                cnt += B[i]
        if cnt >= M:
            L = M
        else:
            R = M
    print(L)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if K >= a - ans:
            K += b
            ans = a
    print(ans + K)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    for a, b in AB:
        if K >= a:
            K += b
        else:
            break
    print(K)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    for i in range(n):
        if k >= ab[i][0]:
            k += ab[i][1]
        else:
            break
    print(k)

=======
Suggestion 8

def main():
    N,K=map(int,input().split())
    A=[0]*N
    B=[0]*N
    for i in range(N):
        A[i],B[i]=map(int,input().split())

    A.append(1000000000000000000)

=======
Suggestion 9

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # print(N, K)
    # print(A)
    # print(B)
    # print()
    d = defaultdict(int)
    for i in range(N):
        d[A[i]] += B[i]
    # print(d)
    # pr
