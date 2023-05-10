def solve():
    import sys
    input = sys.stdin.readline
    H, W, C = map(int, input().split())
    A = [[int(a) for a in input().split()] for _ in range(H)]
    ans = float('inf')
    for i in range(H):
        for j in range(W):
            for i2 in range(H):
                for j2 in range(W):
                    if i == i2 and j == j2:
                        continue
                    tmp = A[i][j] + A[i2][j2] + C * (abs(i - i2) + abs(j - j2))
                    ans = min(ans, tmp)
    print(ans)
