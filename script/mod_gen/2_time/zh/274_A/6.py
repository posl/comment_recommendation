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

if __name__ == '__main__':
    main()