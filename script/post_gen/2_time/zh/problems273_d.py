Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    h, w, r, c = map(int, input().split())
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    q = int(input())
    b = []
    for _ in range(q):
        b.append(list(input().split())))
    print(h, w, r, c)
    print(n)
    print(a)
    print(q)
    print(b)

=======
Suggestion 3

def solve(H, W, r_s, c_s, N, r, c, Q, d, l):
    # x, y = r_s, c_s
    # for i in range(Q):
    #     if d[i] == "L":
    #         for j in range(l[i]):
    #             y -= 1
    #             if (x, y) in zip(r, c):
    #                 y += 1
    #     elif d[i] == "R":
    #         for j in range(l[i]):
    #             y += 1
    #             if (x, y) in zip(r, c):
    #                 y -= 1
    #     elif d[i] == "U":
    #         for j in range(l[i]):
    #             x -= 1
    #             if (x, y) in zip(r, c):
    #                 x += 1
    #     else:
    #         for j in range(l[i]):
    #             x += 1
    #             if (x, y) in zip(r, c):
    #                 x -= 1
    #     print(x, y)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 0:上, 1:下, 2:左, 3:右
    d_idx = ["U", "D", "L", "R"]
    # 0:左, 1:右, 2:上, 3:下
    d_idx_rev = ["L", "R", "U", "D"]
    r = [x - 1 for x in r]
    c = [x - 1 for x in c]
    # 与当前方块相邻的方块
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(4):
            if 0 <= r[i] + dx[j] < H and 0 <= c[i] + dy[j] < W:
                adj[i].append((r[i] + dx[j], c[i] + dy[j]))
    # print(adj)
    # 当前方块的左右上下是否有墙
    wall =

=======
Suggestion 4

def main():
    h,w,r,c = map(int,input().split())
    n = int(input())
    wall = [[0 for i in range(w+1)] for j in range(h+1)]
    for i in range(n):
        x,y = map(int,input().split())
        wall[x][y] = 1
    q = int(input())
    move = []
    for i in range(q):
        d,l = input().split()
        move.append((d,int(l)))

    #print(wall)
    #print(move)
    #print(q)
    #print(h,w,r,c)
    #print(n)
    #print(wall)
    #print(move)
    #print(q)

    direction = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
    result = []
    for i in range(q):
        x,y = direction[move[i][0]]
        for j in range(move[i][1]):
            r += x
            c += y
            if wall[r][c] == 1:
                r -= x
                c -= y
        result.append((r,c))
    for i in result:
        print(i[0],i[1])

=======
Suggestion 5

def main():
    h,w,r,c = map(int,input().split())
    n = int(input())
    wall = set()
    for i in range(n):
        r_i,c_i = map(int,input().split())
        wall.add((r_i,c_i))
    q = int(input())
    move = []
    for i in range(q):
        d_i,l_i = input().split()
        move.append((d_i,int(l_i)))
    ans = []
    #print(move)
    for i in range(q):
        d_i,l_i = move[i]
        #print(d_i,l_i)
        if d_i == 'L':
            for j in range(l_i):
                if (r,c-1) not in wall:
                    c -= 1
                else:
                    break
        elif d_i == 'R':
            for j in range(l_i):
                if (r,c+1) not in wall:
                    c += 1
                else:
                    break
        elif d_i == 'U':
            for j in range(l_i):
                if (r-1,c) not in wall:
                    r -= 1
                else:
                    break
        elif d_i == 'D':
            for j in range(l_i):
                if (r+1,c) not in wall:
                    r += 1
                else:
                    break
        ans.append((r,c))
    #print(ans)
    for i in range(q):
        print(ans[i][0],ans[i][1])

=======
Suggestion 6

def main():
    h,w,r,c = map(int,input().split())
    n = int(input())
    wall = []
    for i in range(n):
        wall.append(list(map(int,input().split())))
    q = int(input())
    direction = []
    for i in range(q):
        direction.append(list(input().split()))
    for i in range(q):
        if direction[i][0] == "L":
            c = c - int(direction[i][1])
            if c < 1:
                c = 1
        elif direction[i][0] == "R":
            c = c + int(direction[i][1])
            if c > w:
                c = w
        elif direction[i][0] == "U":
            r = r - int(direction[i][1])
            if r < 1:
                r = 1
        elif direction[i][0] == "D":
            r = r + int(direction[i][1])
            if r > h:
                r = h
        if [r,c] in wall:
            if direction[i][0] == "L":
                c = c + int(direction[i][1])
                if c > w:
                    c = w
            elif direction[i][0] == "R":
                c = c - int(direction[i][1])
                if c < 1:
                    c = 1
            elif direction[i][0] == "U":
                r = r + int(direction[i][1])
                if r > h:
                    r = h
            elif direction[i][0] == "D":
                r = r - int(direction[i][1])
                if r < 1:
                    r = 1
        print(r,c)
main()

=======
Suggestion 7

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    r = [0] * N
    c = [0] * N
    for i in range(N):
        r[i], c[i] = map(int, input().split())
    Q = int(input())
    d = [0] * Q
    l = [0] * Q
    for i in range(Q):
        d[i], l[i] = map(str, input().split())
        l[i] = int(l[i])
    r_s -= 1
    c_s -= 1
    for i in range(N):
        r[i] -= 1
        c[i] -= 1
    for i in range(Q):
        if d[i] == 'L':
            for j in range(N):
                if r[j] == r_s and c[j] == c_s - l[i]:
                    break
            else:
                c_s -= l[i]
        elif d[i] == 'R':
            for j in range(N):
                if r[j] == r_s and c[j] == c_s + l[i]:
                    break
            else:
                c_s += l[i]
        elif d[i] == 'U':
            for j in range(N):
                if r[j] == r_s - l[i] and c[j] == c_s:
                    break
            else:
                r_s -= l[i]
        else:
            for j in range(N):
                if r[j] == r_s + l[i] and c[j] == c_s:
                    break
            else:
                r_s += l[i]
        print(r_s + 1, c_s + 1)

=======
Suggestion 8

def main():
    h, w, r_s, c_s = map(int, input().split())
    n = int(input())
    r = []
    c = []
    for i in range(n):
        tmp_r, tmp_c = map(int, input().split())
        r.append(tmp_r)
        c.append(tmp_c)
    q = int(input())
    d = []
    l = []
    for i in range(q):
        tmp_d, tmp_l = input().split()
        d.append(tmp_d)
        l.append(int(tmp_l))

    r_min = min(r)
    r_max = max(r)
    c_min = min(c)
    c_max = max(c)

    r_s_new = r_s
    c_s_new = c_s
    if r_s_new < r_min:
        r_s_new = r_min
    if r_s_new > r_max:
        r_s_new = r_max
    if c_s_new < c_min:
        c_s_new = c_min
    if c_s_new > c_max:
        c_s_new = c_max

    for i in range(q):
        if d[i] == 'L':
            c_s_new = c_s_new - l[i]
            if c_s_new < c_min:
                c_s_new = c_min
        elif d[i] == 'R':
            c_s_new = c_s_new + l[i]
            if c_s_new > c_max:
                c_s_new = c_max
        elif d[i] == 'U':
            r_s_new = r_s_new - l[i]
            if r_s_new < r_min:
                r_s_new = r_min
        else:
            r_s_new = r_s_new + l[i]
            if r_s_new > r_max:
                r_s_new = r_max
        print(r_s_new, c_s_new)
