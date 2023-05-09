def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for p in permutations(range(1, N)):
        time = T[0][p[0]] + T[p[-1]][0]
        for i in range(N - 2):
            time += T[p[i]][p[i + 1]]
        if time == K:
            ans += 1
    print(ans)
