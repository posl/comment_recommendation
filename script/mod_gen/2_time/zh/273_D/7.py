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

if __name__ == '__main__':
    main()