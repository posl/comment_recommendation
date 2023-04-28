Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            for k in range(h):
                for l in range(w):
                    if i == k and j == l:
                        continue
                    ans = min(ans, a[i][j] + a[k][l] + c * (abs(i - k) + abs(j - l)))
    print(ans)

=======
Suggestion 2

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for i2 in range(H):
                for j2 in range(W):
                    if i == i2 and j == j2:
                        continue
                    ans = min(ans, A[i][j] + A[i2][j2] + C * (abs(i - i2) + abs(j - j2)))
    print(ans)
    return

=======
Suggestion 3

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
Suggestion 4

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    ans = float('inf')
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))
    print(ans)

=======
Suggestion 5

def main():
    H, W, C = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    ans = 10**18
    for i in range(H):
        for j in range(W):
            ans = min(ans, A[i][j] + C * (i + j))
    for i in range(H):
        for j in range(W):
            ans = min(ans, A[i][j] - C * (i + j))
    print(ans)

=======
Suggestion 6

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]

    ans = 10**20
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i != k or j != l:
                        ans = min(ans, A[i][j] + A[k][l] + C*(abs(i-k) + abs(j-l)))

    print(ans)

=======
Suggestion 7

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    # print(H, W, C)
    # print(A)
    # print()

    minA = [[float('inf') for _ in range(W)] for _ in range(H)]
    minB = [[float('inf') for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                minA[i][j] = A[i][j]
            elif i == 0:
                minA[i][j] = min(minA[i][j-1], A[i][j])
            elif j == 0:
                minA[i][j] = min(minA[i-1][j], A[i][j])
            else:
                minA[i][j] = min(minA[i-1][j], minA[i][j-1], A[i][j])

    # print(minA)
    # print()

    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if i == H-1 and j == W-1:
                minB[i][j] = A[i][j]
            elif i == H-1:
                minB[i][j] = min(minB[i][j+1], A[i][j])
            elif j == W-1:
                minB[i][j] = min(minB[i+1][j], A[i][j])
            else:
                minB[i][j] = min(minB[i+1][j], minB[i][j+1], A[i][j])

    # print(minB)
    # print()

    minCost = float('inf')
    for i in range(H):
        for j in range(W):
            minCost = min(minCost, minA[i][j] + minB[i][j] + C*(i+j))

    print(minCost)

=======
Suggestion 8

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    minA = min([min(a) for a in A])
    minA_i, minA_j = 0, 0
    for i in range(H):
        for j in range(W):
            if A[i][j] == minA:
                minA_i, minA_j = i, j
    ans = 10**18
    for i in range(H):
        for j in range(W):
            ans = min(ans, A[i][j] + C * (abs(i - minA_i) + abs(j - minA_j)))
    print(ans)

=======
Suggestion 9

def main():
    h, w, c = [int(x) for x in input().split()]
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            ans = min(ans, a[i][j] + c * (i + j))
    for i in range(h):
        for j in range(w):
            ans = min(ans, a[i][j] - c * (i + j))
    print(ans)

=======
Suggestion 10

def main():
    from sys import stdin
    from bisect import bisect_left
    def input(): return stdin.readline().rstrip()
    def mi(): return map(int, input().split())
    def li(): return list(mi())
    H, W, C = mi()
    A = [li() for _ in range(H)]
    B = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            B[i][j] = A[i][j] - C * (i + j)
    B = [sorted(B[i]) for i in range(H)]
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i-k) + abs(j-l)))
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    x, y = min(i, k), min(j, l)
                    z, w = max(i, k), max(j, l)
                    if x == z:
                        if w - y == 1:
                            continue
                        t = B[z][bisect_left(B[z], A[x][y] - C * (x + y)) - 1]
                        ans = min(ans, A[i][j] + A[k][l] + C * (abs(i-k) + abs(j-l)) - t)
                    elif y == w:
                        if z - x == 1:
                            continue
                        t = B[z][bisect_left(B[z], A[x][y] - C * (x + y)) - 1]
                        ans = min(ans, A[i][j] + A[k][l] + C * (abs(i-k) + abs(j-l)) - t)
                    else:
                        if z - x == 1 and w - y == 1:
                            continue
                        t = B[z][bisect_left(B[z], A[x][y] - C * (x + y)) - 1]
                        ans = min(ans, A[i][j
