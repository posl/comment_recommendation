def main():
    d,g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)
    
    ans = 10000000000
    for i in range(2**d):
        score = 0
        num = 0
        for j in range(d):
            if (i >> j) & 1:
                score += p[j] * 100 * (j+1) + c[j]
                num += p[j]
        if score >= g:
            ans = min(ans, num)
            continue
        for j in range(d-1, -1, -1):
            if (i >> j) & 1:
                continue
            for k in range(p[j]):
                if score >= g:
                    break
                score += 100 * (j+1)
                num += 1
        ans = min(ans, num)
    print(ans)

if __name__ == '__main__':
    main()