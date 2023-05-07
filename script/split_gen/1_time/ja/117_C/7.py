def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(N, M, X)
    diff = []
    for i in range(M-1):
        diff.append(X[i+1]-X[i])
    diff.sort()
    #print(diff)
    ans = sum(diff[:M-N]) if M > N else 0
    print(ans)
