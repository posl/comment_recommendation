def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K == 1:
        if A == sorted(A):
            print('Yes')
        else:
            print('No')
        return
    if K == 2:
        if A == sorted(A):
            print('Yes')
        else:
            print('No')
        return
    if K > 2:
        if A == sorted(A):
            print('Yes')
        else:
            print('No')
        return
solve()
