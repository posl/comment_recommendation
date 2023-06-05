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
