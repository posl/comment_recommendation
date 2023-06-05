def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    XY.sort()
    XY.append([N,0])
    now = 1
    nowT = T
    for x,y in XY:
        nowT -= x - now
        if nowT <= 0:
            print("No")
            return
        now = x
        nowT += y
        if nowT > T:
            nowT = T
    print("Yes")

if __name__ == '__main__':
    solve()