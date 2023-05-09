def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    else:
        D = []
        for i in range(M-1):
            D.append(X[i+1]-X[i])
        D.sort(reverse=True)
        print(sum(D[N-1:]))
