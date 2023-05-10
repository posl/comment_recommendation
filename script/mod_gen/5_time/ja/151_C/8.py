def main():
    N, M = map(int, input().split())
    p = [0] * N
    s = [0] * N
    for i in range(M):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    ac = [0] * N
    wa = [0] * N
    for i in range(M):
        if s[i] == "AC":
            ac[p[i] - 1] = 1
        elif s[i] == "WA" and ac[p[i] - 1] == 0:
            wa[p[i] - 1] += 1
    ac_cnt = 0
    wa_cnt = 0
    for i in range(N):
        if ac[i] == 1:
            ac_cnt += 1
            wa_cnt += wa[i]
    print(ac_cnt, wa_cnt)

if __name__ == '__main__':
    main()