def main():
    print("请输入问题数，目标分数，每个问题的分数，每个问题的奖金")
    d,g = map(int,input().split())
    p = []
    c = []
    for i in range(d):
        a,b = map(int,input().split())
        p.append(a)
        c.append(b)
    ans = 100000
    for i in range(2**d):
        s = 0
        num = 0
        rest_max = -1
        for j in range(d):
            if ((i >> j) & 1):
                s += p[j] * (j+1) * 100 + c[j]
                num += p[j]
            else:
                rest_max = j
        if s < g:
            s1 = (rest_max + 1) * 100
            need = (g - s + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans,num)
    print(ans)

if __name__ == '__main__':
    main()