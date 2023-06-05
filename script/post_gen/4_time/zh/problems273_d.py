Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    h, w, r_s, c_s = map(int, input().split())
    n = int(input())
    r = [0] * n
    c = [0] * n
    for i in range(n):
        r[i], c[i] = map(int, input().split())
    q = int(input())
    d = [0] * q
    l = [0] * q
    for i in range(q):
        d[i], l[i] = input().split()
        l[i] = int(l[i])

    # 墙的位置
    wall = [[0] * w for i in range(h)]
    for i in range(n):
        wall[r[i] - 1][c[i] - 1] = 1

    # 高桥的位置
    r_s -= 1
    c_s -= 1

    # 移动方向
    dr = [-1, 0, 1, 0] # 上、右、下、左
    dc = [0, 1, 0, -1]
    dir = ['U', 'R', 'D', 'L']

    # 移动
    for i in range(q):
        for j in range(4):
            if d[i] == dir[j]:
                for k in range(l[i]):
                    # 如果下一个位置没有墙，就移动过去
                    if 0 <= r_s + dr[j] < h and 0 <= c_s + dc[j] < w and wall[r_s + dr[j]][c_s + dc[j]] == 0:
                        r_s += dr[j]
                        c_s += dc[j]
                    # 如果下一个位置有墙，就不移动
                    else:
                        break
                break
        print(r_s + 1, c_s + 1)

=======
Suggestion 3

def main():
    h,w,r_s,c_s = map(int,input().split())
    n = int(input())
    r_c = [map(int,input().split()) for _ in range(n)]
    q = int(input())
    d_l = [input().split() for _ in range(q)]
    r_c = [[r,c] for r,c in r_c]
    d_l = [[d,int(l)] for d,l in d_l]
    for d,l in d_l:
        if d == "L":
            c_s -= l
        elif d == "R":
            c_s += l
        elif d == "U":
            r_s -= l
        elif d == "D":
            r_s += l
        print(r_s,c_s)

=======
Suggestion 4

def main():
    h,w,rs,cs = map(int,input().split())
    n = int(input())
    walls = []
    for i in range(n):
        walls.append(list(map(int,input().split())))
    q = int(input())
    commands = []
    for i in range(q):
        commands.append(list(input().split()))

    #print(h,w,rs,cs)
    #print(n)
    #print(walls)
    #print(q)
    #print(commands)

    #判断当前位置是否有墙
    def isWall(x,y):
        if [x,y] in walls:
            return True
        else:
            return False

    #判断当前位置是否在网格内
    def isInner(x,y):
        if x>=1 and x<=h and y>=1 and y<=w:
            return True
        else:
            return False

    #高桥移动
    def move(x,y,direction):
        if direction=='L':
            y -= 1
        elif direction=='R':
            y += 1
        elif direction=='U':
            x -= 1
        elif direction=='D':
            x += 1
        else:
            print('error')
        return x,y

    #高桥移动一次
    def moveOnce(x,y,direction):
        x,y = move(x,y,direction)
        if isInner(x,y) and not isWall(x,y):
            return x,y
        else:
            return x,y

    #高桥移动多次
    def moveMultiTimes(x,y,direction,times):
        for i in range(times):
            x,y = moveOnce(x,y,direction)
        return x,y

    #高桥移动多次，直到遇到墙
    def moveUntilWall(x,y,direction):
        while True:
            if isInner(x,y) and not isWall(x,y):
                x,y = moveOnce(x,y,direction)
            else:
                break
        return x,y

    #高桥移动多次，直到遇到墙或者网格边界
    def moveUntilWallOrBorder(x,y,direction):
        while True:
            if isInner(x,y) and not isWall(x,y):
                x,y = moveOnce(x,y,direction)
            else:

=======
Suggestion 5

def solve():
    H, W, r, c = map(int, input().split())
    N = int(input())
    R = []
    C = []
    for i in range(N):
        r_, c_ = map(int, input().split())
        R.append(r_)
        C.append(c_)
    Q = int(input())
    D = []
    L = []
    for i in range(Q):
        d_, l_ = map(str, input().split())
        D.append(d_)
        L.append(l_)
    for i in range(Q):
        if D[i] == 'L':
            if c - int(L[i]) >= 1:
                c -= int(L[i])
        elif D[i] == 'R':
            if c + int(L[i]) <= W:
                c += int(L[i])
        elif D[i] == 'U':
            if r - int(L[i]) >= 1:
                r -= int(L[i])
        elif D[i] == 'D':
            if r + int(L[i]) <= H:
                r += int(L[i])
        print(r, c)

=======
Suggestion 6

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    r = []
    c = []
    for i in range(N):
        r_i, c_i = map(int, input().split())
        r.append(r_i)
        c.append(c_i)
    Q = int(input())
    d = []
    l = []
    for i in range(Q):
        d_i, l_i = map(str, input().split())
        d.append(d_i)
        l.append(l_i)

    for i in range(Q):
        if d[i] == 'U':

            if r_s == min(r):
                r_s = r_s
            else:
                r_s = r_s - 1
        elif d[i] == 'D':
            if r_s == max(r):
                r_s = r_s
            else:
                r_s = r_s + 1
        elif d[i] == 'L':
            if c_s == min(c):
                c_s = c_s
            else:
                c_s = c_s - 1
        elif d[i] == 'R':
            if c_s == max(c):
                c_s = c_s
            else:
                c_s = c_s + 1
        print(r_s, c_s)
