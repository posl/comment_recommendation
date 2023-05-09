def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = 10**9
    for i in range(2**D):
        tmp = 0
        cnt = 0
        for j in range(D):
            if (i >> j) & 1:
                tmp += 100 * (j + 1) * pc[j][0] + pc[j][1]
                cnt += pc[j][0]
        if tmp >= G:
            ans = min(ans, cnt)
            continue
        for j in range(D - 1, -1, -1):
            if (i >> j) & 1:
                continue
            for k in range(pc[j][0] - 1):
                tmp += 100 * (j + 1)
                cnt += 1
                if tmp >= G:
                    ans = min(ans, cnt)
        if ans == 10**9:
            ans = cnt
    print(ans)

if __name__ == '__main__':
    main()