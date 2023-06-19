Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans =

=======
Suggestion 2

def solve(D, G, P, C):
    ans = float('inf')
    for i in range(1 << D):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                s += P[j] * 100 * (j + 1) + C[j]
                cnt += P[j]
            else:
                rest_max = j
        if s < G:
            s1 = 100 * (rest_max + 1)
            need = (G - s + s1 - 1) // s1
            if need >= P[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    return ans

=======
Suggestion 3

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

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    D, G = map(int, input().split())
    PC = [list(map(int, input().split())) for _ in range(D)]
    ans = float('inf')
    for i in range(2**D):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                score += 100 * (j+1) * PC[j][0] + PC[j][1]
                cnt += PC[j][0]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= PC[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 6

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for _ in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    min_num = 1000000
    for i in range(2**D):
        score = 0
        num = 0
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j+1) * p[j] + c[j]
                num += p[j]
        if score >= G:
            min_num = min(min_num, num)
        else:
            for j in range(D-1, -1, -1):
                if (i >> j) & 1:
                    continue
                for k in range(p[j]):
                    if score >= G:
                        break
                    score += 100 * (j + 1)
                    num += 1
            min_num = min(min_num, num)
    print(min_num)

=======
Suggestion 7

def solve():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = float("inf")
    for i in range(1 << D):
        score = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                score += pc[j][0] * (j + 1) * 100 + pc[j][1]
                cnt += pc[j][0]
            else:
                rest_max = j
        if score < G:
            s1 = (rest_max + 1) * 100
            need = (G - score + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 8

def solve(d, g, p, c):
    ans = 100000000
    for i in range(2 ** d):
        s = 0
        num = 0
        rest_max = -1
        for j in range(d):
            if (i >> j) & 1:
                s += p[j] * (j + 1) * 100 + c[j]
                num += p[j]
            else:
                rest_max = j
        if s < g:
            s1 = (rest_max + 1) * 100
            need = (g - s + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    return ans

=======
Suggestion 9

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 10000000
    for i in range(2 ** D):
        score = 0
        num = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                score += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

=======
Suggestion 10

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = 10**9

    for i in range(2**D):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                score += 100*(j+1)*pc[j][0]+pc[j][1]
                cnt += pc[j][0]
            else:
                rest_max = j
        if score < G:
            s1 = 100*(rest_max+1)
            need = (G-score+s1-1)//s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)
