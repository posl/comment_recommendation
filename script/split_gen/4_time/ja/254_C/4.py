def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 'Yes'
    for i in range(N-K):
        if A[i] > A[i+K]:
            ans = 'No'
    print(ans)
