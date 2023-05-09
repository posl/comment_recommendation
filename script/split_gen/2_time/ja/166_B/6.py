def main():
    N, K = map(int, input().split())
    d = [int(input()) for _ in range(K)]
    A = [[int(x) for x in input().split()] for _ in range(K)]
    #print(N, K, d, A)
    ans = 0
    for i in range(K):
        for j in range(d[i]):
            #print(A[i][j])
            if A[i][j] == 1:
                ans += 1
                break
    print(N - ans)
    return
