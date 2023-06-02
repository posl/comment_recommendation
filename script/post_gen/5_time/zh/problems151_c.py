Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        a,b = input().split()
        p.append(int(a))
        s.append(b)
    ac = 0
    wa = 0
    ac_list = []
    wa_list = []
    for i in range(m):
        if s[i] == 'AC':
            ac_list.append(p[i])
        else:
            wa_list.append(p[i])
    ac = len(set(ac_list))
    wa = len(set(wa_list))
    print(ac,wa)

=======
Suggestion 2

def problem151_c():
    n,m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        p_i, s_i = input().split()
        p.append(p_i)
        s.append(s_i)
    print(p)
    print(s)
    print(n,m)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    plist = []
    for i in range(m):
        plist.append(list(input().split()))
    plist.sort(key=lambda x:x[0])
    print(plist)
    ac = 0
    wacount = 0
    for i in range(m):
        if plist[i][1] == 'AC':
            ac += 1
            wacount += int(plist[i][0]) - 1
        else:
            if int(plist[i][0]) - 1 == wacount:
                ac += 1
    print(ac,wacount)

=======
Suggestion 4

def main():
    #第一行输入
    n, m = map(int, input().split())
    #初始化题目状态
    p = [0]*n
    s = [0]*n
    #记录AC的题目数
    ac = 0
    #记录罚分
    wa = 0
    for i in range(m):
        #输入题号和状态
        pi, si = input().split()
        pi = int(pi)
        #如果是AC
        if si == "AC":
            #如果之前没AC过
            if s[pi-1] == 0:
                #AC题目数+1
                ac += 1
                #罚分+之前WA的数量
                wa += p[pi-1]
                #标记AC
                s[pi-1] = 1
        #如果是WA
        else:
            #之前没AC过
            if s[pi-1] == 0:
                #WA数量+1
                p[pi-1] += 1
    #输出答案
    print(ac, wa)

=======
Suggestion 5

def get_input():
    n,m = input().split(' ')
    n = int(n)
    m = int(m)
    p = []
    s = []
    for i in range(m):
        p_i,s_i = input().split(' ')
        p_i = int(p_i)
        p.append(p_i)
        s.append(s_i)
    return n,m,p,s

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    p = [0] * N
    s = [0] * N
    for i in range(M):
        p_i, s_i = input().split()
        p_i = int(p_i)
        p[p_i - 1] += 1
        if s_i == 'AC':
            s[p_i - 1] = 1
        else:
            if s[p_i - 1] != 1:
                s[p_i - 1] = 2
    ac = 0
    wa = 0
    for i in range(N):
        if s[i] == 1:
            ac += 1
            wa += p[i] - 1
        elif s[i] == 2:
            wa += p[i]
    print(ac, wa)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        p,s = input().split()
        p = int(p)
        if s == 'AC':
            ac[p-1] = 1
        else:
            if ac[p-1] == 0:
                wa[p-1] += 1
    print(sum(ac),sum([ac[i]*wa[i] for i in range(n)]))

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    ac = [0]*n
    wa = [0]*n
    for i in range(m):
        p,s = input().split()
        p = int(p)
        if s == "AC":
            ac[p-1] = 1
        else:
            if ac[p-1] == 0:
                wa[p-1] += 1
    print(sum(ac),sum([ac[i]*wa[i] for i in range(n)]))

=======
Suggestion 9

def main():
    n,m=map(int,input().split())
    p=[0]*n
    s=[0]*n
    for i in range(m):
        tmp=list(input().split())
        p[int(tmp[0])-1]+=1
        if tmp[1]=='AC':
            s[int(tmp[0])-1]=1
    ans=0
    for i in range(n):
        if s[i]==1:
            ans+=1
    s=[0]*n
    for i in range(m):
        tmp=list(input().split())
        if s[int(tmp[0])-1]==0:
            if tmp[1]=='WA':
                s[int(tmp[0])-1]=1
            elif tmp[1]=='AC':
                s[int(tmp[0])-1]=2
    wa=0
    for i in range(n):
        if s[i]==2:
            wa+=p[i]
    print(ans,wa)

=======
Suggestion 10

def problems151_c():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        a,b = input().split()
        p.append(int(a))
        s.append(b)
    ac = 0
    wa = 0
    for i in range(n):
        if s[i] == 'AC':
            ac += 1
            wa += p[i]
    print(ac,wa)

problems151_c()
