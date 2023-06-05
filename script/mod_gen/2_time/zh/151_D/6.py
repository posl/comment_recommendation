def main():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    p = []
    s = []
    for i in range(m):
        ps = input().split()
        p.append(int(ps[0]))
        s.append(ps[1])
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == "AC":
            ac += 1
        elif s[i] == "WA":
            wa += 1
    print(ac, wa)

if __name__ == '__main__':
    main()