def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    t = T
    p = 0
    for i in range(N-1):
        t = t - A[i] + (X[p] - i - 1) * Y[p]
        if t <= 0:
            break
        if i+1 == X[p]:
            t += Y[p]
            p += 1
            if p == M:
                break
    if t > 0:
        print("Yes")
    else:
        print("No")
