def solve():
    # 整数 1 つ
    N,M,T = map(int, input().split())
    # 整数複数個
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    # 出力
    # print(N,M,T)
    # print(A)
    # print(XY)
    # print(N,M,T,A,XY)
    t = T
    n = N
    for i in range(N-1):
        t = t - A[i]
        if t<=0:
            print("No")
            return
        for xy in XY:
            if i+1 == xy[0]:
                t = t + xy[1]
                break
    print("Yes")
    return

if __name__ == '__main__':
    solve()