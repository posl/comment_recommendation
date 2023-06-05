def main():
    N, M = map(int, input().split())
    p = []
    s = []
    for i in range(M):
        pi, si = input().split()
        p.append(int(pi))
        s.append(si)
    ac = 0
    wa = 0
    ac_flag = [False] * N
    wa_flag = [0] * N
    for i in range(M):
        if ac_flag[p[i] - 1] == False:
            if s[i] == "AC":
                ac_flag[p[i] - 1] = True
                ac += 1
                wa += wa_flag[p[i] - 1]
            else:
                wa_flag[p[i] - 1] += 1
    print(ac, wa)

if __name__ == '__main__':
    main()