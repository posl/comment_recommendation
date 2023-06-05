def main():
    # 读取输入
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    # 问题数目最大值
    ans = 1000
    # 全部解决
    for i in range(2 ** D):
        # 问题数目
        num = 0
        # 得分
        score = 0
        # 未解决的最高分
        rest_max = -1
        for j in range(D):
            # 解决了该问题
            if (i >> j) & 1:
                # 问题数目
                num += p[j]
                # 得分
                score += 100 * (j + 1) * p[j] + c[j]
            else:
                # 未解决的最高分
                rest_max = j
        # 如果得分不够
        if score < G:
            # 还需要的问题数目
            solve = (G - score + 100 * (rest_max + 1) - 1) // (100 * (rest_max + 1))
            # 问题数目最小值
            if solve < p[rest_max]:
                num += solve
    # 更新答案
    ans = min(ans, num)
    print(ans)

if __name__ == '__main__':
    main()