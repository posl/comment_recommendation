def find_min_step():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    if N == 1:
        return 0
    X.sort()
    diff = []
    for i in range(M - 1):
        diff.append(X[i + 1] - X[i])
    diff.sort()
    return sum(diff[:M - N])
print(find_min_step())
