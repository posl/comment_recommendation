def main():
    N,K = map(int, input().split())
    T = [[0] * N for _ in range(N)]
    for i in range(N):
        T[i] = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            for j in range(N):
                if j == 0:
                    continue
                if T[i][j] == K:
                    ans += 1
        else:
            for j in range(N):
                if j == i or j == 0:
                    continue
                if T[i][j] + T[j][0] == K:
                    ans += 1
    print(ans)
