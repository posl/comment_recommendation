Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h, w, r_s, c_s = map(int, input().split())
    n = int(input())
    r = []
    c = []
    for i in range(n):
        r_i, c_i = map(int, input().split())
        r.append(r_i)
        c.append(c_i)
    q = int(input())
    d = []
    l = []
    for i in range(q):
        d_i, l_i = map(str, input().split())
        d.append(d_i)
        l.append(l_i)
    print(h, w, r_s, c_s)
    print(n)
    print(r)
    print(c)
    print(q)
    print(d)
    print(l)

=======
Suggestion 2

def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    r = [0] * N
    c = [0] * N
    for i in range(N):
        r[i], c[i] = map(int, input().split())
    Q = int(input())
    d = [0] * Q
    l = [0] * Q
    for i in range(Q):
        d[i], l[i] = input().split()
        l[i] = int(l[i])

    #print(H, W, rs, cs)
    #print(N)
    #print(r)
    #print(c)
    #print(Q)
    #print(d)
    #print(l)

    # 1. 求出每个方块的左、右、上、下的邻接方块
    # 2. 求出每个方块的左、右、上、下的邻接方块中没有墙的方块
    # 3. 求出每个方块的左、右、上、下的邻接方块中没有墙的方块中的最小的方块
    # 4. 求出每个方块的左、右、上、下的邻接方块中没有墙的方块中的最小的方块的位置
    # 5. 求出每个方块的左、右、上、下的邻接方块中没有墙的方块中的最小的方块的位置的位置
    # 6. 求出每个方块的左、右、上、下的邻接方块中没有墙的方块中的最小的方块的位置的位置的方块
    # 7. 求出每个方块的左、右、上、下的邻接方块中没有墙的方块中的最小的方块的位置的位置的方块的位置
    # 8. 求出每个方块的左、右、上、

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    h, w, rs, cs = map(int, input().split())
    n = int(input())
    r = [0] * (n + 1)
    c = [0] * (n + 1)
    for i in range(1, n + 1):
        r[i], c[i] = map(int, input().split())
    q = int(input())
    d = [0] * (q + 1)
    l = [0] * (q + 1)
    for i in range(1, q + 1):
        d[i], l[i] = input().split()
        l[i] = int(l[i])
    # print(h, w, rs, cs)
    # print(n)
    # print(r, c)
    # print(q)
    # print(d, l)
    # print()

    # 1. 向左移动
    # 2. 向右移动
    # 3. 向上移动
    # 4. 向下移动
    # 5. 什么都不做
    # 6. 什么都不做
    # 7. 什么都不做
    # 8. 什么都不做
    # 9. 什么都不做
    # 10. 什么都不做
    # 11. 什么都不做
    # 12. 什么都不做
    # 13. 什么都不做
    # 14. 什么都不做
    # 15. 什么都不做
    # 16. 什么都不做
    # 17. 什么都不做
    # 18. 什么都不做
    # 19. 什么都不做
    # 20. 什么都不做
    # 21. 什么都不做
    # 22. 什么都不做
    # 23. 什么都不做
    # 24.

=======
Suggestion 5

def main():
    h, w, rs, cs = map(int, input().split())
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
        l[i] = int(l[i])
    # print(h, w, rs, cs)
    # print(r)
    # print(c)
    # print(q)
    # print(d)
    # print(l)

    # print(h, w, rs, cs, n, r, c, q, d, l)
    # print()

    # print(h, w, rs, cs, n, r, c, q, d, l)
    # print()

    # print(h, w, rs, cs, n, r, c, q, d, l)
    # print()

    # print(h, w, rs, cs, n, r, c, q, d, l)
    # print()

    # print(h, w, rs, cs, n, r, c, q, d, l)
    # print()

    # print(h, w, rs, cs, n, r, c, q, d, l)
    # print()

    # print(h, w, rs, cs, n, r, c, q, d, l)
    # print()

    # print(h, w, rs, cs, n, r, c, q, d, l)
    # print()

    # print(h, w, rs, cs, n, r, c, q, d, l)
    # print()

    # print(h, w, rs, cs, n, r, c, q, d, l)
    # print()
    # print(h, w, rs, cs, n, r, c, q, d, l)
    # print()

    # print(h, w, rs, cs, n, r, c, q, d, l)
    # print()
    # print(h, w, rs, cs, n, r, c, q, d,

=======
Suggestion 6

def main():
    h, w, r, c = map(int, input().split())
    n = int(input())
    grid = [[0 for i in range(w)] for i in range(h)]
    for i in range(n):
        r_i, c_i = map(int, input().split())
        grid[r_i - 1][c_i - 1] = 1
    q = int(input())
    for i in range(q):
        d, l = input().split()
        l = int(l)
        if d == 'L':
            for j in range(l):
                if c - 2 >= 0 and grid[r - 1][c - 2] == 0:
                    c -= 1
        elif d == 'R':
            for j in range(l):
                if c < w and grid[r - 1][c] == 0:
                    c += 1
        elif d == 'U':
            for j in range(l):
                if r - 2 >= 0 and grid[r - 2][c - 1] == 0:
                    r -= 1
        else:
            for j in range(l):
                if r < h and grid[r][c - 1] == 0:
                    r += 1
        print(r, c)

=======
Suggestion 7

def main():
    h, w, rs, cs = map(int, input().split())
    n = int(input())
    r = []
    c = []
    for i in range(n):
        a, b = map(int, input().split())
        r.append(a)
        c.append(b)
    q = int(input())
    d = []
    l = []
    for i in range(q):
        a, b = input().split()
        d.append(a)
        l.append(int(b))

    #print(h, w, rs, cs)
    #print(n)
    #print(r)
    #print(c)
    #print(q)
    #print(d)
    #print(l)

    #print(h, w, rs, cs)
    #print(n)
    #print(r)
    #print(c)
    #print(q)
    #print(d)
    #print(l)

    #print(h, w, rs, cs)
    #print(n)
    #print(r)
    #print(c)
    #print(q)
    #print(d)
    #print(l)

    #print(h, w, rs, cs)
    #print(n)
    #print(r)
    #print(c)
    #print(q)
    #print(d)
    #print(l)

    #print(h, w, rs, cs)
    #print(n)
    #print(r)
    #print(c)
    #print(q)
    #print(d)
    #print(l)

    #print(h, w, rs, cs)
    #print(n)
    #print(r)
    #print(c)
    #print(q)
    #print(d)
    #print(l)

    #print(h, w, rs, cs)
    #print(n)
    #print(r)
    #print(c)
    #print(q)
    #print(d)
    #print(l)

    #print(h, w, rs, cs)
    #print(n)
    #print(r)
    #print(c)
    #print(q)
    #print(d)
    #print(l)

    #print(h, w, rs, cs)
    #print(n)
    #print(r)
    #print(c)
    #print(q)
    #print(d)
    #print(l)

=======
Suggestion 8

def problems273_d():
    pass
