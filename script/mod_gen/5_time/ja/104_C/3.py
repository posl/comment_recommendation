def main():
    n, g = map(int, input().split())
    p = [0]
    c = [0]
    for i in range(n):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)
    ans = 10**10
    for i in range(2**n):
        point = 0
        count = 0
        rest_max = -1
        for j in range(n):
            if (i >> j) & 1:
                point += p[j + 1] * 100 * (j + 1) + c[j + 1]
                count += p[j + 1]
            else:
                rest_max = j + 1
        if point < g:
            s1 = (g - point + 100 * rest_max - 1) // (100 * rest_max)
            if s1 < p[rest_max]:
                count += s1
            else:
                continue
        ans = min(ans, count)
    print(ans)
main()

if __name__ == '__main__':
    main()