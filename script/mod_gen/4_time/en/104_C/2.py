def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for i in range(1, 1 << D):
        tmp = 0
        cnt = 0
        for j in range(D):
            if i & (1 << j):
                tmp += (j + 1) * 100 * p[j] + c[j]
                cnt += p[j]
        if tmp < G:
            for j in range(D - 1, -1, -1):
                if not i & (1 << j):
                    for k in range(p[j]):
                        if tmp >= G:
                            break
                        tmp += (j + 1) * 100
                        cnt += 1
                    break
        if tmp >= G:
            ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()