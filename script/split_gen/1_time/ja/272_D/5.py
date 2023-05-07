def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    ans = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (i - j) % 2 == 0:
                if (i + j) % 2 == 0:
                    if (i + j) // 2 <= M:
                        ans[i][j] = (i + j) // 2
    for i in range(N):
        print(*ans[i])
