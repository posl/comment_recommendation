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

if __name__ == '__main__':
    main()