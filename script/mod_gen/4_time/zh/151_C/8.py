def main():
    n, m = map(int, input().split())
    p = [0] * m
    s = [0] * m
    for i in range(m):
        p[i], s[i] = map(str, input().split())
    #print(p)
    #print(s)
    #print()
    #print(p[0])
    #print(s[0])
    #print()
    #print(p[1])
    #print(s[1])
    #print()
    #print(p[2])
    #print(s[2])
    #print()
    #print(p[3])
    #print(s[3])
    #print()
    #print(p[4])
    #print(s[4])
    #print()
    #print()
    #print()
    #print()
    #print()
    #print()
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        if s[i] == 'AC':
            ac[int(p[i]) - 1] = 1
        else:
            if ac[int(p[i]) - 1] == 0:
                wa[int(p[i]) - 1] += 1
    #print(ac)
    #print(wa)
    #print()
    #print(ac[0])
    #print(wa[0])
    #print()
    #print(ac[1])
    #print(wa[1])
    #print()
    #print(ac[2])
    #print(wa[2])
    #print()
    #print(ac[3])
    #print(wa[3])
    #print()
    #print(ac[4])
    #print(wa[4])
    #print()
    #print()
    #print()
    #print()
    #print()
    #print()
    ac_cnt = 0
    wa_cnt = 0
    for i in range(n):
        if ac[i] == 1:
            ac_cnt += 1
            wa_cnt += wa[i]
    print(ac_cnt, wa_cnt)

if __name__ == '__main__':
    main()