def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    #print(N, M, T, A, XY)
    now = 0
    for i in range(N-1):
        now += A[i]
        for j in range(M):
            if i+1 == XY[j][0]:
                now += XY[j][1]
        if now >= T:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    solve()