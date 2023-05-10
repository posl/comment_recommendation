Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    t_d = []
    for i in range(n):
        t,d = map(int,input().split())
        t_d.append([t,d])
    t_d.sort(key=lambda x:x[1],reverse=True)
    #print(t_d)
    t_d_t = t_d[:k]
    #print(t_d_t)
    t_d_t.sort(key=lambda x:x[0])
    #print(t_d_t)
    t_d_t_t = []
    for i in range(len(t_d_t)):
        if t_d_t[i][0] not in t_d_t_t:
            t_d_t_t.append(t_d_t[i][0])
    #print(t_d_t_t)
    #print(len(t_d_t_t))
    t_d_t_t_t = len(t_d_t_t)**2
    #print(t_d_t_t_t)
    t_d_t_t_t_t = 0
    for i in range(len(t_d_t)):
        t_d_t_t_t_t += t_d_t[i][1]
    #print(t_d_t_t_t_t)
    print(t_d_t_t_t_t+t_d_t_t_t_t_t)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    used = set()
    base = 0
    for i in range(K):
        base += sushi[i][1]
        used.add(sushi[i][0])
    #print(base)
    ans = base + len(used)**2
    #print(ans)
    for i in range(K, N):
        if sushi[i][0] not in used:
            used.add(sushi[i][0])
            base -= sushi[i-K][1]
            base += sushi[i][1]
            ans = max(ans, base + len(used)**2)
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append([d, t])
    sushi.sort(reverse=True)
    eat = []
    eat_kind = []
    ans = 0
    for i in range(N):
        if i < K:
            ans += sushi[i][0]
            if sushi[i][1] not in eat_kind:
                eat_kind.append(sushi[i][1])
            else:
                eat.append(sushi[i][0])
        else:
            if sushi[i][1] not in eat_kind:
                eat.append(sushi[i][0])
    eat.sort(reverse=True)
    eat_kind.sort()
    ans += sum(eat_kind)**2
    ans += sum(eat)
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        sushi.append(list(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    t = []
    d = []
    for i in range(N):
        t.append(sushi[i][0])
        d.append(sushi[i][1])
    t = t[:K]
    d = d[:K]
    t.sort()
    d.sort()
    d.reverse()
    t_set = set(t)
    t_set = list(t_set)
    t_set.sort()
    t_set.reverse()
    t_set = t_set[:len(t)]
    t_set.sort()
    t_set.reverse()
    t_set = t_set[:K]
    result = 0
    for i in range(K):
        result += d[i]
    result += len(t_set) ** 2
    print(result)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    #print(N, K)
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t,d))
    #print(sushi)
    sushi.sort(key=lambda x:x[1], reverse=True)
    #print(sushi)
    #print(sushi[0][1])
    #print(sushi[0][0])
    #print(sushi[1][1])
    #print(sushi[1][0])
    #print(sushi[2][1])
    #print(sushi[2][0])
    #print(sushi[3][1])
    #print(sushi[3][0])
    #print(sushi[4][1])
    #print(sushi[4][0])
    #print(sushi[5][1])
    #print(sushi[5][0])
    #print(sushi[6][1])
    #print(sushi[6][0])
    #print(sushi[7][1])
    #print(sushi[7][0])
    #print(sushi[8][1])
    #print(sushi[8][0])
    #print(sushi[9][1])
    #print(sushi[9][0])
    #print(sushi[10][1])
    #print(sushi[10][0])
    #print(sushi[11][1])
    #print(sushi[11][0])
    #print(sushi[12][1])
    #print(sushi[12][0])
    #print(sushi[13][1])
    #print(sushi[13][0])
    #print(sushi[14][1])
    #print(sushi[14][0])
    #print(sushi[15][1])
    #print(sushi[15][0])
    #print(sushi[16][1])
    #print(sushi[16][0])
    #print(sushi[17][1])
    #print(sushi[17][0])
    #print(sushi[18][1])
    #print(sushi[18][0])
    #print(sushi[19][1])
    #print(sushi[19][0])
    #print(sushi[20][1])
    #print(sushi[20][0])
    #print(s

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)

    # 前処理
    # 各ネタが何個あるかを記録しておく
    # 前から順に見ていくので、あるネタが何個あるかは、
    # そのネタの寿司に到達した時点で、そのネタの個数を記録する
    # そのネタの個数が2個目以降であれば、そのネタを食べることができる
    # また、そのネタの個数が2個目以降であれば、そのネタを食べた時の
    # 「種類ボーナスポイント」は、そのネタの個数を1つ減らした値の2乗である
    # また、そのネタの個数が2個目以降であれば、そのネタを食べた時の
    # 「おいしさ基礎ポイント」は、そのネタのおいしさである
    # なお、そのネタの個数が1個しかなければ、そのネタを食べることはできない
    # また、そのネタの個数が1個しかなければ、そのネタを食べた時の
    # 「種類ボーナスポイント」は、0 である
    # また、そのネタの個数が1個しかなければ、そのネタを食べた時の
    # 「おいしさ基礎ポイント」は、

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append([d, t])
    sushi.sort(reverse=True)
    #print(sushi)
    #print(sushi[:K])
    #print(sushi[K:])
    #print(sushi[K-1][0])
    #print(sushi[K-1][1])
    #print(sushi[K-1][0] * sushi[K-1][1])
    #print(sushi[K-1][1] * sushi[K-1][1])
    #print(sushi[K-1][0] * sushi[K-1][1] + sushi[K-1][1] * sushi[K-1][1])
    #print(sushi[K-1][0] * sushi[K-1][1] + sushi[K-1][1] * sushi[K-1][1] - sushi[K][0] * sushi[K][1])
    #print(sushi[K-1][0] * sushi[K-1][1] + sushi[K-1][1] * sushi[K-1][1] - sushi[K][0] * sushi[K][1] + sushi[K][1] * sushi[K][1])
    #print(sushi[K-1][0] * sushi[K-1][1] + sushi[K-1][1] * sushi[K-1][1] - sushi[K][0] * sushi[K][1] + sushi[K][1] * sushi[K][1] - sushi[K+1][0] * sushi[K+1][1])
    #print(sushi[K-1][0] * sushi[K-1][1] + sushi[K-1][1] * sushi[K-1][1] - sushi[K][0] * sushi[K][1] + sushi[K][1] * sushi[K][1] - sushi[K+1][0] * sushi[K+1][1] + sushi[K+1][1] * sushi[K+1][1])
    #print(sushi[K-1][0] * sushi[K-1][1] + sushi[K-1][1] * sushi[K-1][1] - sushi[K][0] * sushi[K][1] + sushi[K][1] * sushi[K][1] - sushi

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(n)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])

    # print(sushi)

    sushi_dict = {}
    for t, d in sushi:
        if t not in sushi_dict:
            sushi_dict[t] = []
        sushi_dict[t].append(d)

    # print(sushi_dict)

    sushi_list = []
    for t, d in sushi_dict.items():
        sushi_list.append([t, sum(d)])

    # print(sushi_list)

    sushi_list.sort(key=lambda x: x[1], reverse=True)

    # print(sushi_list)

    sushi_list = sushi_list[:k]

    # print(sushi_list)

    sushi_list.sort(key=lambda x: x[0])

    # print(sushi_list)

    sushi_list = sushi_list[::-1]

    # print(sushi_list)

    sushi_dict = {}
    for t, d in sushi_list:
        if t not in sushi_dict:
            sushi_dict[t] = []
        sushi_dict[t].append(d)

    # print(sushi_dict)

    sushi_list = []
    for t, d in sushi_dict.items():
        sushi_list.append([t, len(d)])

    # print(sushi_list)

    ans = 0
    for t, d in sushi_list:
        ans += d ** 2

    # print(ans)

    for t, d in sushi_list:
        ans += sum(sushi_dict[t])

    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    Sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        Sushi.append((t, d))
    Sushi.sort(key=lambda x: x[1], reverse=True)
    #print(Sushi)
    T = []
    D = []
    for i in range(K):
        t, d = Sushi[i]
        T.append(t)
        D.append(d)
    T.sort()
    #print(T)
    #print(D)
    ans = sum(D) + len(set(T))**2
    #print(ans)
    for i in range(K, N):
        if Sushi[i][0] in T:
            continue
        else:
            T.append(Sushi[i][0])
            D.append(Sushi[i][1])
            T.sort()
            D.sort(reverse=True)
            #print(T)
            #print(D)
            ans = max(ans, sum(D[:K]) + len(set(T))**2)
            #print(ans)
    print(ans)
main()

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    td = [list(map(int,input().split())) for _ in range(n)]
    td.sort(key=lambda x: x[1],reverse=True)
    t = [0 for _ in range(n)]
    d = [0 for _ in range(n)]
    for i in range(n):
        t[i] = td[i][0]
        d[i] = td[i][1]
    dsum = [0 for _ in range(n+1)]
    for i in range(n):
        dsum[i+1] = dsum[i] + d[i]
    tset = set()
    tset.add(t[0])
    tsum = [0 for _ in range(n+1)]
    for i in range(n):
        tsum[i+1] = tsum[i] + t[i]
        tset.add(t[i])
    tsum2 = [0 for _ in range(n+1)]
    for i in range(n):
        tsum2[i+1] = tsum2[i] + t[i]*t[i]
    ans = 0
    for i in range(1,k+1):
        ans = max(ans,dsum[i] + i*i)
    for i in range(k+1,n+1):
        if t[i-1] in tset:
            continue
        tset.add(t[i-1])
        ans = max(ans,dsum[i] + tsum[i] + i*i)
    for i in range(k+1,n+1):
        if t[i-1] not in tset:
            continue
        tset.remove(t[i-1])
        ans = max(ans,dsum[i] + tsum[i-1] + i*i - tsum2[i-1])
    print(ans)
