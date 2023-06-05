Synthesizing 10/10 solutions

=======
Suggestion 1

def problems128_c():
    pass

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    k = []
    s = []
    p = []
    for i in range(m):
        a = list(map(int,input().split()))
        k.append(a[0])
        s.append(a[1:])
    p = list(map(int,input().split()))
    #print(k,s,p)
    ans = 0
    for i in range(2**n):
        #print(i)
        flag = 0
        for j in range(m):
            cnt = 0
            for l in range(k[j]):
                #print(l,s[j][l])
                if (i>>(s[j][l]-1))&1:
                    cnt += 1
            if cnt%2 != p[j]:
                flag = 1
        if flag == 0:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    k = []
    for i in range(M):
        k.append(list(map(int,input().split())))
    p = list(map(int,input().split()))
    count = 0
    for i in range(2**N):
        on = 0
        for j in range(M):
            s = 0
            for l in range(k[j][0]):
                if i >> (k[j][l+1]-1) & 1:
                    s += 1
            if s % 2 == p[j]:
                on += 1
        if on == M:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    # 读入数据
    n, m = map(int, input().split())
    k = []
    s = []
    for i in range(m):
        k.append(int(input().split()[0]))
        s.append([int(x) for x in input().split()])

    p = [int(x) for x in input().split()]

    # 穷举
    ans = 0
    for i in range(2 ** n):
        # 计算灯泡状态
        light = [0] * m
        for j in range(n):
            if (i >> j) & 1 == 1:
                for l in range(m):
                    if j + 1 in s[l]:
                        light[l] += 1

        # 检查灯泡状态
        ok = True
        for j in range(m):
            if light[j] % 2 != p[j]:
                ok = False

        # 计数
        if ok:
            ans += 1

    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    switch = []
    for i in range(m):
        switch.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**n):
        on = [0]*m
        for j in range(n):
            if (i>>j)&1:
                for k in range(m):
                    if j+1 in switch[k][1:]:
                        on[k] += 1
        if on == p:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    k = []
    s = []
    for i in range(m):
        k.append(list(map(int, input().split())))
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))

    ans = 0
    for i in range(2 ** n):
        flag = True
        for j in range(m):
            count = 0
            for x in range(1, k[j][0] + 1):
                if i & (1 << (s[j][x - 1] - 1)):
                    count += 1
            if count % 2 != p[j]:
                flag = False
        if flag:
            ans += 1

    print(ans)

=======
Suggestion 7

def isLightUp(switch, bulb, p):
    for i in range(len(bulb)):
        if p[i] != sum([switch[j-1] for j in bulb[i]]) % 2:
            return False
    return True

=======
Suggestion 8

def get_lights_on_count(switches, bulbs, switch_bulbs, p):
    result = 0
    for i in range(2**switches):
        switch_state = []
        for j in range(switches):
            if (i >> j) & 1:
                switch_state.append(1)
            else:
                switch_state.append(0)
        #print(switch_state)
        bulbs_on = 0
        for k in range(bulbs):
            bulbs_on_temp = 0
            for l in range(switch_bulbs[k][0]):
                bulbs_on_temp += switch_state[switch_bulbs[k][l+1]-1]
            if bulbs_on_temp % 2 == p[k]:
                bulbs_on += 1
        if bulbs_on == bulbs:
            result += 1
    return result

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        ki, *si = map(int, input().split())
        k.append(ki)
        s.append(si)
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1 << N):
        for j in range(M):
            on = 0
            for l in range(k[j]):
                if i & (1 << s[j][l] - 1):
                    on += 1
            if on % 2 != p[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n,m=map(int,input().split())
    k=[]
    s=[]
    p=[]
    for i in range(m):
        k.append(list(map(int,input().split()))[0])
        s.append(list(map(int,input().split())))
    p=list(map(int,input().split()))
    count=0
    for i in range(2**n):
        flag=True
        for j in range(m):
            sum=0
            for l in range(k[j]):
                sum+=((i>>(s[j][l]-1))&1)
            if sum%2!=p[j]:
                flag=False
                break
        if flag:
            count+=1
    print(count)
