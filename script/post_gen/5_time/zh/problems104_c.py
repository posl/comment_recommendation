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

    min_num =

=======
Suggestion 2

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = float('inf')
    for bits in range(1<<D):
        score = 0
        cnt = 0
        rest_max = -1
        for i in range(D):
            if bits & (1<<i):
                score += 100*(i+1)*pc[i][0] + pc[i][1]
                cnt += pc[i][0]
            else:
                rest_max = i
        if score < G:
            s1 = 100*(rest_max+1)
            need = (G-score+s1-1)//s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    # 输入
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]

    # 计算
    ans = float('inf')
    for i in range(1 << D):
        score = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                score += pc[j][0] * 100 * (j + 1) + pc[j][1]
                cnt += pc[j][0]
            else:
                rest_max = j

        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)

    # 输出
    print(ans)

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]

    min_num = 10000
    for i in range(2**D):
        num = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                score += 100 * (j+1) * pc[j][0] + pc[j][1]
                num += pc[j][0]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            num += need
        min_num = min(min_num, num)
    print(min_num)

=======
Suggestion 6

def main():
    D,G = map(int,input().split())
    pc = [list(map(int,input().split())) for i in range(D)]
    #print(pc)
    #print(D,G)
    #print(pc[0][0],pc[0][1])
    #print(pc[1][0],pc[1][1])
    #print(pc[2][0],pc[2][1])
    #print(pc[3][0],pc[3][1])

    #print(pc[0][0]*100,pc[0][1])
    #print(pc[1][0]*100,pc[1][1])
    #print(pc[2][0]*100,pc[2][1])
    #print(pc[3][0]*100,pc[3][1])

    #print(pc[0][0]*100*(pc[0][0]+1)/2+pc[0][1])
    #print(pc[1][0]*100*(pc[1][0]+1)/2+pc[1][1])
    #print(pc[2][0]*100*(pc[2][0]+1)/2+pc[2][1])
    #print(pc[3][0]*100*(pc[3][0]+1)/2+pc[3][1])

    #print(pc[0][0]*100*(pc[0][0]+1)/2+pc[0][1])
    #print(pc[1][0]*100*(pc[1][0]+1)/2+pc[1][1])
    #print(pc[2][0]*100*(pc[2][0]+1)/2+pc[2][1])
    #print(pc[3][0]*100*(pc[3][0]+1)/2+pc[3][1])

    #print(pc[0][0]*100*(pc[0][0]+1)/2+pc[0][1])
    #print(pc[1][0]*100*(pc[1][0]+1)/2+pc[1][1])
    #print(pc[2][0]*100*(pc[2][0]+1)/2+pc[2][1])
    #print(pc[3][0]*100*(pc[3][0]+1)/2+pc[3][1])

    #print(pc[0][0

=======
Suggestion 7

def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 1000000000
    for i in range(2**d):
        tmp = 0
        num = 0
        rest_max = -1
        for j in range(d):
            if ((i >> j) & 1):
                tmp += (j + 1) * 100 * p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if tmp < g:
            s1 = 100 * (rest_max + 1)
            need = (g - tmp + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

=======
Suggestion 8

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)

    # print(D, G)
    # print(p)
    # print(c)

    # 1. 穷举所有的问题解决方案
    # 2. 对每个方案，计算总分
    # 3. 对每个方案，计算解决问题的最小数目
    # 4. 对每个方案，找到最小的解决问题的数目

    # 1. 穷举所有的问题解决方案
    # 1.1 穷举所有的问题解决方案，对于每个问题，有解决和不解决两种方案
    # 1.2 穷举所有的问题解决方案，对于每个问题，有解决和不解决两种方案，对于所有的问题，有2^D种方案
    # 1.3 穷举所有的问题解决方案，对于每个问题，有解决和不解决两种方案，对于所有的问题，有2^D种方案，对于所有的方案，有2^D种方案
    # 1.4 穷举所有的问题解决方案，对于每个问题，有解决和不解决两种方案，对于所有的问题，有2^D种方案，对于所有的方案，有2^D种方案，对于所有的方案，有2^D种方案

    # 1.4 穷举所有的问题解决方案，对于每个问题，有解决和不解决两种方案，对于所有的问题，有2^D种方案，对于所有的方案，有2^D种方案，对于所有的方案，有2^D种方案

=======
Suggestion 9

def problems104_c():
    d, g = map(int, input().split())
    p = [0] * d
    c = [0] * d
    for i in range(d):
        p[i], c[i] = map(int, input().split())

    ans = 10 ** 9
    for i in range(2 ** d):
        s = 0
        num = 0
        rest_max = -1
        for j in range(d):
            if (i >> j) & 1:
                s += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
            else:
                rest_max = j

        if s < g:
            s1 = 100 * (rest_max + 1)
            need = (g - s + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)

    print(ans)

=======
Suggestion 10

def main():
    #输入数据
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    #初始化
    ans = float('inf')
    #枚举所有解决问题的方法
    for i in range(2**D):
        #记录解决问题的总数
        num = 0
        #记录解决问题的总分
        score = 0
        #记录最后一题
        last = -1
        for j in range(D):
            #如果解决了第j题
            if (i>>j)&1:
                #记录解决问题的总数
                num += pc[j][0]
                #记录解决问题的总分
                score += pc[j][0]*(j+1)*100 + pc[j][1]
            #否则
            else:
                #记录最后一题
                last = j
        #如果解决问题的总分不够
        if score < G:
            #需要解决的最后一题
            s = 100*(last+1)
            #需要解决的问题数
            need = (G-score+s-1)//s
            #如果需要解决的问题数超过了这道题的数量
            if need >= pc[last][0]:
                continue
            #更新解决问题的总数
            num += need
        #更新解决问题的总数
        ans = min(ans, num)
    #输出结果
    print(ans)
