Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(n):
        tmp = list(map(int,input().split()))
        x.append(tmp[0])
        y.append(tmp[1])
    print(x,y)
    print(n,k,a)

=======
Suggestion 3

def main():
    # 读入数据
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(n):
        xx,yy = map(int,input().split())
        x.append(xx)
        y.append(yy)
    # 计算最小值
    ans = 0
    for i in range(n):
        if i+1 in a:
            continue
        tmp = (x[i]**2+y[i]**2)**(1/2)
        if tmp > ans:
            ans = tmp
    print(ans)

=======
Suggestion 4

def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    # 二分法
    ok = 0
    ng = 100000000
    while ng - ok > 1e-6:
        mid = (ok + ng) / 2
        # 灯的坐标
        ax = [0] * k
        ay = [0] * k
        for i in range(k):
            ax[i] = x[a[i] - 1]
            ay[i] = y[a[i] - 1]
        # 求最小圆
        ok2 = 0
        ng2 = 100000000
        while ng2 - ok2 > 1e-6:
            mid2 = (ok2 + ng2) / 2
            # 判断是否所有人都被灯照亮
            ok3 = False
            for i in range(n):
                ok4 = False
                for j in range(k):
                    if (x[i] - ax[j]) ** 2 + (y[i] - ay[j]) ** 2 <= mid ** 2:
                        ok4 = True
                if not ok4:
                    ok3 = True
            if ok3:
                ok2 = mid2
            else:
                ng2 = mid2
        if ok2 <= mid:
            ok = mid
        else:
            ng = mid
    print(ok)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(N)]
    #print(N, K, A, XY)
    min_x = min([x for x, y in XY])
    max_x = max([x for x, y in XY])
    min_y = min([y for x, y in XY])
    max_y = max([y for x, y in XY])
    #print(min_x, max_x, min_y, max_y)
    min_r = 10**10
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            r = max([((x - x0)**2 + (y - y0)**2)**0.5 for x0, y0 in XY])
            #print(x, y, r)
            if r < min_r:
                min_r = r
    print(min_r)

main()

=======
Suggestion 6

def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i],y[i] = map(int,input().split())
    ans = 10**18
    for i in range(n):
        for j in range(i+1,n):
            for l in range(n):
                if l in a:
                    ans = min(ans,max((x[i]-x[l])**2+(y[i]-y[l])**2,(x[j]-x[l])**2+(y[j]-y[l])**2)**0.5)
    print(ans)
solve()

=======
Suggestion 7

def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for i in range(n):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)

    # 二分搜索
    left = 0
    right = 10 ** 9
    while right - left > 10 ** -6:
        mid = (left + right) / 2
        # 使得灯光强度为mid时，能够照亮的人的编号
        lighted = []
        for i in range(k):
            lighted.append(a[i])
        for i in range(n):
            if i not in lighted:
                for j in range(len(lighted)):
                    if (x[i] - x[lighted[j]]) ** 2 + (y[i] - y[lighted[j]]) ** 2 <= mid ** 2:
                        lighted.append(i)
                        break
        if len(lighted) == n:
            right = mid
        else:
            left = mid
    print(right)

=======
Suggestion 8

def get_distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 9

def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for i in range(n):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    # 二分查找
    left = 0
    right = 10 ** 9
    while right - left > 1e-6:
        mid = (left + right) / 2
        # 计算灯光覆盖的区域
        light = []
        for i in range(k):
            light.append((x[a[i] - 1], y[a[i] - 1], mid))
        while True:
            flag = False
            for i in range(len(light)):
                for j in range(i + 1, len(light)):
                    if (light[i][0] - light[j][0]) ** 2 + (light[i][1] - light[j][1]) ** 2 < (light[i][2] + light[j][2]) ** 2:
                        flag = True
                        light[i] = (light[i][0], light[i][1], max(light[i][2], light[j][2]))
                        light.pop(j)
                        break
                if flag:
                    break
            if not flag:
                break
        if len(light) == 1:
            right = mid
        else:
            left = mid
    print(right)
