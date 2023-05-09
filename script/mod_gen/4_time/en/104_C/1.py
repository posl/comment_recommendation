def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10 ** 10
    for i in range(2 ** D):
        sum = 0
        num = 0
        for j in range(D):
            if i >> j & 1:
                sum += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        if sum < G:
            for j in range(D - 1, -1, -1):
                if not i >> j & 1:
                    for k in range(p[j]):
                        sum += 100 * (j + 1)
                        num += 1
                        if sum >= G:
                            ans = min(ans, num)
                            break
                    break
        else:
            ans = min(ans, num)
    print(ans)

if __name__ == '__main__':
    main()