Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    kind = set()
    kind_sushi = []
    ans = 0
    for i in range(K):
        ans += sushi[i][1]
        if sushi[i][0] in kind:
            kind_sushi.append(sushi[i][1])
        else:
            kind.add(sushi[i][0])
    ans += len(kind) ** 2
    kind_sushi.sort()
    for i in range(K, N):
        if sushi[i][0] in kind:
            continue
        if not kind_sushi:
            break
        ans += sushi[i][1] - kind_sushi.pop(0)
        kind.add(sushi[i][0])
    print(ans)
solve()

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    sushi = []
    for _ in range(n):
        sushi.append(list(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    from collections import defaultdict
    d = defaultdict(int)
    t = []
    for i in range(k):
        t.append(sushi[i][0])
        d[sushi[i][0]] += 1
    ans = sum([sushi[i][1] for i in range(k)]) + len(d)**2
    for i in range(k, n):
        if sushi[i][0] in d:
            continue
        if len(d) == k:
            break
        t.append(sushi[i][0])
        d[sushi[i][0]] += 1
        ans = max(ans, sum([sushi[i][1] for i in range(k)]) + len(d)**2)
    for i in range(k):
        if d[t[i]] > 1:
            continue
        for j in range(k, n):
            if sushi[j][0] == t[i]:
                continue
            t[i] = sushi[j][0]
            ans = max(ans, sum([sushi[i][1] for i in range(k)]) + len(d)**2)
            break
    print(ans)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]

    sushi.sort(key=lambda x: x[1], reverse=True)

    # 1. 一番美味しいものから順に，ネタの種類で分ける
    # 2. 各ネタの中で，一番美味しいものを選ぶ
    # 3. 各ネタの中で，二番目に美味しいものを選ぶ
    # 4. それ以降は，一番美味しいものを選ぶ
    # 5. 1~4を繰り返す
    # 6. 最後に，ネタの種類の数だけ，ネタの種類の数を加算する
    # 7. 6で得られた値が，最大のものを選ぶ

    # 1. 一番美味しいものから順に，ネタの種類で分ける
    sushi_by_t = [[] for _ in range(N + 1)]
    for t, d in sushi:
        sushi_by_t[t].append(d)

    # 2. 各ネタの中で，一番美味しいものを選ぶ
    sushi_by_t2 = [None for _ in range(N + 1)]
    for t in range(1, N + 1):
        if len(sushi_by_t[t]) == 0:
            continue
        sushi_by_t[t].sort(reverse=True)
        sushi_by_t2[t] = sushi_by_t[t][0]

    # 3. 各ネタの中で，二番目に美味しいものを選ぶ
    sushi_by_t3 = [None for _ in range(N + 1)]
    for t in range(1, N + 1):
        if len(sushi_by_t[t]) <= 1:
            continue
        sushi_by_t[t].sort(reverse=True)

=======
Suggestion 4

def solve(n, k, td):
    td.sort(key=lambda x: x[1], reverse=True)
    eat = [0] * (n + 1)
    eat_kind = []
    for i in range(k):
        eat[td[i][0]] += 1
        if eat[td[i][0]] == 1:
            eat_kind.append(td[i][0])
    eat_kind.sort()
    ans = sum([t[1] for t in td[:k]])
    ans += len(eat_kind) ** 2
    ans_max = ans
    for i in range(k, n):
        if eat[td[i][0]] == 0:
            eat[td[i][0]] += 1
            eat_kind.append(td[i][0])
        else:
            continue
        eat_kind.sort()
        eat[td[i - k][0]] -= 1
        if eat[td[i - k][0]] == 0:
            eat_kind.remove(td[i - k][0])
        ans = ans - td[i - k][1] + td[i][1] + len(eat_kind) ** 2
        ans_max = max(ans_max, ans)
    return ans_max


n, k = map(int, input().split())
td = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, k, td))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append([t, d])
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    #print(sushi[:K])
    #print(sushi[K:])
    #print(set(sushi[:K]))
    #print(set(sushi[K:]))
    max_sushi = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i + j > N:
                break
            #print(i, j)
            #print(sushi[:i])
            #print(sushi[K-j:])
            tmp_sushi = sushi[:i] + sushi[K-j:]
            tmp_sushi.sort(key=lambda x: x[0])
            #print(tmp_sushi)
            cnt = 0
            tmp_sum = 0
            for k in range(K):
                cnt += 1
                tmp_sum += tmp_sushi[k][1]
                #print(tmp_sushi[k])
            #print(cnt)
            #print(tmp_sum)
            tmp_sum += cnt * cnt
            max_sushi = max(max_sushi, tmp_sum)
    print(max_sushi)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    sushis = []
    for i in range(n):
        t,d = map(int,input().split())
        sushis.append((t,d))
    sushis.sort(key=lambda x:x[1],reverse=True)
    #print(sushis)
    #print(sushis[0][0],sushis[0][1])
    #print(sushis[1][0],sushis[1][1])
    #print(sushis[2][0],sushis[2][1])
    #print(sushis[3][0],sushis[3][1])
    #print(sushis[4][0],sushis[4][1])
    #print(sushis[5][0],sushis[5][1])
    #print(sushis[6][0],sushis[6][1])
    #print(sushis[7][0],sushis[7][1])
    #print(sushis[8][0],sushis[8][1])
    #print(sushis[9][0],sushis[9][1])
    #print(sushis[10][0],sushis[10][1])
    #print(sushis[11][0],sushis[11][1])
    #print(sushis[12][0],sushis[12][1])
    #print(sushis[13][0],sushis[13][1])
    #print(sushis[14][0],sushis[14][1])
    #print(sushis[15][0],sushis[15][1])
    #print(sushis[16][0],sushis[16][1])
    #print(sushis[17][0],sushis[17][1])
    #print(sushis[18][0],sushis[18][1])
    #print(sushis[19][0],sushis[19][1])
    #print(sushis[20][0],sushis[20][1])
    #print(sushis[21][0],sushis[21][1])
    #print(sushis[22][0],sushis[22

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    # print(sushi)
    types = set()
    sum_d = 0
    for t, d in sushi[:K]:
        sum_d += d
        types.add(t)
    # print(types)
    # print(sum_d)
    ans = sum_d + len(types)**2
    # print(ans)
    for t, d in sushi[K:]:
        if t not in types:
            sum_d += d
            types.add(t)
            ans = max(ans, sum_d + len(types)**2)
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    t = []
    d = []
    for i in range(n):
        t_i, d_i = map(int, input().split())
        t.append(t_i)
        d.append(d_i)
    sushi = []
    for i in range(n):
        sushi.append([d[i], t[i]])
    sushi.sort(reverse=True)
    eat = []
    eat_kind = []
    for i in range(k):
        eat.append(sushi[i][0])
        if sushi[i][1] not in eat_kind:
            eat_kind.append(sushi[i][1])
    ans = sum(eat) + len(eat_kind)**2
    print(ans)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    t = []
    d = []
    for i in range(n):
        a,b = map(int,input().split())
        t.append(a)
        d.append(b)
    #print(t)
    #print(d)
    d2 = []
    for i in range(n):
        d2.append([d[i],t[i]])
    #print(d2)
    d2.sort(reverse=True)
    #print(d2)
    d3 = []
    d4 = []
    for i in range(k):
        d3.append(d2[i][0])
        d4.append(d2[i][1])
    #print(d3)
    #print(d4)
    d4 = list(set(d4))
    #print(d4)
    d5 = []
    for i in range(len(d4)):
        d5.append(d4[i]*d4[i])
    #print(d5)
    d6 = []
    for i in range(len(d4)):
        d6.append(0)
    #print(d6)
    for i in range(len(d4)):
        for j in range(len(d)):
            if d4[i] == d[j]:
                d6[i] = d6[i]+d[j]
    #print(d6)
    print(sum(d3)+sum(d5))

=======
Suggestion 10

def solve(N, K, sushi):
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
    ans = 0
    used = set()
    maxd = 0
    for t, d in sushi:
        if t in used:
            maxd = max(maxd, d)
        else:
            used.add(t)
            ans += d
    ans += len(used) ** 2
    return ans - (maxd if len(used) == K else 0)
