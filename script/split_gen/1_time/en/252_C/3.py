def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(10):
        d = {}
        for j in range(N):
            d[S[j][i]] = d.get(S[j][i], 0) + 1
        ans += max(d.values())
    print(ans)
