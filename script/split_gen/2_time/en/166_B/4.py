def main():
    #input
    N, K = map(int, input().split())
    d = [int(input()) for _ in range(K)]
    A = [list(map(int, input().split())) for _ in range(K)]
    #compute
    ans = 0
    for i in range(K):
        for j in range(d[i]):
            if A[i][j] == 1:
                ans += 1
    #output
    print(N-ans)
