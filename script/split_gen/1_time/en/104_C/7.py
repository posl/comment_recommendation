def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = 10**9
    for i in range(2**D):
        cnt = 0
        tmp = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                cnt += pc[j][0]
                tmp += 100 * (j + 1) * pc[j][0] + pc[j][1]
            else:
                rest_max = j
        if tmp < G:
            s1 = 100 * (rest_max + 1)
            need = (G - tmp + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)
