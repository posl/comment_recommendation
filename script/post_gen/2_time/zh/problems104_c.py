Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    D, G = map(int, input().split())
    P = []
    C = []
    for i in range(D):
        p, c = map(int, input().split())
        P.append(p)
        C.append(c)

    min_count =

=======
Suggestion 2

def solve():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)
    ans =

=======
Suggestion 3

def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)

    ans =

=======
Suggestion 4

def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        p_temp, c_temp = map(int, input().split())
        p.append(p_temp)
        c.append(c_temp)

    min_count =

=======
Suggestion 5

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)

    min_cnt = float('inf')

    for i in range(2**D):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if (i>>j) & 1:
                score += 100*(j+1)*p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j

        if score < G:
            s1 = 100*(rest_max+1)
            need = (G-score+s1-1)//s1
            if need >= p[rest_max]:
                continue
            cnt += need
        min_cnt = min(min_cnt, cnt)
    print(min_cnt)

=======
Suggestion 6

def main():
    D,G = map(int,input().split())
    p_c = [list(map(int,input().split())) for _ in range(D)]
    ans = float('inf')
    for i in range(2**D):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i>>j)&1):
                score += 100*(j+1)*p_c[j][0]+p_c[j][1]
                cnt += p_c[j][0]
            else:
                rest_max = j
        if score < G:
            s1 = 100*(rest_max+1)
            need = (G-score+s1-1)//s1
            if need >= p_c[rest_max][0]:
                continue
            cnt += need
        ans = min(ans,cnt)
    print(ans)

=======
Suggestion 7

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 10000
    for i in range(2**D):
        score = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
    D, G = map(int,input().split())
    p = []
    c = []
    for i in range(D):
        pi, ci = map(int,input().split())
        p.append(pi)
        c.append(ci)
    ans = 100000000000000000000
    for i in range(2**D):
        count = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                score += 100 * (j+1) * p[j] + c[j]
                count += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max+1)
            need = (G - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            count += need
        ans = min(ans,count)
    print(ans)

=======
Suggestion 9

def get_problem_num(problem_list, score, bonus):
    if score >= bonus:
        return 0
    else:
        return 1

=======
Suggestion 10

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
