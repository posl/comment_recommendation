def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        p_tmp, s_tmp = input().split()
        p.append(int(p_tmp))
        s.append(s_tmp)
    print(p)
    print(s)
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            ac += 1
        elif s[i] == 'WA':
            wa += 1
    print(ac)
    print(wa)
    print(ac, wa)

if __name__ == '__main__':
    main()