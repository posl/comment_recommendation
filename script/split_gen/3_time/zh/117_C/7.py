def main():
    N, M = map(int, input().split())
    X = [int(x) for x in input().split()]
    X.sort()
    if N >= M:
        print(0)
    else:
        Y = []
        for i in range(M-1):
            Y.append(X[i+1]-X[i])
        Y.sort(reverse=True)
        print(sum(Y[N-1:]))
