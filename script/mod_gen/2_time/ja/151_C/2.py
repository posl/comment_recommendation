def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        p_s = input().split()
        p.append(int(p_s[0]))
        s.append(p_s[1])
    ac = 0
    wa = 0
    ac_list = []
    for i in range(m):
        if s[i] == "AC":
            ac += 1
            if p[i] not in ac_list:
                ac_list.append(p[i])
                wa += ac_list.count(p[i])
        else:
            if p[i] not in ac_list:
                wa += 1
    print(ac, wa)

if __name__ == '__main__':
    main()