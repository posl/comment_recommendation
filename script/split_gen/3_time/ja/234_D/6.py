def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K)
    #print(P)
    #print(P[K-1:N])
    #print(sorted(P[K-1:N]))
    ans = sorted(P[K-1:N])
    for i in range(K):
        print(ans[i])
