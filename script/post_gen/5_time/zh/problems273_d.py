Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    R = []
    C = []
    for i in range(N):
        r, c = map(int, input().split())
        R.append(r)
        C.append(c)
    Q = int(input())
    D = []
    L = []
    for i in range(Q):
        d, l = input().split()
        D.append(d)
        L.append(l)
    print(H, W, rs, cs)
    print(N)
    for i in range(N):
        print(R[i], C[i])
    print(Q)
    for i in range(Q):
        print(D[i], L[i])

=======
Suggestion 2

def q273_d():
    pass

=======
Suggestion 3

def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    rcs = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    ds = [list(input().split()) for _ in range(Q)]
    # print(H, W, rs, cs)
    # print(N)
    # print(rcs)
    # print(Q)
    # print(ds)

    # # 初始化地图
    # map = [['.' for _ in range(W)] for _ in range(H)]
    # for rc in rcs:
    #     map[rc[0] - 1][rc[1] - 1] = '#'
    # map[rs - 1][cs - 1] = 'T'
    # for m in map:
    #     print(m)

    # # 指令
    # for d in ds:
    #     if d[0] == 'L':
    #         for _ in range(int(d[1])):
    #             if map[rs - 1][cs - 2] == '#':
    #                 pass
    #             else:
    #                 cs -= 1
    #             map[rs - 1][cs - 1] = 'T'
    #     elif d[0] == 'R':
    #         for _ in range(int(d[1])):
    #             if map[rs - 1][cs] == '#':
    #                 pass
    #             else:
    #                 cs += 1
    #             map[rs - 1][cs - 1] = 'T'
    #     elif d[0] == 'U':
    #         for _ in range(int(d[1])):
    #             if map[rs - 2][cs - 1] == '#':
    #                 pass
    #             else:
    #                 rs -= 1
    #             map[rs - 1][cs - 1] = 'T'
    #     elif d[0] == 'D':
    #         for _ in range(int(d[1])):
    #             if map[rs][cs - 1] == '#':
    #                 pass
    #             else:
    #                 rs += 1
    #             map[

=======
Suggestion 4

def main():
    h,w,r,c = map(int,input().split())
    n = int(input())
    wall = []
    for i in range(n):
        wall.append(list(map(int,input().split())))
    q = int(input())
    order = []
    for i in range(q):
        order.append(list(map(str,input().split())))
    #print(order)
    #print(wall)
    #print(order[0][0])
    #print(order[0][1])
    #print(order[1][0])
    #print(order[1][1])
    #print(order[2][0])
    #print(order[2][1])
    #print(order[3][0])
    #print(order[3][1])
    #print(order[4][0])
    #print(order[4][1])
    #print(order[5][0])
    #print(order[5][1])
    #print(order[6][0])
    #print(order[6][1])
    #print(order[7][0])
    #print(order[7][1])
    #print(order[8][0])
    #print(order[8][1])
    #print(order[9][0])
    #print(order[9][1])
    #print(order[10][0])
    #print(order[10][1])
    r = r - 1
    c = c - 1
    for i in range(q):
        if order[i][0] == 'L':
            for j in range(int(order[i][1])):
                if c - 1 >= 0:
                    if [r,c-1] in wall:
                        pass
                    else:
                        c = c - 1
        elif order[i][0] == 'R':
            for j in range(int(order[i][1])):
                if c + 1 <= w:
                    if [r,c+1] in wall:
                        pass
                    else:
                        c = c + 1
        elif order[i][0] == 'U':
            for j in range(int(order[i][1])):
                if r - 1 >= 0:
                    if [r-1,c] in wall:
                        pass
                    else:
                        r = r - 1
        elif order[i][0] == 'D':
            for j in range(int(order[i][1])):
                if r + 1 <= h

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def f1():
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
    # print(h, w, r_s, c_s)
    # print(n)
    # print(r)
    # print(c)
    # print(q)
    # print(d)
    # print(l)
    for i in range(q):
        if d[i] == 'L':
            c_s -= l[i]
            for j in range(n):
                if r[j] == r_s and c[j] <= c_s and c[j] >= c_s - l[i]:
                    c_s = c[j] - 1
                    break
        elif d[i] == 'R':
            c_s += l[i]
            for j in range(n):
                if r[j] == r_s and c[j] >= c_s and c[j] <= c_s + l[i]:
                    c_s = c[j] + 1
                    break
        elif d[i] == 'U':
            r_s -= l[i]
            for j in range(n):
                if c[j] == c_s and r[j] <= r_s and r[j] >= r_s - l[i]:
                    r_s = r[j] - 1
                    break
        elif d[i] == 'D':
            r_s += l[i]
            for j in range(n):
                if c[j] == c_s and r[j] >= r_s and r[j] <= r_s + l[i]:
                    r_s = r[j] + 1
                    break
        print(r_s, c_s)

=======
Suggestion 7

def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    r = []
    c = []
    for _ in range(N):
        r_i, c_i = map(int, input().split())
        r.append(r_i)
        c.append(c_i)
    Q = int(input())
    d = []
    l = []
    for _ in range(Q):
        d_i, l_i = input().split()
        d.append(d_i)
        l.append(int(l_i))

    #print(H, W, r_s, c_s)
    #print(N)
    #print(r)
    #print(c)
    #print(Q)
    #print(d)
    #print(l)

    #print(H, W, r_s, c_s, N, r, c, Q, d, l)
    #print(H, W, r_s, c_s, N, r, c, Q, d, l)
    #print(H, W, r_s, c_s, N, r, c, Q, d, l)

    #print(H, W, r_s, c_s, N, r, c, Q, d, l)

    #print(H, W, r_s, c_s, N, r, c, Q, d, l)
    #print(H, W, r_s, c_s, N, r, c, Q, d, l)

    #print(H, W, r_s, c_s, N, r, c, Q, d, l)
    #print(H, W, r_s, c_s, N, r, c, Q, d, l)

    #print(H, W, r_s, c_s, N, r, c, Q, d, l)
    #print(H, W, r_s, c_s, N, r, c, Q, d, l)

    #print(H, W, r_s, c_s, N, r, c, Q, d, l)
    #print(H, W, r_s, c_s, N, r, c, Q, d, l)

    #print(H, W, r_s, c_s, N, r, c, Q, d, l)
    #print(H, W, r_s, c_s, N, r, c, Q

=======
Suggestion 8

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
        d[i], l[i] = map(str, input().split())

    print(r, c, d, l)

    # r = [5, 2, 1]
    # c = [3, 2, 4]
    # d = ['L', 'U', 'L', 'R']
    # l = [2, 3, 2, 4]
    # h, w, r_s, c_s = 5, 5, 4, 4
    # n = 3
    # q = 4

    # r = [3, 4, 2, 3, 5, 1, 3]
    # c = [1, 3, 6, 4, 5, 1, 2]
    # d = ['D', 'U', 'L', 'D', 'U', 'D', 'U', 'R', 'L', 'D']
    # l = [3, 3, 2, 2, 3, 3, 3, 3, 3, 1]
    # h, w, r_s, c_s = 6, 6, 6, 3
    # n = 7
    # q = 10

    # r = [2, 5, 5, 4, 1, 2, 6, 4, 3, 4, 5, 3, 1, 2, 3, 4, 2, 5, 3, 1, 4, 2, 5, 1, 3, 6, 5, 3, 6, 4, 1, 2, 3, 4, 5, 6, 1, 3, 2, 4, 5
