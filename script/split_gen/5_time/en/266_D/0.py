def main():
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    max = 0
    for i in range(N):
        if i == 0:
            max += A[i]
            continue
        t = T[i] - T[i-1]
        x = abs(X[i] - X[i-1])
        if t < x:
            continue
        elif t == x:
            max += A[i]
        else:
            max += A[i] - (t - x)
    print(max)
