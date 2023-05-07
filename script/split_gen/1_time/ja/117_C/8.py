def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    L = [X[i+1] - X[i] for i in range(M-1)]
    #print(L)
    L.sort()
    #print(L)
    print(sum(L[0:M-N]))
