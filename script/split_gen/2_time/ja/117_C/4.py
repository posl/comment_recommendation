def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    #print(N, M, X)
    X.sort()
    #print(X)
    diff = [abs(X[i] - X[i+1]) for i in range(M-1)]
    #print(diff)
    diff.sort(reverse=True)
    #print(diff)
    print(sum(diff[N-1:]))
