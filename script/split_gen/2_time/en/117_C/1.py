def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    D = []
    for i in range(M-1):
        D.append(X[i+1] - X[i])
    D.sort()
    print(sum(D[:max(0, M-N)]))
