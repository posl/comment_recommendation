def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * Q
    K = [0] * Q
    for i in range(Q):
        X[i], K[i] = map(int, input().split())
    # dictionary of lists
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]].append(i)
        else:
            d[A[i]] = [i]
    for i in range(Q):
        if X[i] in d and len(d[X[i]]) >= K[i]:
            print(d[X[i]][K[i] - 1] + 1)
        else:
            print(-1)
