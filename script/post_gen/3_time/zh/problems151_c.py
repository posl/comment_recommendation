Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    input_line = input().split()
    return input_line

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    p = []
    s = []
    for i in range(M):
        pi, si = input().split()
        p.append(int(pi))
        s.append(si)
    #print(p)
    #print(s)
    ac = 0
    wa = 0
    ac_list = [0]*N
    wa_list = [0]*N
    for i in range(M):
        if s[i] == 'AC':
            if ac_list[p[i]-1] == 0:
                ac_list[p[i]-1] = 1
                ac += 1
                wa += wa_list[p[i]-1]
        else:
            if ac_list[p[i]-1] == 0:
                wa_list[p[i]-1] += 1
    print(ac, wa)

=======
Suggestion 3

def problems151_c():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        p_i,s_i = input().split()
        p.append(p_i)
        s.append(s_i)

    print(p)
    print(s)

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    p = [0]*n
    s = ['']*n
    for i in range(m):
        p[i],s[i] = input().split()
        p[i] = int(p[i])
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == 'AC':
            if p[i] == 1:
                ac += 1
            else:
                if p[i] in p[:i]:
                    continue
                else:
                    ac += 1
                    wa += p[:i].count(p[i])
        else:
            if p[i] == 1:
                wa += 1
            else:
                if p[i] in p[:i]:
                    continue
                else:
                    wa += p[:i].count(p[i])
    print(ac,wa)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if s == "AC":
            ac[p] = 1
        else:
            if ac[p] == 0:
                wa[p] += 1
    print(sum(ac), sum([ac[i] * wa[i] for i in range(n)]))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    p = []
    s = []
    for i in range(M):
        p_i, s_i = input().split()
        p.append(int(p_i))
        s.append(s_i)
    print(p)
    print(s)

    ac = 0
    wa = 0
    for i in range(M):
        if s[i] == 'AC':
            ac += 1
        elif s[i] == 'WA':
            wa += 1
    print(ac, wa)
    return

=======
Suggestion 7

def main():
    #输入
    n,m = map(int,input().split())
    #初始值
    p = [0]*n
    s = [0]*n
    #输入
    for i in range(m):
        p[i],s[i] = map(str,input().split())
        p[i] = int(p[i])
    #初始值
    ans = 0
    pen = 0
    #循环
    for i in range(n):
        #如果答案正确
        if s[i] == "AC":
            #答案正确的问题数+1
            ans += 1
            #罚时加上该问题的罚时
            pen += p[i]
        #如果答案错误
        else:
            #并且该问题的答案已经错误过一次
            if p[i] in p[:i]:
                #罚时加上20
                pen += 20
    #输出
    print(ans,pen)

=======
Suggestion 8

def problems151_c():
    N, M = map(int, input().split())
    ACs = [0] * N
    WAs = [0] * N
    for i in range(M):
        p, S = input().split()
        p = int(p)
        if S == 'AC':
            ACs[p-1] = 1
        else:
            if ACs[p-1] == 0:
                WAs[p-1] += 1
    print(sum(ACs), sum([ACs[i] * WAs[i] for i in range(N)]))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    p = []
    S = []
    for i in range(M):
        p_i, S_i = input().split()
        p.append(int(p_i))
        S.append(S_i)

    # print(p)
    # print(S)
    # print(p[0])
    # print(S[0])

    # 正解数
    correct_number = 0
    # 罚分数
    penalty_number = 0

    # 按照问题的序号进行筛选
    for i in range(N):
        # 第i个问题的序号
        i = i + 1
        # print('i = ', i)
        # 按照问题的序号进行筛选
        for j in range(M):
            # print('j = ', j)
            # print('p[j] = ', p[j])
            # print('i = ', i)
            if p[j] == i:
                # print('p[j] = ', p[j])
                # print('i = ', i)
                # print('S[j] = ', S[j])
                if S[j] == 'AC':
                    correct_number = correct_number + 1
                    # print('correct_number = ', correct_number)
                    break
                elif S[j] == 'WA':
                    penalty_number = penalty_number + 1
                    # print('penalty_number = ', penalty_number)

    print(correct_number, penalty_number)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    p = [0 for i in range(n)]
    s = ["" for i in range(n)]
    for i in range(m):
        x, y = map(str, input().split())
        p[int(x) - 1] += 1
        s[int(x) - 1] = y
    ac = 0
    wa = 0
    for i in range(n):
        if s[i] == "AC":
            ac += 1
            wa += p[i]
        else:
            p[i] = 0
    print(ac, wa)
