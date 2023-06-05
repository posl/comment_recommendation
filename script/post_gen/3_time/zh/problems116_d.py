Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    sushi = []
    for _ in range(n):
        sushi.append(list(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi_dict = {}
    for i in range(n):
        if sushi[i][0] in sushi_dict.keys():
            sushi_dict[sushi[i][0]] += sushi[i][1]
        else:
            sushi_dict[sushi[i][0]] = sushi[i][1]
    sushi = []
    for key in sushi_dict.keys():
        sushi.append([key, sushi_dict[key]])
    sushi.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(k):
        ans += sushi[i][1]
    ans += k * k
    print(ans)

main()

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    sushi = []
    for i in range(n):
        t, d = map(int, input().split())
        sushi.append([t, d])
    sushi.sort(key=lambda x: x[1], reverse=True)
    from collections import defaultdict
    dic = defaultdict(int)
    for i in range(k):
        dic[sushi[i][0]] += 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(k):
        ans += sushi[i][1]
    ans += len(dic) ** 2
    now = ans
    for i in range(k, n):
        if dic[sushi[i][0] - 1][1] == 0:
            now -= len(dic) ** 2
            now += (len(dic) + 1) ** 2
            dic[sushi[i][0] - 1][1] += 1
            dic = sorted(dic, key=lambda x: x[1], reverse=True)
            ans = max(ans, now)
    print(ans)

=======
Suggestion 3

def solve():
    # 读取输入
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    # print(sushi)
    # 选出美味度最大的K个寿司
    # 选出来的寿司的种类
    kinds = set()
    # 选出来的寿司的美味度之和
    sum_d = 0
    # 选出来的寿司的美味度之和的平方
    sum_d2 = 0
    # 选出来的寿司的种类数
    kinds_num = 0
    # 选出来的寿司的种类数的平方
    kinds_num2 = 0
    for i in range(K):
        t, d = sushi[i]
        kinds.add(t)
        sum_d += d
        sum_d2 += d * d
    kinds_num = len(kinds)
    kinds_num2 = kinds_num * kinds_num
    # print(kinds_num, kinds_num2)
    # print(sum_d, sum_d2)
    # 满意度
    ans = sum_d2 + kinds_num2
    # print(ans)
    # 选出最大的满意度
    for i in range(K, N):
        t, d = sushi[i]
        # print(t, d)
        if t in kinds:
            continue
        # print(kinds)
        kinds_num += 1
        kinds_num2 = kinds_num * kinds_num
        sum_d2 = sum_d2 - d * d + sum_d * 2 * d + d * d
        # print(kinds_num, kinds_num2)
        # print(sum_d, sum_d2)
        ans = max(ans, sum_d2 + kinds_num2)
        # print(ans)
        kinds.add(t)
    print(ans)

=======
Suggestion 4

def input():
    n, k = map(int, input().split())
    sushi = []
    for _ in range(n):
        t, d = map(int, input().split())
        sushi.append((d, t))
    return n, k, sushi

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    kind = set()
    sum = 0
    for i in range(K):
        sum += sushi[i][1]
        kind.add(sushi[i][0])
    ans = sum + len(kind) ** 2
    for i in range(K, N):
        if sushi[i][0] not in kind:
            sum += sushi[i][1] - sushi[K - 1][1]
            kind.add(sushi[i][0])
            ans = max(ans, sum + len(kind) ** 2)
    print(ans)

solve()

=======
Suggestion 6

def solve():
    n, k = map(int, input().split())
    t_d = []
    for i in range(n):
        t, d = map(int, input().split())
        t_d.append((t, d))
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    # print(t_d)
    d = 0
    t_set = set()
    for i in range(k):
        d += t_d[i][1]
        t_set.add(t_d[i][0])
    # print(d, t_set)
    ans = d + len(t_set) ** 2
    # print(ans)
    for i in range(k, n):
        if t_d[i][0] not in t_set:
            d += t_d[i][1] - t_d[k - 1][1]
            t_set.add(t_d[i][0])
            ans = max(ans, d + len(t_set) ** 2)
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    sushi = []
    for _ in range(n):
        t,d = map(int,input().split())
        sushi.append((t,d))
    sushi.sort(key=lambda x:x[1],reverse=True)
    sushi.sort(key=lambda x:x[0])

    # print(sushi)

    # 配列tに寿司の種類を入れる
    t = []
    for i in range(n):
        t.append(sushi[i][0])

    # 配列dに寿司の美味しさを入れる
    d = []
    for i in range(n):
        d.append(sushi[i][1])

    # print(t)
    # print(d)

    # 配列dicに寿司の美味しさを入れる
    dic = {}
    for i in range(n):
        if t[i] in dic.keys():
            dic[t[i]].append(d[i])
        else:
            dic[t[i]] = [d[i]]

    # print(dic)

    # 配列d2に各種類の寿司の美味しさの最大値を入れる
    d2 = []
    for i in range(1,n+1):
        d2.append(max(dic[i]))

    # print(d2)

    # 配列d3に各種類の寿司の美味しさの最大値を降順に入れる
    d3 = sorted(d2,reverse=True)

    # print(d3)

    # 配列d4に各種類の寿司の美味しさの最大値の累積和を入れる
    d4 = []
    d4.append(d3[0])
    for i in range(1,n):
        d4.append(d4[i-1]+d3[i])

    # print(d4)

    # 配列d5に各種類の寿司の美味しさの最大値の累積和の最大値を入れる
    d5 = []
    for i in range(k-1,n):
        d5.append(d4[i])

=======
Suggestion 8

def solve():
    n, k = map(int, input().split())
    td = [list(map(int, input().split())) for _ in range(n)]
    td.sort(key=lambda x: x[1], reverse=True)
    t = [0] * n
    d = [0] * n
    for i in range(n):
        t[i] = td[i][0]
        d[i] = td[i][1]
    from collections import defaultdict
    dic = defaultdict(list)
    for i in range(n):
        dic[t[i]].append(d[i])
    dic = sorted(dic.items(), key=lambda x: x[0])
    # print(dic)
    ans = 0
    for i in range(k):
        ans += d[i]
    # print(ans)
    cnt = 0
    for i in range(k):
        if len(dic[t[i]]) > 1:
            cnt += 1
    # print(cnt)
    if cnt == 0:
        print(ans)
        exit()
    for i in range(k, n):
        if len(dic[t[i]]) > 1:
            for j in range(len(dic[t[i]]) - 1):
                if cnt == 0:
                    print(ans)
                    exit()
                ans += dic[t[i]][j]
                cnt -= 1
    print(ans)

=======
Suggestion 9

def solve():
    N,K = map(int,input().split())
    t = []
    d = []
    for i in range(N):
        t_i,d_i = map(int,input().split())
        t.append(t_i)
        d.append(d_i)
    sushi = []
    for i in range(N):
        sushi.append([d[i],t[i]])
    sushi.sort(reverse=True)
    #print(sushi)
    #print(sushi[0][0])
    #print(sushi[0][1])
    #print(sushi[1][0])
    #print(sushi[1][1])
    #print(sushi[2][0])
    #print(sushi[2][1])
    #print(sushi[3][0])
    #print(sushi[3][1])
    #print(sushi[4][0])
    #print(sushi[4][1])
    #print(sushi[5][0])
    #print(sushi[5][1])
    #print(sushi[6][0])
    #print(sushi[6][1])
    #print(sushi[7][0])
    #print(sushi[7][1])
    #print(sushi[8][0])
    #print(sushi[8][1])
    #print(sushi[9][0])
    #print(sushi[9][1])
    #print(sushi[10][0])
    #print(sushi[10][1])
    #print(sushi[11][0])
    #print(sushi[11][1])
    #print(sushi[12][0])
    #print(sushi[12][1])
    #print(sushi[13][0])
    #print(sushi[13][1])
    #print(sushi[14][0])
    #print(sushi[14][1])
    #print(sushi[15][0])
    #print(sushi[15][1])
    #print(sushi[16][0])
    #print(sushi[16][1])
    #print(sushi[17][0])
    #print(sushi[17][1])
    #print(sushi[18][0])
    #print(sushi[18][1])
    #print(sushi[19][0])
    #print(sushi[19][1])
    #print(sushi[20][0])
    #print(sushi[

=======
Suggestion 10

def max_sushi(N, K, sushi):
    sushi.sort(key=lambda x: x[1], reverse=True)
    # print(sushi)
    # print(sushi[:K])
    # print(sushi[K:])
    # print(len(set(sushi[:K])))
    # print(len(set(sushi[K:])))
    # print(len(set(sushi[K:]))**2)
    return sum([x[1] for x in sushi[:K]]) + len(set(sushi[:K]))**2
