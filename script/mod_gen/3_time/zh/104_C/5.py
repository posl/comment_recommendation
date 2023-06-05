def main():
    d, g = map(int, input().split())
    pc = [tuple(map(int, input().split())) for _ in range(d)]
    ans = 10 ** 9
    for i in range(2 ** d):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(d):
            if (i >> j) & 1:
                s += 100 * (j + 1) * pc[j][0] + pc[j][1]
                cnt += pc[j][0]
            else:
                rest_max = j
        if s < g:
            s1 = 100 * (rest_max + 1)
            need = (g - s + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()