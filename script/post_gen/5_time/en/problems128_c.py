Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n,m=map(int,input().split())
    k=[]
    s=[]
    for _ in range(m):
        k.append(int(input()))
        s.append(list(map(int,input().split())))
    p=list(map(int,input().split()))
    return n,m,k,s,p

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = []
    p = []
    for i in range(m):
        s.append(list(map(int, input().split()))[1:])
    p = list(map(int, input().split()))

    ans = 0
    for i in range(2**n):
        flag = True
        for j in range(m):
            cnt = 0
            for k in range(len(s[j])):
                if (i >> (s[j][k]-1)) & 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1

    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        k.append(int(input().split()[0]))
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            count = 0
            for l in range(k[j]):
                if ((i >> (s[j][l]-1)) & 1) == 1:
                    count += 1
            if count % 2 != p[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(m):
        k.append(list(map(int, input().split()))[0])
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** n):
        tmp = []
        for j in range(n):
            if ((i >> j) & 1) == 1:
                tmp.append(1)
            else:
                tmp.append(0)
        flag = True
        for j in range(m):
            cnt = 0
            for l in range(k[j]):
                if tmp[s[j][l] - 1] == 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
        if flag == True:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))

    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            count = 0
            for l in range(k[j][0]):
                if (i >> (s[j][l] - 1)) & 1:
                    count += 1
            if count % 2 != p[j]:
                flag = False
        if flag:
            ans += 1

    print(ans)

=======
Suggestion 6

def get_input():
    n, m = map(int, input().split())
    k = []
    s = []
    for i in range(m):
        k.append(list(map(int, input().split())))
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    return n, m, k, s, p

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    s = []
    p = []
    for _ in range(m):
        *si, pi = map(int, input().split())
        s.append(si)
        p.append(pi)

    ans = 0
    for i in range(1 << n):
        flag = True
        for j in range(m):
            cnt = 0
            for k in s[j]:
                if i & (1 << (k - 1)):
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

main()

=======
Suggestion 8

def get_input():
    n, m = map(int, input().split())
    bulbs = []
    for i in range(m):
        bulbs.append([int(x) for x in input().split()])
    p = [int(x) for x in input().split()]
    return n, m, bulbs, p

=======
Suggestion 9

def on_off_combination(n,m,k,s,p):
    # n: number of switches
    # m: number of bulbs
    # k: number of switches connected to bulb
    # s: switches connected to bulb
    # p: state of bulb
    # return: number of combinations to turn on all bulbs
    comb = []
    for i in range(2**n):
        switch = []
        for j in range(n):
            if (i>>j)&1:
                switch.append(1)
            else:
                switch.append(0)
        comb.append(switch)

    count = 0
    for c in comb:
        bulb = []
        for i in range(m):
            light = 0
            for j in range(k[i]):
                light += c[s[i][j]-1]
            bulb.append(light%2)
        if bulb == p:
            count += 1
    return count

=======
Suggestion 10

def solve(N, M, switches, bulbs, states):
    #print(N, M, switches, bulbs, states)
    #print()
    #
