Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        if i+1 in [x for x,y in XY]:
            t += [y for x,y in XY if x == i+1][0]
            if t > T:
                t = T
    print("Yes")
    return

=======
Suggestion 2

def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for _ in range(m):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)

    time = t
    for i in range(n-1):
        time -= a[i]
        if time <= 0:
            print("No")
            exit()
        if (i+1) in x:
            time += y[x.index(i+1)]
            if time > t:
                time = t
    print("Yes")

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for i in range(m)]
    time = t
    room = 1
    for i in range(n-1):
        time -= a[i]
        if time <= 0:
            print('No')
            return
        if room < xy[0][0]:
            time += xy[0][1]
            room += 1
        else:
            xy.pop(0)
    print('Yes')

=======
Suggestion 5

def main():
    # 標準入力受付
    n,m,t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(m)]

    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]

    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]

    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]

    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]

    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]

    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]

    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]

    # 部屋に移動するための時間を計算
    for i in range(1,n):
        a[i] += a[i-1]

    # 持ち時間を計算
    t += a[-1]

    # ボーナス部屋の処理
    for x,y in xy:
        t += y - a[x-1]

    # 結果出力
    print("Yes" if t >= a[-1] else "No")

=======
Suggestion 6

def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    xy = [list(map(int,input().split())) for i in range(m)]
    now = t
    for i in range(n-1):
        now -= a[i]
        if now <= 0:
            print("No")
            exit()
        for j in range(m):
            if i+1 == xy[j][0]:
                now += xy[j][1]
                break
            elif i+1 < xy[j][0]:
                break
    print("Yes")

=======
Suggestion 7

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]

    time = T
    prev = 0
    for i in range(N-1):
        time -= A[i] - prev
        if time <= 0:
            print('No')
            return
        time += XY[i][1] - XY[i][0]
        if time > T:
            time = T
        prev = A[i]
    time -= A[N-1] - prev
    if time <= 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 8

def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for _ in range(m):
        i, j = map(int, input().split())
        x.append(i)
        y.append(j)
    
    now = t
    for i in range(n-1):
        now -= a[i]
        if now <= 0:
            print("No")
            return
        if i+1 in x:
            now += y[x.index(i+1)]
            if now > t:
                now = t
    
    print("Yes")

=======
Suggestion 9

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]

    now = 0
    for x, y in XY:
        T -= x - now
        if T <= 0:
            print("No")
            return
        T += y - x
        now = y
        if T > A[N-2]:
            T = A[N-2]
    T -= N - 1 - now
    if T <= 0:
        print("No")
        return
    print("Yes")

=======
Suggestion 10

def solve():
    N,M,T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    XY.sort()
    for x,y in XY:
        A.insert(x-1,y)
    for i in range(N-1):
        T -= A[i]
        if T <= 0:
            return False
    return True
