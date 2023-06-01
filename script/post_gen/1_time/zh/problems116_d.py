Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(n)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    type_cnt = {}
    type_list = []
    for t, d in sushi[:k]:
        if t not in type_cnt:
            type_cnt[t] = 0
            type_list.append(t)
        type_cnt[t] += 1
    type_list.sort()
    type_cnt_list = [type_cnt[t] for t in type_list]
    type_cnt_list.sort(reverse=True)
    t

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    sushi = []
    for _ in range(N):
        t,d = map(int,input().split())
        sushi.append((t,d))
    sushi = sorted(sushi,key=lambda x:x[1],reverse=True)
    from collections import defaultdict
    sushi_dic = defaultdict(list)
    for i in range(N):
        sushi_dic[sushi[i][0]].append(sushi[i][1])
    sushi_dic = sorted(sushi_dic.items(),key=lambda x:len(x[1]),reverse=True)
    sushi_dic = dict(sushi_dic)
    sushi_dic = sorted(sushi_dic.items(),key=lambda x:x[1][0],reverse=True)
    sushi_dic = dict(sushi_dic)
    sushi_dic = sorted(sushi_dic.items(),key=lambda x:x[1][0],reverse=True)
    sushi_dic = dict(sushi_dic)
    # print(sushi_dic)
    ans = 0
    sushi_dic_key = list(sushi_dic.keys())
    for i in range(K):
        ans += sushi_dic[sushi_dic_key[i]][0]
    ans += (K**2)
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        T, D = map(int, input().split())
        sushi.append((T, D))
    sushi.sort(key=lambda x: x[1], reverse=True)
    # print(sushi)
    kind = set()
    delicious = 0
    for i in range(K):
        kind.add(sushi[i][0])
        delicious += sushi[i][1]
    # print(kind, delicious)
    ans = delicious + len(kind) ** 2
    # print(ans)
    kind = list(kind)
    for i in range(K, N):
        if sushi[i][0] in kind:
            continue
        else:
            kind.append(sushi[i][0])
            delicious += sushi[i][1] - sushi[K - 1][1]
            ans = max(ans, delicious + len(kind) ** 2)
    print(ans)

=======
Suggestion 4

def input():
    n, k = map(int, input().split())
    sushi = []
    for i in range(n):
        sushi.append(list(map(int, input().split())))
    return n, k, sushi

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    t_d = []
    for i in range(n):
        t_d.append(list(map(int, input().split())))
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])

    t_set = set()
    d_sum = 0
    for i in range(k):
        d_sum += t_d[i][1]
        t_set.add(t_d[i][0])
    t_set_length = len(t_set)
    d_sum += t_set_length ** 2
    print(d_sum)

=======
Suggestion 6

def get_input():
    n, k = map(int, input().split())
    sushi = []
    for i in range(n):
        sushi.append(list(map(int, input().split())))
    return n, k, sushi

=======
Suggestion 7

def solve():
    import sys
    from collections import defaultdict
    from heapq import heappush, heappop
    input = sys.stdin.readline
    N, K = map(int, input().split())
    sushi = defaultdict(list)
    for _ in range(N):
        t, d = map(int, input().split())
        sushi[t].append(d)
    for v in sushi.values():
        v.sort(reverse=True)
    # 最初のK個を選ぶ
    sushi_heap = []
    for v in sushi.values():
        if len(v) >= 2:
            heappush(sushi_heap, (-(v[0] + v[1]), 0, 1))
    # 最初のK個を選んだ時の美味しさの合計
    ans = sum(v[0] for v in sushi.values())
    ans += sum(-v[0] for v in sushi_heap[:K - len(sushi)])
    # K個の中から1個ずつ入れ替えていく
    for _ in range(K - len(sushi)):
        v, i, j = heappop(sushi_heap)
        ans -= v
        if j + 1 < len(sushi[sushi_heap[i][1]]):
            heappush(sushi_heap, (-(sushi[sushi_heap[i][1]][j] + sushi[sushi_heap[i][1]][j + 1]), i, j + 1))
    print(ans)

=======
Suggestion 8

def get_input():
    n,k = map(int,input().split())
    sushi = []
    for i in range(n):
        t,d = map(int,input().split())
        sushi.append([t,d])
    return n,k,sushi

=======
Suggestion 9

def f(n, k, t, d):
    # 1. 按照t, d排序
    td = [(t[i], d[i]) for i in range(n)]
    td.sort(key=lambda x: (x[0], -x[1]))
    # 2. 按照t, d分组
    td_group = []
    td_group.append([td[0]])
    for i in range(1, n):
        if td[i][0] == td[i - 1][0]:
            td_group[-1].append(td[i])
        else:
            td_group.append([td[i]])
    # 3. 每组取前k个
    td_group = [sorted(x, key=lambda x: -x[1])[:k] for x in td_group]
    # 4. 取最大的k个
    td_group = sorted(td_group, key=lambda x: -sum([y[1] for y in x]))
    td_group = td_group[:k]
    # 5. 计算满意度
    return sum([y[1] for x in td_group for y in x]) + sum([len(x) ** 2 for x in td_group])

n, k = map(int, input().split())
t = []
d = []
for i in range(n):
    t_i, d_i = map(int, input().split())
    t.append(t_i)
    d.append(d_i)
print(f(n, k, t, d))

=======
Suggestion 10

def main():
    n,k=map(int,input().split())
    sushi=[]
    for _ in range(n):
        sushi.append(list(map(int,input().split())))
    sushi.sort(key=lambda x:x[1],reverse=True)
    sushi.sort(key=lambda x:x[0])
    print(sushi)
