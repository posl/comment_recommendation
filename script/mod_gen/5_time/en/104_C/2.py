def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 1000000000
    for i in range(2**D):
        tmp = 0
        cnt = 0
        for j in range(D):
            if i >> j & 1:
                tmp += c[j] + p[j] * 100 * (j + 1)
                cnt += p[j]
        if tmp >= G:
            ans = min(ans, cnt)
        else:
            for j in range(D - 1, -1, -1):
                if i >> j & 1:
                    continue
                for k in range(p[j]):
                    if tmp >= G:
                        ans = min(ans, cnt)
                        break
                    tmp += 100 * (j + 1)
                    cnt += 1
    print(ans)

if __name__ == '__main__':
    main()