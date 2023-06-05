def main():
    # 读入数据
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    # 枚举解决问题的组合
    ans = float('inf')
    for i in range(1 << D):
        score = 0
        solved = 0
        rest_max = -1
        for j in range(D):
            if i >> j & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                solved += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            solved += need
        ans = min(ans, solved)
    print(ans)

if __name__ == '__main__':
    main()