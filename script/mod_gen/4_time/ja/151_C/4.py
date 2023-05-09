def main():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        pi,si = input().split()
        p.append(int(pi))
        s.append(si)
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            ac += 1
        elif s[i] == 'WA':
            wa += 1
    print(ac,wa)

if __name__ == '__main__':
    main()