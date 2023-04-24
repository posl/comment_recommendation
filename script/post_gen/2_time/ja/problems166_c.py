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
    ans = 0
    for i in range(N):
        ok = True
        for j in range(M):
            if A[j] == i + 1:
                if H[i] <= H[B[j] - 1]:
                    ok = False
                    break
            elif B[j] == i + 1:
                if H[i] <= H[A[j] - 1]:
                    ok = False
                    break
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if A[j] == i + 1 and H[A[j] - 1] <= H[B[j] - 1]:
                flag = False
            if B[j] == i + 1 and H[B[j] - 1] <= H[A[j] - 1]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A - 1].append(B - 1)
        G[B - 1].append(A - 1)
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
Suggestion 4

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = 0
    for i in range(N):
        for j in range(M):
            if i == A[j]-1 and H[i] <= H[B[j]-1]:
                break
            if i == B[j]-1 and H[i] <= H[A[j]-1]:
                break
        else:
            ans += 1

    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a-1)
        B.append(b-1)

    # 隣接リスト
    G = [[] for _ in range(N)]
    for i in range(M):
        G[A[i]].append(B[i])
        G[B[i]].append(A[i])

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
Suggestion 6

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    ans = 0
    for i in range(n):
        ok = True
        for j in g[i]:
            if h[i] <= h[j]:
                ok = False
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        ok = True
        for j in range(M):
            if A[j] == i+1 and H[i] <= H[B[j]-1]:
                ok = False
                break
            if B[j] == i+1 and H[i] <= H[A[j]-1]:
                ok = False
                break
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if A[j]-1 == i:
                if H[i] <= H[B[j]-1]:
                    flag = False
                    break
            if B[j]-1 == i:
                if H[i] <= H[A[j]-1]:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    good = [True] * N
    for a, b in AB:
        if H[a - 1] < H[b - 1]:
            good[a - 1] = False
        elif H[a - 1] > H[b - 1]:
            good[b - 1] = False
        else:
            good[a - 1] = False
            good[b - 1] = False
    print(sum(good))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [tuple(map(int, input().split())) for _ in range(M)]

    # 隣接リスト
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    # 標高の高い方から順に訪問していく
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
