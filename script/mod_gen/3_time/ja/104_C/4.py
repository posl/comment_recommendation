def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    min_num = 1000
    for i in range(2**D):
        num = 0
        score = 0
        for j in range(D):
            if ((i>>j)&1):
                score += (j+1)*100*p[j] + c[j]
                num += p[j]
        if score >= G:
            min_num = min(min_num, num)
        else:
            for j in range(D-1, -1, -1):
                if ((i>>j)&1):
                    continue
                for k in range(p[j]):
                    score += (j+1)*100
                    num += 1
                    if score >= G:
                        min_num = min(min_num, num)
                        break
                break
    print(min_num)

if __name__ == '__main__':
    main()