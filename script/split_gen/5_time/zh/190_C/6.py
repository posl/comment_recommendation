def dfs(i, balls):
    if i == K:
        return sum([1 if all([balls[a-1] and balls[b-1] for a, b in AB]) else 0 for AB in ABs])
    else:
        balls[C[i]-1] += 1
        res = dfs(i+1, balls)
        balls[C[i]-1] -= 1
        balls[D[i]-1] += 1
        res = max(res, dfs(i+1, balls))
        balls[D[i]-1] -= 1
        return res
N, M = map(int, input().split())
ABs = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
C, D = [], []
for _ in range(K):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)
print(dfs(0, [0]*N))
