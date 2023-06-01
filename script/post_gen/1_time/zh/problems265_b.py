Synthesizing 10/10 solutions

=======
Suggestion 1

def problems265_b():
    pass

=======
Suggestion 2

def solve():
    N,M,T=map(int,input().split())
    A=list(map(int,input().split()))
    XY=[]
    for i in range(M):
        XY.append(list(map(int,input().split())))
    XY.sort()
    t=T
    x=1
    for i in range(M):
        t-=XY[i][0]-x
        if t<=0:
            print("No")
            return
        t+=XY[i][1]
        x=XY[i][0]
    t-=N-x
    if t<=0:
        print("No")
    else:
        print("Yes")
    return

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def solve():
    pass

=======
Suggestion 6

def main():
    n,m,t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = []
    for _ in range(m):
        xy.append(list(map(int, input().split())))

    for i in range(m):
        a[xy[i][0]-2] += xy[i][1]

    for i in range(n-1):
        t -= a[i]
        if t <= 0:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    
    # 1. 预处理
    # 1.1. 从1号房间移动到i号房间的时间
    B = [0] * N
    for i in range(N-1):
        B[i+1] = B[i] + A[i]
    # 1.2. 奖励房间
    R = [0] * N
    for x, y in XY:
        R[x-1] = y
    
    # 2. 動的計画法
    # dp[i] := i号房间的时限
    dp = [0] * N
    dp[0] = T
    for i in range(N-1):
        dp[i+1] = min(dp[i+1], dp[i] - A[i])
        dp[i+1] = min(dp[i+1], T - B[i])
        dp[i+1] += R[i]
    return dp[N-1] >= 0

=======
Suggestion 8

def solve(n,m,t,a,x,y):
    for i in range(0,m):
        if t<=x[i]:
            return False
        else:
            t+=y[i]
    return True

=======
Suggestion 9

def main():
    # 读取输入
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    # 从1号房间开始，所以当前时间限制为T
    now = T
    # 遍历每个房间
    for i in range(N-1):
        # 消耗时间
        now -= A[i]
        # 如果时间到了，就返回No
        if now <= 0:
            print("No")
            return
        # 遍历奖励房间
        for j in range(M):
            # 如果当前房间是奖励房间，就增加时间
            if XY[j][0] == i + 1:
                now += XY[j][1]
    # 遍历完了，如果时间还有，就返回Yes
    if now > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    for i in range(n-1):
        t = t - a[i]
        if (i+1) in x:
            t = t + y[x.index(i+1)]
        if t <= 0:
            print("No")
            break
        if i == n-2:
            print("Yes")
main()
