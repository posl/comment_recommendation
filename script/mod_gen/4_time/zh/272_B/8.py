def solve():
    N, M = map(int, input().split())
    A = [[0 for i in range(N)] for i in range(N)]
    for i in range(M):
        a = list(map(int, input().split()))
        for j in range(1, a[0]+1):
            for k in range(j+1, a[0]+1):
                A[a[j]-1][a[k]-1] = 1
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    solve()