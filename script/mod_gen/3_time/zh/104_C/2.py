def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for bit in range(1 << D):
        s = 0
        num = 0
        rest_max = -1
        for i in range(D):
            if bit & (1 << i):
                s += 100 * (i + 1) * p[i] + c[i]
                num += p[i]
            else:
                rest_max = i
        if s < G:
            s1 = 100 * (rest_max + 1)
            need = (G - s + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

if __name__ == '__main__':
    main()