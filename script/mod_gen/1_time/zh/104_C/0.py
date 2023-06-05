def solve():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = float('inf')
    for i in range(1 << D):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if i >> j & 1:
                s += 100 * (j + 1) * pc[j][0] + pc[j][1]
                cnt += pc[j][0]
            else:
                rest_max = j
        if s < G:
            s1 = 100 * (rest_max + 1)
            need = (G - s + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    solve()