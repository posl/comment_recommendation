def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10 ** 9
    for i in range(2 ** D):
        s = 0
        cnt = 0
        for j in range(D):
            if ((i >> j) & 1):
                s += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
        if s >= G:
            ans = min(ans, cnt)
            continue
        for j in range(D - 1, -1, -1):
            if ((i >> j) & 1):
                continue
            for k in range(p[j]):
                if s >= G:
                    break
                s += 100 * (j + 1)
                cnt += 1
            if s >= G:
                break
        if s >= G:
            ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()