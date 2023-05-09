def main():
    n, m = map(int, input().split())
    p = [0 for _ in range(n+1)]
    s = [0 for _ in range(n+1)]
    for i in range(m):
        pp, ss = input().split()
        pp = int(pp)
        if ss == 'AC':
            s[pp] = 1
        elif ss == 'WA':
            if s[pp] == 0:
                p[pp] += 1
    ac = 0
    wa = 0
    for i in range(n+1):
        if s[i] == 1:
            ac += 1
            wa += p[i]
    print(ac, wa)

if __name__ == '__main__':
    main()