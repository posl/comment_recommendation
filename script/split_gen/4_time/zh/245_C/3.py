def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    for i in range(N):
        if A[i] > B[i]:
            print('No')
            return
    print('Yes')
