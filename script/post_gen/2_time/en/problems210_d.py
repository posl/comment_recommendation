Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 1000

=======
Suggestion 2

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            ans = min(ans, a[i][j] + c * (i + j), a[i][j] - c * (i + j))
    for i in range(h):
        for j in range(w):
            ans = min(ans, a[i][j] + c * (i - j), a[i][j] - c * (i - j))
    print(ans)

=======
Suggestion 3

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            tmp = 0
            for k in range(h):
                for l in range(w):
                    tmp = max(tmp, a[i][j] + a[k][l] - c * (i - k + j - l))
            ans = min(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i-k) + abs(j-l)))
    print(ans)

=======
Suggestion 5

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            a[i][j] -= c * (i + j)
    for i in range(h):
        for j in range(w):
            for k in range(h):
                for l in range(w):
                    if i == k and j == l:
                        continue
                    ans = min(ans, a[i][j] + a[k][l] + c * (abs(i - k) + abs(j - l)))
    print(ans)

=======
Suggestion 6

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_cost = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    cost = A[i][j] + A[k][l] + C * (abs(i-k) + abs(j-l))
                    min_cost = min(min_cost, cost)
    print(min_cost)

=======
Suggestion 7

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]

    ans = 10**20
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))

    print(ans)

=======
Suggestion 8

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_A = [[float('inf') for _ in range(W)] for _ in range(H)]
    min_A[0][0] = A[0][0]
    for h in range(H):
        for w in range(W):
            if h > 0:
                min_A[h][w] = min(min_A[h][w], min_A[h-1][w])
            if w > 0:
                min_A[h][w] = min(min_A[h][w], min_A[h][w-1])
            min_A[h][w] = min(min_A[h][w], A[h][w])
    ans = float('inf')
    for h in range(H):
        for w in range(W):
            ans = min(ans, min_A[h][w] + A[h][w] + C * (h + w))
    print(ans)

=======
Suggestion 9

def main():
    from sys import stdin
    import numpy as np

    H, W, C = map(int, stdin.readline().split())
    A = np.array([list(map(int, stdin.readline().split())) for i in range(H)])
    B = np.array([list(map(int, stdin.readline().split())) for i in range(H)])

    result = A[0, 0] + B[0, 0] + C * (H + W - 2)

    for i in range(H):
        for j in range(W):
            temp = A[i, j] + B[i, j] + C * (i + j)
            result = min(result, temp)

    for i in range(H):
        for j in range(W):
            temp = A[i, j] + B[i, j] + C * (H - i - 1 + W - j - 1)
            result = min(result, temp)

    print(result)
