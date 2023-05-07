def main():
    #入力
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    #print(D, G, p, c)
    #解く問題数の最小値を求める
    ans = 1000000
    for bit in range(1 << D):
        sum = 0
        cnt = 0
        max = 0
        for i in range(D):
            if bit & (1 << i):
                sum += (i + 1) * 100 * p[i] + c[i]
                cnt += p[i]
            else:
                max = i
        if sum < G:
            for j in range(p[max]):
                sum += (max + 1) * 100
                cnt += 1
                if sum >= G:
                    break
        if sum >= G:
            ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()