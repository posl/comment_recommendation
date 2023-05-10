def find_min_use(N, M, A):
    A.sort()
    B = []
    for i in range(M-1):
        B.append(A[i+1]-A[i]-1)
    B.append(A[0]-1)
    B.append(N-A[M-1])
    k = min(B)
    ans = 0
    for i in range(M):
        ans += (A[i]+k-1)//k
    return ans
N, M = map(int, input().split())
A = list(map(int, input().split()))
print(find_min_use(N, M, A))
