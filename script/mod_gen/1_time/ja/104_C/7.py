def main():
    # input
    D, G = map(int, input().split())
    p, c = [], []
    for _ in range(D):
        p_, c_ = map(int, input().split())
        p.append(p_)
        c.append(c_)
    # compute
    min_num = 10**9
    for i in range(2**D):
        score = 0
        num = 0
        for j in range(D):
            if (i>>j)&1:
                score += 100*(j+1)*p[j] + c[j]
                num += p[j]
        if score < G:
            for j in range(1, p[D-1]+1):
                if score >= G:
                    break
                score += 100*(D-1)
                num += 1
        if score >= G:
            min_num = min(min_num, num)
    # output
    print(min_num)

if __name__ == '__main__':
    main()