Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    neta = []
    for i in range(n):
        t,d = map(int,input().split())
        neta.append([d,t])
    neta.sort(reverse=True)
    #print(neta)
    #print(neta[:k])

=======
Suggestion 2

def solve():
    # N, K = map(int, input().split())
    # sushi = []
    # for _ in range(N):
    #     t, d = map(int, input().split())
    #     sushi.append((t, d))
    N, K = 6, 5
    sushi = [(5, 1000000000), (2, 990000000), (3, 980000000), (6, 970000000), (6, 960000000), (4, 950000000)]
    sushi.sort(key=lambda x: -x[1])
    # print(sushi)
    # print()
    # print()
    # print()

=======
Suggestion 3

def main():
    n,k = map(int, input().split())
    sushi = []
    for _ in range(n):
        sushi.append(list(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    print(sushi)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    sushi = []
    for _ in range(n):
        sushi.append(list(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])

    print(sushi)
    print(sushi[0:k])

    # for i in range(k):
    #     print(sushi[i][1])

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    t_d = [list(map(int,input().split())) for _ in range(n)]
    t_d.sort(key=lambda x:x[1],reverse=True)
    #print(t_d)
    t = []
    d = []
    for i in range(n):
        t.append(t_d[i][0])
        d.append(t_d[i][1])
    #print(t,d)
    t_d = []
    for i in range(n):
        t_d.append([t[i],d[i]])
    #print(t_d)
    t_d.sort(key=lambda x:x[0])
    #print(t_d)
    t = []
    d = []
    for i in range(n):
        t.append(t_d[i][0])
        d.append(t_d[i][1])
    #print(t,d)
    t_d = []
    for i in range(n):
        t_d.append([t[i],d[i]])
    #print(t_d)
    s = 0
    t = []
    d = []
    for i in range(n):
        if t_d[i][0] not in t:
            t.append(t_d[i][0])
            d.append(t_d[i][1])
    #print(t,d)
    for i in range(k):
        s += d[i]
    #print(s)
    for i in range(n):
        if t_d[i][0] not in t[:k]:
            s += t_d[i][1]
    print(s)

=======
Suggestion 6

def main():
    # 读入
    N, K = map(int, input().split())
    # 建立一个字典
    d = {}
    for i in range(N):
        t, d_ = map(int, input().split())
        if t not in d:
            d[t] = [d_]
        else:
            d[t].append(d_)
    # 按照美味程度排序
    for k in d.keys():
        d[k].sort(reverse=True)
    # 按照美味程度排序
    sushi = []
    for k in d.keys():
        sushi += d[k]
    sushi.sort(reverse=True)

    # print(sushi)
    # 从头开始吃K个
    # 1. 基本总美味
    base = sum(sushi[:K])
    # 2. 种类奖励
    kind = 0
    # 计算种类奖励
    for k in d.keys():
        if len(d[k]) > 1:
            kind += (len(d[k]) - 1) ** 2
    # 输出
    print(base + kind)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    td = []
    for i in range(n):
        td.append(list(map(int,input().split())))
    td.sort(key=lambda x:x[1],reverse=True)
    td.sort(key=lambda x:x[0])
    print(td)
    t = []
    d = []
    for i in range(n):
        t.append(td[i][0])
        d.append(td[i][1])
    print(t)
    print(d)
    print()
    count = 0
    for i in range(k):
        count += d[i]
    print(count)
    print()
    count2 = 0
    for i in range(k):
        if t[i] not in t[:i]:
            count2 += 1
    print(count2)
    print()
    count3 = count + count2**2
    print(count3)
    print()

main()

=======
Suggestion 8

def solve():
    n, k = map(int, input().split())
    td = [list(map(int, input().split())) for _ in range(n)]
    td.sort(key=lambda x: -x[1])
    td.sort(key=lambda x: x[0])
    td.append([0, 0])
    i = 0
    j = 0
    s = 0
    t = []
    while i < n:
        while j < n and td[i][0] == td[j][0]:
            t.append(td[j][1])
            j += 1
        t.sort(reverse=True)
        for l in range(len(t)):
            if l < k - i:
                s += t[l]
            else:
                break
        i = j
        t = []
    print(s)

solve()

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    sushis = []
    for _ in range(n):
        t, d = map(int, input().split())
        sushis.append((t, d))
    sushis.sort(key=lambda x: x[1], reverse=True)
    t_set = set()
    sushis_selected = []
    for t, d in sushis:
        if t not in t_set:
            t_set.add(t)
            sushis_selected.append((t, d))
    sushis_selected.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for t, d in sushis_selected[:k]:
        ans += d
    t_set = set()
    t_count = 0
    for t, d in sushis_selected[:k]:
        if t not in t_set:
            t_set.add(t)
            t_count += 1
    ans += t_count ** 2
    print(ans)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    t_d = []
    for i in range(n):
        t_d.append(list(map(int,input().split())))
    t_d.sort(key=lambda x:x[1],reverse=True)
    t_d.sort(key=lambda x:x[0])
    t = []
    d = []
    for i in range(n):
        t.append(t_d[i][0])
        d.append(t_d[i][1])
    t_d = []
    for i in range(n):
        t_d.append([t[i],d[i]])
    t = []
    d = []
    for i in range(n):
        if t_d[i][0] not in t:
            t.append(t_d[i][0])
            d.append(t_d[i][1])
    #print(t)
    #print(d)
    t_d = []
    for i in range(len(t)):
        t_d.append([t[i],d[i]])
    #print(t_d)
    d = []
    for i in range(len(t_d)):
        d.append(t_d[i][1])
    #print(d)
    for i in range(len(d)-1):
        if d[i] < d[i+1]:
            d[i+1] = d[i]
    #print(d)
    d = d[::-1]
    #print(d)
    d = d[:k]
    #print(d)
    print(sum(d)+len(d)**2)
