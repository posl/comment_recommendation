def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    SUM = sum(A)
    for i in range(M):
        if A[i] < SUM / (4*M):
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    solve()