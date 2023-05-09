def solve():
    N, M = map(int, input().split())
    B = []
    for n in range(N):
        B.append(list(map(int, input().split())))
    A = []
    for n in range(N):
        A.append([0]*M)
    for n in range(N):
        for m in range(M):
            A[n][m] = (n+1)*7+m+1
    for n in range(N):
        for m in range(M):
            if A[n][m] != B[n][m]:
                print('No')
                return
    print('Yes')
    return

if __name__ == '__main__':
    solve()