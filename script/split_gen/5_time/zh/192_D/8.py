def solve(X, M):
    d = int(max(X))
    if len(X) == 1:
        if int(X) <= M:
            return 1
        else:
            return 0
    else:
        X = list(X)
        X = [int(i) for i in X]
        X = [i-d for i in X]
        X = [str(i) for i in X]
        X = ''.join(X)
        X = int(X, d+1)
        if X <= M:
            return 1
        else:
            return 0
X = input()
M = int(input())
ans = 0
while True:
    ans += solve(X, M)
    X = int(X)
    X += 1
    X = str(X)
    if len(X) == 1:
        X = '0' + X
    if int(X) > M:
        break
print(ans)
