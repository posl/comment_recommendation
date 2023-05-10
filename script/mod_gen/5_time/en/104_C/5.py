def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = float('inf')
    for i in range(2**d):
        s = 0
        num = 0
        rest_max = -1
        for j in range(d):
            if (i >> j) & 1:
                s += 100*(j+1)*p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if s < g:
            s1 = 100*(rest_max+1)
            need = (g-s+s1-1)//s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

if __name__ == '__main__':
    main()