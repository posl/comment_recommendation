def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for p in permutations(range(1, N)):
        t = 0
        now = 0
        for i in p:
            t += T[now][i]
            now = i
        t += T[now][0]
        if t == K:
            ans += 1
    print(ans)
