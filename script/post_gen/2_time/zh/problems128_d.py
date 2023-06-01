Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    k = [0] * m
    s = [0] * m
    for i in range(m):
        k[i],*s[i] = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(2**n):
        light = [0] * m
        for j in range(n):
            if (i >> j) & 1:
                for l in range(m):
                    if j+1 in s[l]:
                        light[l] += 1
        if all(light[l]%2 == p[l] for l in range(m)):
            ans += 1
    print(ans)

=======
Suggestion 2

def getSwitchState(switch_status, switch_num, bulb_num):
    if switch_num == 1:
        return [switch_status]
    else:
        switch_state = []
        for i in range(switch_num):
            if i == 0:
                switch_state.append([switch_status[i]])
            else:
                switch_state[0].append(switch_status[i])
        return switch_state

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def readinput():
    line = input()
    N,M = line.split()
    N = int(N)
    M = int(M)
    switches = []
    for i in range(M):
        line = input()
        switch = list(map(int, line.split()))
        switches.append(switch)
    line = input()
    P = list(map(int, line.split()))
    return (N,M,switches,P)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    k = []
    for _ in range(m):
        k.append(list(map(int,input().split()))[1:])
    p = list(map(int,input().split()))

    ans = 0
    for i in range(2**n):
        light = [0]*m
        for j in range(n):
            if (i>>j)&1 == 1:
                for l in range(m):
                    if j+1 in k[l]:
                        light[l] += 1
        if light == p:
            ans += 1

    print(ans)

=======
Suggestion 6

def get_switch_status(n, m, k, s, p):
    # n:开关个数
    # m:灯泡个数
    # k:灯泡与开关的关联关系
    # s:开关与灯泡的关联关系
    # p:开关状态
    # 灯泡i与k_i个开关相连：开关s_{i1}，s_{i2}，...，和s_{ik_i}。当这些开关中 "开 "的开关数与p_i的模数一致时，它就被点亮。
    # 有多少种开关的 "开 "和 "关 "状态的组合可以点亮所有的灯泡？

    # 灯泡状态
    bulb_status = [0] * m

    # 开关状态
    switch_status = [0] * n

    # 开关与灯泡的关联关系
    switch_bulb = {}
    for i in range(m):
        switch_bulb[i + 1] = s[i]

    # 灯泡与开关的关联关系
    bulb_switch = {}
    for i in range(n):
        bulb_switch[i + 1] = k[i]

    # 开关状态组合
    switch_status_combination = []

    # 灯泡状态组合
    bulb_status_combination = []

    # 灯泡与开关的关联关系组合
    bulb_switch_combination = []

    # 开关与灯泡的关联关系组合
    switch_bulb_combination = []

    # 灯泡状态组合
    bulb_status_combination = get_status_combination(bulb_status, bulb_status_combination)

    # 灯泡与开关的关联关系组合
    bulb_switch_combination = get_combination(bulb_switch_combination, bulb_switch)

    # 开关与灯泡的关联关系组合
    switch_bulb_combination = get_combination(switch_bulb_combination, switch_bulb)

    # 开关状态组合

=======
Suggestion 7

def problems128_c():
    pass

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    k = []
    s = []
    p = []
    for i in range(m):
        k.append(list(map(int,input().split())))
    for i in range(m):
        p.append(list(map(int,input().split())))
    print(k)
    print(p)

=======
Suggestion 9

def main():
    N, M = list(map(int, input().split()))
    k = []
    s = []
    for i in range(M):
        k.append(list(map(int, input().split()))[0])
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))

    # print(N, M)
    # print(k)
    # print(s)
    # print(p)

    # 2**N - 1种可能
    cnt = 0
    for i in range(2**N):
        # print("i = ", i)
        # print("bin(i) = ", bin(i))
        # print("bin(i)[2:] = ", bin(i)[2:])
        # print("len(bin(i)[2:]) = ", len(bin(i)[2:]))
        # print("N - len(bin(i)[2:]) = ", N - len(bin(i)[2:]))
        # print("str(bin(i)[2:]) = ", str(bin(i)[2:]))
        # print("str(bin(i)[2:]).zfill(N) = ", str(bin(i)[2:]).zfill(N))
        # print("str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):] = ", str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):])
        # print("len(str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):]) = ", len(str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):]))
        # print("list(str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):]) = ", list(str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):]))
        # print("list(map(int, str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):])) = ", list(map(int, str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):])))
        # print("list(map(int, str(bin(i)[2:]).zfill(N)[N - len(bin(i)[2:]):])) == [1] * N = ", list(map(int, str(bin(i)[2:]).zfill(N)[N -
