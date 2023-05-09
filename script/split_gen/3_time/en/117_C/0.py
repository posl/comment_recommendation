def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    D = [X[i+1] - X[i] for i in range(M-1)]
    D.sort()
    print(sum(D[:max(0, M-N)]))
