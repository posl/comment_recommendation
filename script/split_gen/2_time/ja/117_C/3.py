def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    L = []
    for i in range(M-1):
        L.append(X[i+1]-X[i])
    #print(L)
    L.sort()
    #print(L)
    if N >= M:
        print(0)
    else:
        print(sum(L[:M-N]))
