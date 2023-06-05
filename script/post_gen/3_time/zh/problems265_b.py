Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    room = 1
    time = t
    for i in range(n-1):
        time -= a[i]
        if time <= 0:
            print('No')
            exit()
        if i+1 in x:
            time += y[x.index(i+1)]
        room += 1
    if room == n:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    xy = [list(map(int,input().split())) for i in range(m)]
    #print(xy)
    for i in range(n-1):
        if a[i] >= xy[0][0]:
            a[i] += xy[0][1]
            xy.pop(0)
            if len(xy) == 0:
                break
        else:
            break
    #print(a)
    if a[-1] >= t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    A.append(0)
    A.insert(0,0)
    XY.sort()
    #print(A)
    #print(XY)
    for i in range(M):
        XY[i][0] += 1
    #print(XY)
    for i in range(M):
        A[XY[i][0]] += XY[i][1]
    #print(A)
    for i in range(1,N+1):
        A[i] += A[i-1]
    #print(A)
    for i in range(N):
        if A[i+1] - A[i] > A[i+1] - A[i-1]:
            A[i] = A[i+1]
    #print(A)
    if A[N] <= T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x.append(list(map(int,input().split())))
        y.append(x[i][1])
        x[i] = x[i][0]
    #print(n,m,t,a,x,y)
    #print(a)
    #print(x)
    #print(y)
    now = 1
    nowt = t
    for i in range(n-1):
        #print(i)
        #print(now)
        #print(nowt)
        #print(a[i])
        nowt -= a[i]
        if nowt <= 0:
            print('No')
            return
        if now == x[0]:
            nowt += y[0]
            x.pop(0)
            y.pop(0)
            if len(x) == 0:
                print('Yes')
                return
        now += 1
    print('No')
    return

=======
Suggestion 5

def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    dp = [0]*N
    dp[0] = T
    for i in range(N-1):
        dp[i+1] = min(dp[i]+A[i],T)
    for x,y in XY:
        if dp[x-1]+y>=T:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 6

def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]

    for i in range(N-1):
        A[i] = [A[i], i+1]

    A.sort(reverse=True)
    A.append([0, N])

    now = 1
    time = T
    for a, b in A:
        time -= now - b
        if time <= 0:
            print('No')
            exit(0)
        time += a
        now = b

    print('Yes')

=======
Suggestion 7

def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = []
    for i in range(M):
        XY.append(list(map(int,input().split())))
    #print(N,M,T,A,XY)
    now = 0
    for i in range(N-1):
        now += A[i]
        for j in range(M):
            if XY[j][0] == i+2:
                now += XY[j][1]
        if now >= T:
            print("No")
            return
    print("Yes")

=======
Suggestion 8

def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x1,y1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
    for i in range(m):
        if t + a[i] >= x[i]:
            t = t + a[i] + y[i]
        else:
            print("No")
            exit()
    if t >= n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def can_go(N, M, T, A, XY):
    xy = sorted(XY, key=lambda x: x[0])
    xy.append([N, 0])
    now = 1
    for x, y in xy:
        T -= x - now
        if T <= 0:
            return False
        T += y
        now = x
    return T >= N - now

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]
print('Yes' if can_go(N, M, T, A, XY) else 'No')

=======
Suggestion 10

def main():
    n,m,t=map(int,input().split())
    a=[int(x) for x in input().split()]
    xy=[]
    for i in range(m):
        xy.append([int(x) for x in input().split()])
    #print(n,m,t,a,xy)

    time=t
    room=1
    for i in range(n-1):
        time-=a[i]
        if time<=0:
            print('No')
            return
        if room==xy[0][0]:
            time+=xy[0][1]
            xy.pop(0)
        room+=1
    print('Yes')
