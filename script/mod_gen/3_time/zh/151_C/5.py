def main():
    N, M = map(int, input().split())
    p = []
    s = []
    for i in range(M):
        p_i, s_i = input().split()
        p.append(int(p_i))
        s.append(s_i)
    print(p)
    print(s)
    ac = 0
    wa = 0
    for i in range(M):
        if s[i] == 'AC':
            ac += 1
        elif s[i] == 'WA':
            wa += 1
    print(ac, wa)
    return

if __name__ == '__main__':
    main()