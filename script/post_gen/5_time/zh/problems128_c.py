Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    K = [0] * M
    S = [[]] * M
    P = [0] * M
    for i in range(M):
        K[i], *S[i] = map(int, input().split())
    P = list(map(int, input().split()))

    ans = 0
    for i in range(2 ** N):
        for j in range(M):
            cnt = 0
            for s in S[j]:
                if (i >> (s - 1)) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 2

def get_number_of_combinations(N, M, K, S, P):
    """
    N: number of switches
    M: number of light bulbs
    K: list of number of switches connected to each light bulb
    S: list of switches connected to each light bulb
    P: list of remainders for each light bulb
    """
    combinations = 0
    for i in range(2**N):
        # convert i to binary
        i_binary = "{0:b}".format(i)
        # pad the binary string with 0s
        i_binary = i_binary.zfill(N)
        # check if the switch combination satisfies the remainders
        if satisfies_remainders(i_binary, K, S, P):
            combinations += 1
    return combinations

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    k = []
    s = []
    p = []
    for i in range(m):
        k.append(list(map(int,input().split()))[0])
        s.append(list(map(int,input().split())))
    p = list(map(int,input().split()))
    ans = 0
    for i in range(2**n):
        flag = True
        for j in range(m):
            on = 0
            for sij in s[j]:
                if (i >> (sij-1)) & 1:
                    on += 1
            if on % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def check_on_off(switch, bulb, p):
    #print("switch: ", switch)
    #print("bulb: ", bulb)
    #print("p: ", p)
    for i in range(bulb):
        count = 0
        for j in range(len(switch[i])):
            if switch[i][j] in p:
                count += 1
        if count % 2 != p[i]:
            return False
    return True

=======
Suggestion 6

def get_input():
    N, M = map(int, input().split())
    k = [0] * M
    s = [0] * M
    for i in range(M):
        k[i], *s[i] = map(int, input().split())
        s[i].sort()
    p = list(map(int, input().split()))
    return N, M, k, s, p

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        k.append(list(map(int, input().split())))
    for i in range(M):
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    print(N, M)
    print(k)
    print(s)
    print(p)
    return 0

=======
Suggestion 8

def solve(N, M, k, s, p):
    result = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            count = 0
            for l in range(k[j]):
                if (i >> (s[j][l]-1) & 1):
                    count += 1
            if (count % 2 != p[j]):
                flag = False
                break
        if (flag):
            result += 1
    return result

=======
Suggestion 9

def get_light_num(num, switch, light):
    switch_num = len(switch)
    switch_status = [0] * switch_num
    light_status = [0] * light
    for i in range(num):
        for j in range(switch_num):
            if (i + 1) in switch[j]:
                switch_status[j] += 1
    for i in range(switch_num):
        switch_status[i] = switch_status[i] % 2
    for i in range(switch_num):
        for j in range(light):
            if (j + 1) in switch[i]:
                light_status[j] += switch_status[i]
    for i in range(light):
        light_status[i] = light_status[i] % 2
    if light_status.count(1) == 0:
        return 1
    else:
        return 0
