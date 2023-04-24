Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    L.sort()
    R.sort()

    ans = 0
    for i in range(N):
        if L[i] + D - 1 < R[i]:
            ans += 1

    print(ans)

=======
Suggestion 2

def main():
    #入力
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    #壁の位置をソート
    #壁の位置をソートしておくと、次のようにして、
    #その位置にある壁のうち、最も右にある壁の位置を
    #二分探索で求めることができます。
    #壁の位置をソートしておくと、次のようにして、
    #その位置にある壁のうち、最も右にある壁の位置を
    #二分探索で求めることができます。
    #壁の位置をソートしておくと、次のようにして、
    #その位置にある壁のうち、最も右にある壁の位置を
    #二分探索で求めることができます。
    X = []
    for i in range(N):
        X.append(L[i])
        X.append(R[i])
    X.sort()
    X = list(set(X)) #重複を削除

    #壁の位置を座標圧縮
    #壁の位置を座標圧縮しておくと、次のようにして、
    #その位置にある壁のうち、最も右にある壁の位置を
    #二分探索で求めることができます。
    #壁の位置を座標圧縮しておくと、次のようにして、
    #その位置にある壁のうち、最も右にある壁の位置を
    #二分探索で求めることができます。
    #壁の位置を座標圧縮しておくと、次のように

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    wall = []
    for i in range(N):
        l, r = map(int, input().split())
        wall.append([l, r])
    wall.sort(key=lambda x: x[0])
    #print(wall)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if wall[j][0] - wall[i][1] <= D:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    wall = [list(map(int, input().split())) for _ in range(N)]
    wall.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if wall[i][1] - wall[i][0] + 1 >= D:
            ans += 1
        else:
            for j in range(i + 1, N):
                if wall[j][0] <= wall[i][1] + D:
                    wall[j][0] = wall[i][1] + 1
                else:
                    break
    print(ans)

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(N)]
    walls.sort(key=lambda x: x[1])
    ans = 0
    r = 0
    for l, r in walls:
        if r < r:
            ans += 1
        else:
            r = l + D - 1
    print(ans)

=======
Suggestion 6

def main():
    n, d = map(int, input().split())
    wall = []
    for _ in range(n):
        l, r = map(int, input().split())
        wall.append((r, l))
    wall.sort()
    ans = 0
    for i in range(n):
        if wall[i][1] > d:
            ans += 1
            d = wall[i][0]
        else:
            d = min(d, wall[i][0])
    ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, D = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x:x[0])
    ans = 0
    for i in range(N):
        if LR[i][0] <= LR[i][1] - D + 1:
            ans += 1
            LR[i][0] = LR[i][1] - D + 2
            for j in range(i+1, N):
                if LR[j][0] <= LR[i][1] - D + 1:
                    LR[j][0] = LR[i][1] - D + 2
                else:
                    break
    print(ans)

=======
Suggestion 8

def main():
    N, D = map(int,input().split())
    wall = []
    for i in range(N):
        L, R = map(int,input().split())
        wall.append([L,R])
    wall.sort()
    ans = 0
    for i in range(N):
        if wall[i][0] < wall[i-1][1]:
            wall[i][1] = min(wall[i-1][1], wall[i][1])
        if wall[i][1] - wall[i][0] + 1 >= D:
            ans += 1
            wall[i][0] = wall[i][1] - D + 1
    print(ans)

=======
Suggestion 9

def main():
    N,D = map(int,input().split())
    wall = [list(map(int,input().split())) for i in range(N)]
    wall.sort(key=lambda x:x[1])
    #print(wall)
    ans = 0
    for i in range(N):
        if wall[i][0] > D:
            wall[i][0] -= D
            wall[i][1] -= D
        else:
            wall[i][0] = 1
            wall[i][1] -= D
        if wall[i][0] <= 0:
            wall[i][0] = 1
    wall.sort(key=lambda x:x[0])
    #print(wall)
    for i in range(N):
        if wall[i][0] == 1:
            ans += 1
            for j in range(i+1,N):
                if wall[j][0] <= wall[i][1]:
                    wall[j][0] = wall[i][1] + 1
                else:
                    break
    print(ans)

=======
Suggestion 10

def main():
    n,d = map(int,input().split())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort(key = lambda x:x[1])
    cnt = 0
    for i in range(n):
        if l[i][0] > l[i][1]:
            continue
        for j in range(i+1,n):
            if l[i][1]+d-1 < l[j][0]:
                break
            if l[i][1]+d-1 >= l[j][1]:
                l[j][0] = l[i][1]+d
            else:
                l[j][0] = l[i][1]+d
                cnt += 1
                break
        cnt += 1
    print(cnt)
