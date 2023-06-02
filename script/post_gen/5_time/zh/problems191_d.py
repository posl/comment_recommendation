Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def readinput():
    x,y,r=map(float,input().split())
    return x,y,r

=======
Suggestion 2

def solve(x, y, r):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    return 0

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    x, y, r = map(float, input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    x1 = x - r
    x2 = x + r
    count = 0
    for i in range(x1, x2+1):
        y1 = y - r
        y2 = y + r
        for j in range(y1, y2+1):
            if (i-x)**2 + (j-y)**2 <= r**2:
                count += 1
    print(count)

=======
Suggestion 5

def count(x, y, r):
    x1 = int(x - r)
    x2 = int(x + r)
    y1 = int(y - r)
    y2 = int(y + r)

    cnt = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if (x - x1) * (x - x1) + (y - y1) * (y - y1) <= r * r:
                cnt += 1
    return cnt

=======
Suggestion 6

def main():
    #输入
    x,y,r = map(float, input().split())
    #计算
    x1 = int(x-r)
    x2 = int(x+r)
    count = 0
    for i in range(x1,x2+1):
        #y = sqrt(r^2-(x-x0)^2)+y0
        y1 = y + (r**2-(i-x)**2)**0.5
        y2 = y - (r**2-(i-x)**2)**0.5
        count += int(y1) - int(y2)
    #输出
    print(count*4+4)
main()

=======
Suggestion 7

def main():
    #input
    X,Y,R = map(float,input().split())
    x = int(X*10000)
    y = int(Y*10000)
    r = int(R*10000)
    #solve
    x_min = x-r
    x_max = x+r
    y_min = y-r
    y_max = y+r
    ans = 0
    for i in range(x_min,x_max+1):
        for j in range(y_min,y_max+1):
            if (i-x)**2+(j-y)**2 <= r**2:
                ans += 1
    print(ans)

=======
Suggestion 8

def count_grid_points(x, y, r):
    #圆内网格点数
    #圆上网格点数
    #圆外网格点数
    #圆内网格点数+圆上网格点数+圆外网格点数=圆内网格点数+圆上网格点数+圆外网格点数
    #圆内网格点数+圆上网格点数+圆外网格点数=2*圆内网格点数+圆上网格点数
    #圆上网格点数=圆内网格点数+圆外网格点数
    #圆上网格点数=2*圆内网格点数+圆上网格点数
    #圆上网格点数=圆内网格点数
    #圆上网格点数=圆内网格点数+圆外网格点数
    #圆内网格点数=圆外网格点数
    #圆内网格点数=圆外网格点数=圆上网格点数
    #圆内网格点数=圆外网格点数=圆上网格点数=圆内网格点数+圆外网格点数
    #圆内网格点数=圆外网格点数=圆上网格点数=圆内网格点数+圆外网格点数=圆内网格点数+圆上网格点数+圆外网格点数
    #圆内网格点数=圆外网格点数=圆上网格点数=圆内网格点数+圆外网格点数=圆内网格点数+圆上网格点数+圆外网格点数=圆内网格点数+圆上网格点数+圆外网格点数
    #圆内网格点数=圆外网格点数=圆上网格点数=

=======
Suggestion 9

def count_points(x, y, r):
    # 网格点数
    points = 0
    # 网格点坐标
    x0 = int(x)
    y0 = int(y)
    # 半径
    r2 = r * r
    # 遍历网格点
    for x in range(x0 - int(r), x0 + int(r) + 1):
        for y in range(y0 - int(r), y0 + int(r) + 1):
            # 判断网格点是否在圆内
            if (x - x0) * (x - x0) + (y - y0) * (y - y0) <= r2:
                points += 1
    return points
