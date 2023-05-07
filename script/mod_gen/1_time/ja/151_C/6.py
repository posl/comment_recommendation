def main():
    N, M = map(int, input().split())
    p = [0] * (N + 1)
    s = [0] * (N + 1)
    for i in range(M):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    ac = [0] * (N + 1)
    wa = [0] * (N + 1)
    for i in range(M):
        if s[i] == 'AC':
            ac[p[i]] = 1
        else:
            if ac[p[i]] == 0:
                wa[p[i]] += 1
    ans = 0
    penalty = 0
    for i in range(1, N + 1):
        if ac[i] == 1:
            ans += 1
            penalty += wa[i]
    print(ans, penalty)

if __name__ == '__main__':
    main()