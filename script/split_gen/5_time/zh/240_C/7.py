def canReach(X, N, a, b):
    # 从第N次开始跳
    if X == 0:
        return True
    if N == 0:
        return False
    if X < 0:
        return False
    return canReach(X - a[N - 1], N - 1, a, b) or canReach(X - b[N - 1], N - 1, a, b)
N, X = map(int, input().split())
a = []
b = []
for i in range(N):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
