Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def get_input():
    h, w, r_s, c_s = map(int, input().split())
    n = int(input())
    r_c_list = []
    for i in range(n):
        r, c = map(int, input().split())
        r_c_list.append((r, c))
    q = int(input())
    d_l_list = []
    for i in range(q):
        d, l = input().split()
        d_l_list.append((d, int(l)))
    return h, w, r_s, c_s, n, r_c_list, q, d_l_list

=======
Suggestion 3

def main():
    h,w,r_s,c_s = map(int,input().split())
    n = int(input())
    r_c = []
    for i in range(n):
        r_c.append(list(map(int,input().split())))
    q = int(input())
    d_l = []
    for i in range(q):
        d_l.append(list(input().split()))
    print(h,w,r_s,c_s)
    print(n)
    print(r_c)
    print(q)
    print(d_l)
    return

=======
Suggestion 4

def get_next_position(x,y,direction):
    if direction == 'L':
        y -= 1
    elif direction == 'R':
        y += 1
    elif direction == 'U':
        x -= 1
    elif direction == 'D':
        x += 1
    return x,y

=======
Suggestion 5

def main():
    h, w, rs, cs = [int(x) for x in input().split()]
    n = int(input())
    rcs = [[int(x) for x in input().split()] for _ in range(n)]
    q = int(input())
    dls = [[x for x in input().split()] for _ in range(q)]
    walls = set()
    for rc in rcs:
        walls.add((rc[0], rc[1]))
    r, c = rs, cs
    for dl in dls:
        d, l = dl[0], int(dl[1])
        if d == 'L':
            for i in range(l):
                if (r, c - 1) not in walls:
                    c -= 1
        if d == 'R':
            for i in range(l):
                if (r, c + 1) not in walls:
                    c += 1
        if d == 'U':
            for i in range(l):
                if (r - 1, c) not in walls:
                    r -= 1
        if d == 'D':
            for i in range(l):
                if (r + 1, c) not in walls:
                    r += 1
        print(r, c)

=======
Suggestion 6

def main():
    h, w, r_s, c_s = map(int, input().split())
    n = int(input())
    r_c = [list(map(int, input().split())) for _ in range(n)]
    q = int(input())
    q_d = [list(input().split()) for _ in range(q)]
    d = {"L": [-1, 0], "R": [1, 0], "U": [0, -1], "D": [0, 1]}
    r_s, c_s = r_s - 1, c_s - 1
    r_c = [[r - 1, c - 1] for r, c in r_c]
    r_c.sort(key=lambda x: (x[0], x[1]))
    r_c.append([h, w])
    r_c.insert(0, [-1, -1])
    s = 0
    for i in range(1, len(r_c)):
        s += (r_c[i][0] - r_c[i - 1][0] - 1) * (r_c[i][1] - r_c[i - 1][1] - 1)
    print(s)
    for d_i, l_i in q_d:
        d_i = d[d_i]
        l_i = int(l_i)
        r, c = r_s, c_s
        while l_i > 0:
            if d_i[0] == 0:
                if r + d_i[1] == -1 or r + d_i[1] == h:
                    break
                elif [r + d_i[1], c] in r_c:
                    break
                else:
                    r += d_i[1]
            else:
                if c + d_i[0] == -1 or c + d_i[0] == w:
                    break
                elif [r, c + d_i[0]] in r_c:
                    break
                else:
                    c += d_i[0]
            l_i -= 1
        print(r + 1, c + 1)

=======
Suggestion 7

def main():
    H,W,r_s,c_s = map(int,input().split())
    N = int(input())
    r = []
    c = []
    for i in range(N):
        r_i,c_i = map(int,input().split())
        r.append(r_i)
        c.append(c_i)
    Q = int(input())
    d = []
    l = []
    for i in range(Q):
        d_i,l_i = map(str,input().split())
        d.append(d_i)
        l.append(l_i)
    for i in range(Q):
        if d[i] == 'L':
            if c_s - int(l[i]) >= 1:
                c_s = c_s - int(l[i])
                print(r_s,c_s)
            else:
                print(r_s,c_s)
        elif d[i] == 'R':
            if c_s + int(l[i]) <= W:
                c_s = c_s + int(l[i])
                print(r_s,c_s)
            else:
                print(r_s,c_s)
        elif d[i] == 'U':
            if r_s - int(l[i]) >= 1:
                r_s = r_s - int(l[i])
                print(r_s,c_s)
            else:
                print(r_s,c_s)
        elif d[i] == 'D':
            if r_s + int(l[i]) <= H:
                r_s = r_s + int(l[i])
                print(r_s,c_s)
            else:
                print(r_s,c_s)
        else:
            print(r_s,c_s)
