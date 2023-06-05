def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    # print(A)
    # print(A[0:M])
    # print(sum([i*A[i] for i in range(M)]))
    # print(sum([i*A[i] for i in range(M,N)]))
    ans = sum([i*A[i] for i in range(M)])
    tmp = ans
    for i in range(M,N):
        tmp += (i+1)*A[i] - sum([j*A[j] for j in range(i-M+1,i)])
        ans = max(ans,tmp)
    print(ans)
