def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        tmp = list(map(int, input().split()))
        p.append(tmp[0])
        c.append(tmp[1])
    ans = 100000
    for i in range(2**D):
        tmp = 0
        cnt = 0
        for j in range(D):
            if (i >> j) & 1:
                tmp += 100*(j+1)*p[j] + c[j]
                cnt += p[j]
        if tmp >= G:
            ans = min(ans, cnt)
            continue
        for j in range(D-1, -1, -1):
            if (i >> j) & 1:
                continue
            for k in range(p[j]):
                if tmp >= G:
                    break
                tmp += 100*(j+1)
                cnt += 1
            if tmp >= G:
                ans = min(ans, cnt)
                break
    print(ans)

if __name__ == '__main__':
    main()