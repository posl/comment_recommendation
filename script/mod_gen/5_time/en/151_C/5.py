def main():
    N, M = map(int, input().split())
    p = [0] * N
    s = [''] * N
    for i in range(M):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    ac = [0] * N
    wa = [0] * N
    for i in range(M):
        if s[i] == 'AC':
            ac[p[i]-1] = 1
        else:
            if ac[p[i]-1] == 0:
                wa[p[i]-1] += 1
    ac_count = 0
    wa_count = 0
    for i in range(N):
        if ac[i] == 1:
            ac_count += 1
            wa_count += wa[i]
    print(ac_count, wa_count)

if __name__ == '__main__':
    main()