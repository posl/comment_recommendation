def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(N, M)
    #print(X)
    diff = [X[i + 1] - X[i] for i in range(M - 1)]
    diff.sort()
    #print(diff)
    if N >= M:
        print(0)
    else:
        print(sum(diff[:M - N]))
