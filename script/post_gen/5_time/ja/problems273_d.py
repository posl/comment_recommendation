Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    wall = [[0 for col in range(W)] for row in range(H)]
    for i in range(N):
        r, c = map(int, input().split())
        wall[r-1][c-1] = 1
    Q = int(input())
    for i in range(Q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for j in range(l):
                if cs - 1 >= 0 and wall[rs-1][cs-1] == 0:
                    cs -= 1
        elif d == 'R':
            for j in range(l):
                if cs + 1 < W and wall[rs-1][cs] == 0:
                    cs += 1
        elif d == 'U':
            for j in range(l):
                if rs - 1 >= 0 and wall[rs-2][cs-1] == 0:
                    rs -= 1
        elif d == 'D':
            for j in range(l):
                if rs + 1 < H and wall[rs][cs-1] == 0:
                    rs += 1
        print(rs, cs)

=======
Suggestion 2

def main():
    H, W, r, c = map(int, input().split())
    N = int(input())
    wall = set()
    for i in range(N):
        r_i, c_i = map(int, input().split())
        wall.add((r_i, c_i))
    Q = int(input())
    d_l = [list(input().split()) for _ in range(Q)]
    d_l = [[d_l[i][0], int(d_l[i][1])] for i in range(Q)]
    r_c = [r, c]
    d = {'L': [-1, 0], 'R': [1, 0], 'U': [0, -1], 'D': [0, 1]}
    for i in range(Q):
        for _ in range(d_l[i][1]):
            r_c[0] += d[d_l[i][0]][0]
            r_c[1] += d[d_l[i][0]][1]
            if (r_c[0], r_c[1]) in wall:
                r_c[0] -= d[d_l[i][0]][0]
                r_c[1] -= d[d_l[i][0]][1]
                break
    print(r_c[0], r_c[1])

=======
Suggestion 3

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    r_c = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    d_l = [list(input().split()) for _ in range(Q)]

    #print(H, W, r_s, c_s)
    #print(N)
    #print(r_c)
    #print(Q)
    #print(d_l)

    # 1つ目の指示に対して高橋君は、左に 2 マス移動し、高橋君の位置は下記の通り、マス (4, 2) になります。
    # ...#.
    # .#...
    # .....
    # .T...
    # ..#..

    # 2 つ目の指示に対して高橋君は、上に 1 マスに移動した後、次の移動先が壁であるために「何もしない」を 2 回行います。その結果、高橋君の位置は下記の通り、マス (3, 2) になります。
    # ...#.
    # .#...
    # .T...
    # .....
    # ..#..

    # 3 つ目の指示に対して高橋君は、左に 1 マス移動した後、次の移動先となるマスが存在しないために「何もしない」を 1 回行います。その結果、高橋君の位置は下記の通り、マス (3, 1) になります。
    # ...#.
    # .#...
    # T....
    # .....
    # ..#..

    # 4 つ目の指示に対して高橋君は、右に 4 マス移動し、高橋君の位置は下記の通り、マス (3, 5) になります。
    # ...#.

=======
Suggestion 4

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
        l.append(int(l_i))

    #print(H, W, r_s, c_s)
    #print(N)
    #print(r)
    #print(c)
    #print(Q)
    #print(d)
    #print(l)

    # 1つ目の指示に対する処理
    #print(H, W, r_s, c_s)
    #print(N)
    #print(r)
    #print(c)
    #print(Q)
    #print(d)
    #print(l)
    #print("")

    # 2つ目以降の指示に対する処理
    #print(H, W, r_s, c_s)
    #print(N)
    #print(r)
    #print(c)
    #print(Q)
    #print(d)
    #print(l)
    #print("")

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    rc = []
    for i in range(N):
        rc.append(list(map(int, input().split())))
    Q = int(input())
    dl = []
    for i in range(Q):
        dl.append(list(input().split())))
    print(H, W, rs, cs)
    print(N)
    print(rc)
    print(Q)
    print(dl)

=======
Suggestion 7

def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    walls = []
    for i in range(N):
        r, c = map(int, input().split())
        walls.append((r, c))
    Q = int(input())
    query = []
    for i in range(Q):
        d, l = input().split()
        query.append((d, int(l)))

    wall_row = [0] * (H + 2)
    wall_col = [0] * (W + 2)
    for r, c in walls:
        wall_row[r] += 1
        wall_col[c] += 1

    row = rs
    col = cs
    for d, l in query:
        if d == 'L':
            for _ in range(l):
                col -= 1
                if wall_col[col] > 0:
                    col += 1
                    break
        elif d == 'R':
            for _ in range(l):
                col += 1
                if wall_col[col] > 0:
                    col -= 1
                    break
        elif d == 'U':
            for _ in range(l):
                row -= 1
                if wall_row[row] > 0:
                    row += 1
                    break
        elif d == 'D':
            for _ in range(l):
                row += 1
                if wall_row[row] > 0:
                    row -= 1
                    break
        else:
            assert False

    print(row, col)

=======
Suggestion 8

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    r_c = []
    for i in range(N):
        r_c.append(list(map(int, input().split())))
    Q = int(input())
    d_l = []
    for i in range(Q):
        d_l.append(list(input().split()))
    #print(H, W, r_s, c_s)
    #print(N)
    #print(r_c)
    #print(Q)
    #print(d_l)
    for i in range(Q):
        now_r = r_s
        now_c = c_s
        for j in range(int(d_l[i][1])):
            if d_l[i][0] == "L":
                now_c -= 1
                if [now_r, now_c] in r_c:
                    now_c += 1
            elif d_l[i][0] == "R":
                now_c += 1
                if [now_r, now_c] in r_c:
                    now_c -= 1
            elif d_l[i][0] == "U":
                now_r -= 1
                if [now_r, now_c] in r_c:
                    now_r += 1
            elif d_l[i][0] == "D":
                now_r += 1
                if [now_r, now_c] in r_c:
                    now_r -= 1
        print(now_r, now_c)

=======
Suggestion 9

def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    rcs = []
    for i in range(N):
        rcs.append(list(map(int, input().split())))
    Q = int(input())
    dls = []
    for i in range(Q):
        dls.append(list(input().split())))
    for i in range(Q):
        d = dls[i][0]
        l = int(dls[i][1])
        if d == "L":
            for j in range(l):
                if cs - 1 in [rcs[k][1] for k in range(N)]:
                    break
                cs -= 1
        elif d == "R":
            for j in range(l):
                if cs + 1 in [rcs[k][1] for k in range(N)]:
                    break
                cs += 1
        elif d == "U":
            for j in range(l):
                if rs - 1 in [rcs[k][0] for k in range(N)]:
                    break
                rs -= 1
        elif d == "D":
            for j in range(l):
                if rs + 1 in [rcs[k][0] for k in range(N)]:
                    break
                rs += 1
        else:
            print("error")
        print(rs, cs)
    return

=======
Suggestion 10

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
        l.append(int(l_i))
    
    #print(H, W, r_s, c_s, N, r, c, Q, d, l)
    #print(H, W, r_s, c_s, N, Q)
    #print(r)
    #print(c)
    #print(d)
    #print(l)
    #print(r_s, c_s)
    
    #print(H, W, r_s, c_s, N, r, c, Q, d, l)

    #print(H, W, r_s, c_s, N, Q)
    #print(r)
    #print(c)
    #print(d)
    #print(l)
    #print(r_s, c_s)

    #print(H, W, r_s, c_s, N, Q)
    #print(r)
    #print(c)
    #print(d)
    #print(l)
    #print(r_s, c_s)
    
    #print(H, W, r_s, c_s, N, Q)
    #print(r)
    #print(c)
    #print(d)
    #print(l)
    #print(r_s, c_s)
    
    #print(H, W, r_s, c_s, N, Q)
    #print(r)
    #print(c)
    #print(d)
    #print(l)
    #print(r_s, c_s)
    
    #print(H, W, r_s, c_s, N, Q)
    #print(r)
    #print(c)
    #print(d)
    #print(l)
    #print(r_s, c_s)
    
    #print(H, W, r_s, c_s, N, Q)
    #print(r)
    #print(c)
    #print(d)
    #print(l)
    #print(r_s, c_s)
    
    #print(H, W
