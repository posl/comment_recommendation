def main():
    N, M = map(int, input().split())
    p = [0] * N
    s = [0] * N
    for i in range(M):
        p_i, s_i = input().split()
        p_i = int(p_i)
        p[p_i - 1] += 1
        if s_i == 'AC':
            s[p_i - 1] = 1
        else:
            if s[p_i - 1] != 1:
                s[p_i - 1] = 2
    ac = 0
    wa = 0
    for i in range(N):
        if s[i] == 1:
            ac += 1
            wa += p[i] - 1
        elif s[i] == 2:
            wa += p[i]
    print(ac, wa)

if __name__ == '__main__':
    main()