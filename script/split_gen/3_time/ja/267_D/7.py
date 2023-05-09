def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if j-i < M:
                continue
            #print(i, j)
            B = A[i:j]
            #print(B)
            B.sort(reverse=True)
            #print(B)
            tmp = 0
            for k in range(M):
                tmp += (k+1) * B[k]
            #print(tmp)
            ans = max(ans, tmp)
    print(ans)
