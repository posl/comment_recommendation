def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    if N == K:
        print('Yes')
        return True
    else:
        for i in range(N-K):
            if A[i] > A[i+K]:
                print('No')
                return False
        print('Yes')
        return True
