def main():
    # 读取输入
    d, g = map(int, input().split())
    p = []
    c = []
    for _ in range(d):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    # 逐个尝试
    ans = float('inf')
    for i in range(2 ** d):
        # 记录当前尝试的结果
        solved = 0
        score = 0
        rest_max = -1
        for j in range(d):
            if ((i >> j) & 1):
                # 完成第 j 题目
                solved += p[j]
                score += 100 * (j + 1) * p[j] + c[j]
            else:
                rest_max = j
        if score < g:
            # 尝试完所有题目，但得分不够，需要补题
            s1 = 100 * (rest_max + 1) # 补题的最低得分
            need = (g - score + s1 - 1) // s1 # 需要补题的数目
            if need >= p[rest_max]:
                # 题目数目不够
                continue
            solved += need
            score += s1 * need
        ans = min(ans, solved)
    print(ans)
