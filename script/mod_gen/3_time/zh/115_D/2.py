def solve(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= 1 + a[N - 1]:
        return solve(N - 1, X - 1)
    else:
        return p[N - 1] + 1 + solve(N - 1, X - 2 - a[N - 1])
N, X = map(int, input().split())
a = [1]
p = [1]
for i in range(N):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)
print(solve(N, X))
