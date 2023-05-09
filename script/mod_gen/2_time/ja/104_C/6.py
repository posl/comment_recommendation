def solve():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)
    ans = 10**10
    for i in range(1<<D):
        #print(i)
        score = 0
        num = 0
        rest_max = -1
        for j in range(D):
            if (i>>j)&1:
                score += 100*(j+1)*p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100*(rest_max+1)
            need = (G-score+s1-1)//s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)
solve()

if __name__ == '__main__':
    solve()