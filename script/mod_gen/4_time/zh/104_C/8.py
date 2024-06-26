def main():
    D,G = map(int,input().split())
    p = []
    c = []
    for i in range(D):
        p_tmp,c_tmp = map(int,input().split())
        p.append(p_tmp)
        c.append(c_tmp)
    ans = 1000000000
    for i in range(2**D):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                score += 100 * (j+1) * p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans,cnt)
    print(ans)

if __name__ == '__main__':
    main()