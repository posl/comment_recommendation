def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    min_num = 1000000
    for i in range(2**D):
        num = 0
        score = 0
        for j in range(D):
            if i & (1<<j):
                num += p[j]
                score += 100*(j+1)*p[j] + c[j]
        if score >= G:
            min_num = min(min_num, num)
        else:
            for j in range(D-1, -1, -1):
                if i & (1<<j):
                    continue
                for k in range(p[j]):
                    if score >= G:
                        break
                    num += 1
                    score += 100*(j+1)
            min_num = min(min_num, num)
    print(min_num)

if __name__ == '__main__':
    main()