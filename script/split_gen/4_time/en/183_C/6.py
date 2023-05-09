def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, N):
        ans += T[0][i]
    ans += T[0][N - 1]
    if ans == K:
        ans = 1
    else:
        ans = 0
    print(ans)
