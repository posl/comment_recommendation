def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 1000000000
    for i in range(2 ** D):
        sum = 0
        num = 0
        max_num = 0
        for j in range(D):
            if (i >> j) & 1:
                sum += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
            else:
                max_num = j
        if sum < G:
            k = G - sum
            if k > 100 * (max_num + 1) * p[max_num]:
                continue
            else:
                num += -(-k // (100 * (max_num + 1)))
        ans = min(ans, num)
    print(ans)
