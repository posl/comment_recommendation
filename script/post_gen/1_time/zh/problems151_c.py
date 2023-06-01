Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        p_i, s_i = input().split()
        p_i = int(p_i)
        if s_i == "AC":
            if p[p_i - 1] != -1:
                s[p_i - 1] = 1
                p[p_i - 1] = -1
        elif s_i == "WA":
            if p[p_i - 1] != -1:
                s[p_i - 1] += 1
    print(sum(s), sum([s[i] for i in range(n) if p[i] == -1]))

=======
Suggestion 2

def solution():
    n,m = map(int, input().split())
    problem = [0]*n
    ac = 0
    wa = 0
    for i in range(m):
        p,s = input().split()
        p = int(p)
        if problem[p-1] == 0 and s == "AC":
            problem[p-1] = 1
            ac += 1
        elif s == "WA" and problem[p-1] == 0:
            wa += 1
    print(ac,wa)

solution()

=======
Suggestion 3

def main():
    # 读入数据
    N, M = map(int, input().split())
    # print(N, M)
    # 读入数据
    p = []
    s = []
    for i in range(M):
        p_i, s_i = input().split()
        p.append(int(p_i))
        s.append(s_i)
    # print(p)
    # print(s)
    # 处理数据
    # 1.正确答案的数量
    # 2.被罚的数量
    # 3.在该问题上第一次收到AC之前收到的WA的数量
    # 4.在该问题上第一次收到AC之前收到的WA的数量
    # 5.在该问题上第一次收到AC之前收到的WA的数量
    # 6.在该问题上第一次收到AC之前收到的WA的数量
    # 7.在该问题上第一次收到AC之前收到的WA的数量
    # 8.在该问题上第一次收到AC之前收到的WA的数量
    # 9.在该问题上第一次收到AC之前收到的WA的数量
    # 10.在该问题上第一次收到AC之前收到的WA的数量
    # 11.在该问题上第一次收到AC之前收到的WA的数量
    # 12.在该问题上第一次收到AC之前收到的WA的数量
    # 13.在该问题上第一次收到AC之前收到的WA的数量
    # 14.在该问题上第一次收到AC之前收到的WA的数量
    # 15.在该问题上第一次收到AC之前收到的WA的数量
    # 16.在该问题上第一次收到AC之前收到的WA的数量
    # 17.在该问题上第一次收到AC之前收到的WA的数量
    # 18.在该问题上第一次收到AC之前收到的WA的数量

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    p = []
    s = []
    for i in range(M):
        pi, si = input().split()
        p.append(int(pi))
        s.append(si)

    ac = 0
    wa = 0
    ac_flag = [False] * N
    wa_flag = [0] * N

    for i in range(M):
        if ac_flag[p[i] - 1] == False:
            if s[i] == "AC":
                ac_flag[p[i] - 1] = True
                ac += 1
                wa += wa_flag[p[i] - 1]
            else:
                wa_flag[p[i] - 1] += 1

    print(ac, wa)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    p = [0]*n
    s = [0]*n
    for i in range(m):
        pi,si = input().split()
        pi = int(pi)
        if si == 'AC':
            if p[pi-1] == 0:
                p[pi-1] = 1
        else:
            if p[pi-1] == 0:
                s[pi-1] += 1
    print(sum(p),sum([p[i]*s[i] for i in range(n)]))

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    p = [0 for i in range(n)]
    s = ["" for i in range(n)]
    for i in range(m):
        p[i],s[i] = input().split()
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == "AC":
            ac += 1
        else:
            wa += 1
    print(ac,wa)

=======
Suggestion 7

def main():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    p = []
    s = []
    for i in range(m):
        ps = input().split()
        p.append(int(ps[0]))
        s.append(ps[1])
    ac = 0
    wa = 0
    for i in range(m):
        if s[i] == "AC":
            ac += 1
        elif s[i] == "WA":
            wa += 1
    print(ac, wa)

=======
Suggestion 8

def solve(n, m, p, s):
    ac = 0
    wa = 0
    acs = [0] * n
    was = [0] * n
    for i in range(m):
        if s[i] == "AC":
            if acs[p[i]-1] == 0:
                ac += 1
                acs[p[i]-1] = 1
                wa += was[p[i]-1]
        else:
            if acs[p[i]-1] == 0:
                was[p[i]-1] += 1
    return ac, wa

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        p1,s1 = map(str,input().split())
        p.append(p1)
        s.append(s1)
    print(p)
    print(s)
    #print(p[0])
    #print(s[0])
    #print(p[0],s[0])
    #print(p[1],s[1])
    #print(p[2],s[2])
    #print(p[3],s[3])
    #print(p[4],s[4])
    #print(p[5],s[5])
    #print(p[6],s[6])
    #print(p[7],s[7])
    #print(p[8],s[8])
    #print(p[9],s[9])
    #print(p[10],s[10])
    #print(p[11],s[11])
    #print(p[12],s[12])
    #print(p[13],s[13])
    #print(p[14],s[14])
    #print(p[15],s[15])
    #print(p[16],s[16])
    #print(p[17],s[17])
    #print(p[18],s[18])
    #print(p[19],s[19])
    #print(p[20],s[20])
    #print(p[21],s[21])
    #print(p[22],s[22])
    #print(p[23],s[23])
    #print(p[24],s[24])
    #print(p[25],s[25])
    #print(p[26],s[26])
    #print(p[27],s[27])
    #print(p[28],s[28])
    #print(p[29],s[29])
    #print(p[30],s[30])
    #print(p[31],s[31])
    #print(p[32],s[32])
    #print(p[33],s[33])
    #print(p[34],s[34])
    #print(p[35],s[35])
    #print(p[36],s[36])
    #print(p[37],s[37])
    #print(p[38],s[

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    p = [0] * M
    s = [0] * M
    for i in range(M):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    ac = [0] * N
    wa = [0] * N
    for i in range(M):
        if s[i] == 'AC':
            ac[p[i]-1] = 1
        elif ac[p[i]-1] == 0:
            wa[p[i]-1] += 1
    print(sum(ac), sum([ac[i]*wa[i] for i in range(N)]))
