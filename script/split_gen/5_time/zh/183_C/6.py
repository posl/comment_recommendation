def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1, n):
        ans += t[0][i]
    if k == ans:
        print(1)
        return
    import itertools
    for v in itertools.permutations(range(1, n)):
        now = 0
        for i in range(n - 2):
            now += t[v[i]][v[i + 1]]
        now += t[v[-1]][0]
        if now == k:
            ans += 1
    print(ans)
