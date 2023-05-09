def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 10**9
    for i in range(1<<D):
        score = 0
        num = 0
        for j in range(D):
            if (i>>j) & 1:
                score += 100*(j+1)*p[j] + c[j]
                num += p[j]
        if score >= G:
            ans = min(ans, num)
        else:
            for j in range(D-1, -1, -1):
                if (i>>j) & 1:
                    continue
                for k in range(p[j]):
                    score += 100*(j+1)
                    num += 1
                    if score >= G:
                        ans = min(ans, num)
                        break
                break
    print(ans)

if __name__ == '__main__':
    main()