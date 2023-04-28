Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A = [a - 1 for a in A]
    B = [b - 1 for b in B]
    good = [True] * N
    for i in range(M):
        if H[A[i]] >= H[B[i]]:
            good[B[i]] = False
        if H[A[i]] <= H[B[i]]:
            good[A[i]] = False
    print(sum(good))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A-1].append(B-1)
        G[B-1].append(A-1)
    ans = 0
    for i in range(N):
        flag = True
        for j in G[i]:
            if H[i] <= H[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        good = True
        for j in range(M):
            if A[j] == i+1 and H[i] <= H[B[j]-1]:
                good = False
                break
            if B[j] == i+1 and H[i] <= H[A[j]-1]:
                good = False
                break
        if good:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    good = [True] * n
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if h[a] == h[b]:
            good[a] = False
            good[b] = False
        elif h[a] < h[b]:
            good[a] = False
        else:
            good[b] = False
    print(sum(good))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(1, N+1):
        flag = True
        for a, b in AB:
            if i == a:
                if H[i-1] <= H[b-1]:
                    flag = False
                    break
            elif i == b:
                if H[i-1] <= H[a-1]:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(N):
        flag = True
        for a, b in AB:
            if a == i + 1 and H[i] <= H[b - 1]:
                flag = False
                break
            if b == i + 1 and H[i] <= H[a - 1]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    good = [True] * N
    for i in range(M):
        A, B = map(int, input().split())
        if H[A - 1] <= H[B - 1]:
            good[A - 1] = False
        if H[B - 1] <= H[A - 1]:
            good[B - 1] = False
    print(good.count(True))

main()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]

    good = [True] * N
    for a, b in AB:
        if H[a - 1] <= H[b - 1]:
            good[a - 1] = False
        if H[b - 1] <= H[a - 1]:
            good[b - 1] = False

    print(sum(good))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    good = [1 for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        if h[a-1] <= h[b-1]:
            good[a-1] = 0
        if h[a-1] >= h[b-1]:
            good[b-1] = 0
    print(sum(good))

main()

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    h = [0] * N
    for i in range(M):
        a, b = map(int, input().split())
        h[a - 1] = max(h[a - 1], H[b - 1])
        h[b - 1] = max(h[b - 1], H[a - 1])
    ans = 0
    for i in range(N):
        if H[i] > h[i]:
            ans += 1
    print(ans)
