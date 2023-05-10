def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(N+1):
        for r in range(N+1):
            if l + r > K:
                continue
            if l + r > N:
                continue
            if l + r == 0:
                continue
            if l + r == K:
                ans = max(ans, sum(V))
                continue
            v = V[:l] + V[N-r:]
            v.sort()
            for i in range(min(K - (l+r), len(v))):
                if v[i] >= 0:
                    break
                v[i] = 0
            ans = max(ans, sum(v))
    print(ans)

if __name__ == '__main__':
    solve()