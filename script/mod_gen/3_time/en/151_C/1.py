def main():
    N, M = map(int, input().split())
    p = [0] * M
    S = [0] * M
    for i in range(M):
        p[i], S[i] = input().split()
        p[i] = int(p[i])
    ans = 0
    penalty = 0
    ac = [0] * (N + 1)
    wa = [0] * (N + 1)
    for i in range(M):
        if ac[p[i]] == 1:
            continue
        if S[i] == "AC":
            ac[p[i]] = 1
            ans += 1
            penalty += wa[p[i]]
        else:
            wa[p[i]] += 1
    print(ans, penalty)

if __name__ == '__main__':
    main()