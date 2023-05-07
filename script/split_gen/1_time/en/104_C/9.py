def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = 1000000000000000000
    for i in range(2**D):
        sum = 0
        num = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                sum += pc[j][0] * (j+1) * 100 + pc[j][1]
                num += pc[j][0]
            else:
                rest_max = j
        if sum < G:
            s1 = (rest_max + 1) * 100
            need = (G - sum + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)
