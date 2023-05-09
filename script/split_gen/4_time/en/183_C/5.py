def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(1, N):
        for j in range(i + 1, N):
            if T[i][j] + T[j][i] > K:
                ans += 1
    print(ans * 2)
