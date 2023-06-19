Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, k, sushi):
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.append((0, 0))
    sushi.append((0, 0))

    # pr

=======
Suggestion 2

def solve():
    # N, K = map(int, input().split())
    # sushi = [list(map(int, input().split())) for _ in range(N)]
    N, K = 7, 4
    sushi = [[1, 1], [2, 1], [3, 1], [4, 6], [4, 5], [4, 5], [4, 5]]

    sushi.sort(key=lambda x: x[1], reverse=True)
    print(sushi)
    sushi.sort(key=lambda x: x[0])
    print(sushi)

    print('sushi', sushi)
    eat = sushi[:K]
    print('eat', eat)
    base = sum([i[1] for i in eat])
    print('base', base)
    kind = len(set([i[0] for i in eat]))
    print('kind', kind)
    ans = base + kind * kind
    print(ans)

=======
Suggestion 3

def main():
    # 读入数据
    n, k = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(tuple(map(int, input().split())))
    # 按美味程度降序排列
    s.sort(key=lambda x: x[1], reverse=True)
    # 选出美味程度最大的k个，按配料种类升序排列
    s = sorted(s[:k], key=lambda x: x[0])
    # 计算基本总美味
    base = sum(d for _, d in s)
    # 计算种类奖励
    bonus = sum(i * i for i in range(1, len(set(s)) + 1))
    # 输出结果
    print(base + bonus)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    sushi = []
    for _ in range(n):
        sushi.append(list(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    # print(sushi)
    # print(sushi[:k])
    # print(sushi[k:])
    # print(sushi[k-1][1])
    # print(sushi[:k])
    # print(sushi[:k][0])
    # print(sushi[:k][1])
    # print(sushi[:k][2])
    # print(sushi[:k][3])
    # print(sushi[:k][4])
    # print(sushi[:k][5])
    # print(sushi[:k][6])
    # print(sushi[:k][7])
    # print(sushi[:k][8])
    # print(sushi[:k][9])
    # print(sushi[:k][10])
    # print(sushi[:k][11])
    # print(sushi[:k][12])
    # print(sushi[:k][13])
    # print(sushi[:k][14])
    # print(sushi[:k][15])
    # print(sushi[:k][16])
    # print(sushi[:k][17])
    # print(sushi[:k][18])
    # print(sushi[:k][19])
    # print(sushi[:k][20])
    # print(sushi[:k][21])
    # print(sushi[:k][22])
    # print(sushi[:k][23])
    # print(sushi[:k][24])
    # print(sushi[:k][25])
    # print(sushi[:k][26])
    # print(sushi[:k][27])
    # print(sushi[:k][28])
    # print(sushi[:k][29])
    # print(sushi[:k][30])
    # print(sushi[:k][31])
    # print(sushi[:k][32])
    # print(sushi[:k][33])
    # print(sushi[:k][34])
    # print(sushi[:k][35])
    # print(sushi[:k][36])
    # print(sushi[:k][37])
    # print(sushi[:k][38])
    # print(sushi[:k][39])
    # print(sushi[:k][40])

=======
Suggestion 5

def main():
    n,k = map(int, input().split())
    t = []
    d = []
    for i in range(n):
        t1, d1 = map(int, input().split())
        t.append(t1)
        d.append(d1)
    # print(t)
    # print(d)
    # print("n,k = ", n,k)
    # print("t = ", t)
    # print("d = ", d)
    # print("sum(d) = ", sum(d))
    # print("sum(d[:k]) = ", sum(d[:k]))
    # print("sum(d[:k]) + (len(set(t[:k]))**2) = ", sum(d[:k]) + (len(set(t[:k]))**2))
    # print("sum(d[:k]) + (len(set(t[:k]))**2) = ", sum(d[:k]) + (len(set(t[:k]))**2))
    # print("sum(d[:k]) + (len(set(t[:k]))**2) = ", sum(d[:k]) + (len(set(t[:k]))**2))
    # print("sum(d[:k]) + (len(set(t[:k]))**2) = ", sum(d[:k]) + (len(set(t[:k]))**2))
    # print("sum(d[:k]) + (len(set(t[:k]))**2) = ", sum(d[:k]) + (len(set(t[:k]))**2))
    # print("sum(d[:k]) + (len(set(t[:k]))**2) = ", sum(d[:k]) + (len(set(t[:k]))**2))
    # print("sum(d[:k]) + (len(set(t[:k]))**2) = ", sum(d[:k]) + (len(set(t[:k]))**2))
    # print("sum(d[:k]) + (len(set(t[:k]))**2) = ", sum(d[:k]) + (len(set(t[:k]))**2))
    # print("sum(d[:k]) + (len(set(t[:k]))**2) = ", sum(d[:k]) + (len(set(t[:k]))**2))

    # for i in range(k):
    #     print("i = ", i)
    #     print("t[i] = ", t[i])
    #     print("d

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    sushi = []
    for _ in range(n):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    t_count = [0] * n
    t_count_set = set()
    count = 0
    for i in range(k):
        count += sushi[i][1]
        if sushi[i][0] not in t_count_set:
            t_count_set.add(sushi[i][0])
            t_count[i] = 1
    result = count + len(t_count_set) ** 2
    for i in range(k, n):
        if t_count[i] != 0:
            continue
        for j in range(k - 1, -1, -1):
            if t_count[j] == 0:
                continue
            if sushi[i][0] in t_count_set:
                continue
            t_count_set.remove(sushi[j][0])
            t_count[j] = 0
            t_count_set.add(sushi[i][0])
            t_count[i] = 1
            count = count - sushi[j][1] + sushi[i][1]
            result = max(result, count + len(t_count_set) ** 2)
            break
    print(result)

=======
Suggestion 7

def main():
    N, K = [int(x) for x in input().split()]
    sushis = []
    for i in range(N):
        t_i, d_i = [int(x) for x in input().split()]
        sushis.append((t_i, d_i))
    sushis.sort(key=lambda x: x[1], reverse=True)
    sushis.sort(key=lambda x: x[0])
    #print(sushis)
    used = []
    ans = 0
    count = 0
    for t_i, d_i in sushis:
        if t_i in used:
            ans += d_i
        else:
            if count < K:
                ans += d_i
                used.append(t_i)
                count += 1
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    tds = []
    for i in range(n):
        tds.append(list(map(int, input().split())))
    tds.sort(key=lambda x: x[1], reverse=True)
    print(tds)
    tds.sort(key=lambda x: x[0])
    print(tds)
    tds.sort(key=lambda x: x[1], reverse=True)
    print(tds)
    tds.sort(key=lambda x: x[0])
    print(tds)
    tds.sort(key=lambda x: x[1], reverse=True)
    print(tds)
    tds.sort(key=lambda x: x[0])
    print(tds)
    tds.sort(key=lambda x: x[1], reverse=True)
    print(tds)
    tds.sort(key=lambda x: x[0])
    print(tds)
    tds.sort(key=lambda x: x[1], reverse=True)
    print(tds)
    tds.sort(key=lambda x: x[0])
    print(tds)
    tds.sort(key=lambda x: x[1], reverse=True)
    print(tds)
    tds.sort(key=lambda x: x[0])
    print(tds)
    tds.sort(key=lambda x: x[1], reverse=True)
    print(tds)
    tds.sort(key=lambda x: x[0])
    print(tds)
    tds.sort(key=lambda x: x[1], reverse=True)
    print(tds)
    tds.sort(key=lambda x: x[0])
    print(tds)
    tds.sort(key=lambda x: x[1], reverse=True)
    print(tds)
    tds.sort(key=lambda x: x[0])
    print(tds)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    t_d_list = [list(map(int, input().split())) for _ in range(n)]
    t_d_list.sort(key=lambda x: x[1], reverse=True)
    t_d_list.sort(key=lambda x: x[0])
    print(t_d_list)
    # 用于记录每种配料出现的次数
    t_list = [0] * n
    # 用于记录每种配料的最大美味值
    d_list = [0] * n
    for i in range(n):
        t_list[t_d_list[i][0]-1] += 1
        d_list[t_d_list[i][0]-1] = t_d_list[i][1]
    print(t_list)
    print(d_list)
    # 用于记录每种配料的美味值的最大k个值
    d_max_list = [0] * n
    for i in range(n):
        if t_list[i] != 0:
            d_max_list[i] = d_list[i]
    print(d_max_list)
    # 用于记录每种配料的美味值的最大k个值的和
    d_max_sum = sum(d_max_list)
    print(d_max_sum)
    # 用于记录每种配料的美味值的最大k个值的和的最大值
    d_max_sum_max = d_max_sum
    print(d_max_sum_max)
    # 用于记录每种配料的美味值的最大k个值的和的最大值的最大值
    d_max_sum_max_max = d_max_sum_max
    print(d_max_sum_max_max)
    # 用于记录每种配料的美味值的最大k个值的和的最大值的最大值的最大值
    d_max_sum_max_max_max = d_max_sum_max_max
    print(d_max_sum_max_max_max)
    # 用于记录每种配料的美味值的最大k个值的和的最大值的最大值的最大值的最大值
    d_max_sum_max_max_max_max = d_max_sum_max_max_max
    print(d_max_sum

=======
Suggestion 10

def solve():
    N,K = map(int,input().split())
    sushi = []
    for i in range(N):
        t,d = map(int,input().split())
        sushi.append((t,d))
    sushi.sort(key=lambda x:x[1],reverse=True)
    sushi.sort(key=lambda x:x[0])
    #print(sushi)
    eat = []
    eat_type = set()
    eat_type_num = 0
    eat_num = 0
    eat_type_num_max = 0
    eat_type_num_max_list = []
    eat_num_max = 0
    eat_num_max_list = []
    eat_num_max_list_2 = []
    for i in range(N):
        if sushi[i][0] not in eat_type:
            if eat_type_num == K:
                break
            eat.append(sushi[i])
            eat_type.add(sushi[i][0])
            eat_type_num += 1
            eat_num += sushi[i][1]
        else:
            eat_num_max_list.append(sushi[i])
    #print(eat_num_max_list)
    for i in range(len(eat_num_max_list)):
        if eat_num_max_list[i][1] not in eat_num_max_list_2:
            eat_num_max_list_2.append(eat_num_max_list[i][1])
    #print(eat_num_max_list_2)
    eat_num_max_list_2.sort(reverse=True)
    #print(eat_num_max_list_2)
    for i in range(len(eat_num_max_list_2)):
        for j in range(len(eat_num_max_list)):
            if eat_num_max_list_2[i] == eat_num_max_list[j][1]:
                eat_num_max_list_2[i] = eat_num_max_list[j]
    #print(eat_num_max_list_2)
    for i in range(len(eat_num_max_list_2)):
        if eat_num_max_list_2[i][0] not in eat_type:
            eat.append(eat_num_max_list_2[i])
            eat_type.add(eat_num_max_list_2[i][0])
            eat_num += eat_num_max_list_2[i][1]
            eat_type_num += 1
            break
    #print(eat)
    #print(eat_type)
    #print(eat_num)
    #print(eat_type_num)
    #print(eat_type_num_max_list)
    #print(eat
