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
