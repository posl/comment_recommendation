def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        p1, c1 = map(int, input().split())
        p.append(p1)
        c.append(c1)
    ans = float("inf")
    for i in range(2**d):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(d):
            if ((i>>j) & 1):
                score += 100*(j+1)*p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if score < g:
            s1 = 100*(rest_max+1)
            need = (g - score + s1 - 1)//s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()