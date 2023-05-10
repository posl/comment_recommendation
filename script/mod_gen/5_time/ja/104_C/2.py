def main():
    # D, G = map(int, input().split())
    # p, c = zip(*[map(int, input().split()) for _ in range(D)])
    # ans = 10 ** 9
    # for i in range(1 << D):
    #     s = 0
    #     cnt = 0
    #     rest_max = -1
    #     for j in range(D):
    #         if (i >> j) & 1:
    #             s += 100 * (j + 1) * p[j] + c[j]
    #             cnt += p[j]
    #         else:
    #             rest_max = j
    #     if s < G:
    #         s1 = 100 * (rest_max + 1)
    #         need = (G - s + s1 - 1) // s1
    #         if need >= p[rest_max]:
    #             continue
    #         cnt += need
    #     ans = min(ans, cnt)
    # print(ans)
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)
    ans = 10 ** 9
    for i in range(1 << D):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                s += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if s < G:
            s1 = 100 * (rest_max + 1)
            need = (G - s + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()