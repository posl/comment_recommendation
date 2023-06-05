def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    A.insert(0,0)
    A.append(0)
    now = 1
    for i in range(1,N):
        if now+1 == XY[0][0]:
            T += XY[0][1]
            XY.pop(0)
        T -= A[i]
        if T < 0:
            print('No')
            return
        now += 1
    print('Yes')
    return

if __name__ == '__main__':
    solve()