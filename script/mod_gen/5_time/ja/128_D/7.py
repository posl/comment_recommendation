def solve(N, K, V):
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            tmp = []
            for k in range(i):
                tmp.append(V[k])
            for k in range(j):
                tmp.append(V[N - 1 - k])
            tmp.sort()
            for k in range(min(K - i - j, len(tmp))):
                if tmp[k] < 0:
                    tmp[k] = 0
            ans = max(ans, sum(tmp))
    return ans
N, K = map(int, input().split())
V = list(map(int, input().split()))
print(solve(N, K, V))

if __name__ == '__main__':
    solve()