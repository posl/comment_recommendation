def solve():
    K,N = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.append(A[0]+K)
    m = 0
    for i in range(N):
        m = max(m,A[i+1]-A[i])
    print(K-m)
solve()
