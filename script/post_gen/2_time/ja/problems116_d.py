Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    t = [0] * N
    d = [0] * N
    for i in range(N):
        t[i], d[i] = map(int, input().split())
    # おいしさが高い順にソート
    order = sorted(range(N), key=lambda x: d[x], reverse=True)
    # 選んだ寿司のネタ
    s = set()
    # 種類ボーナスポイント
    x = 0
    # おいしさ基礎ポイント
    y = 0
    # 選んだ寿司の種類数
    count = 0
    for i in range(K):
        if t[order[i]] not in s:
            count += 1
            s.add(t[order[i]])
        y += d[order[i]]
    x = count * count
    ans = y + x
    for i in range(K, N):
        if t[order[i]] in s:
            continue
        # 種類ボーナスポイントは最大でも K * K
        if x + 2 * count + 1 > K * K:
            break
        count += 1
        s.add(t[order[i]])
        y += d[order[i]]
        x += 2 * count + 1
        ans = max(ans, y + x)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    t = [0] * N
    d = [0] * N
    for i in range(N):
        t[i], d[i] = map(int, input().split())

    # おいしさの降順にソート
    idx = sorted(range(N), key=lambda x: d[x], reverse=True)

    # 選んだ寿司のネタの種類を管理
    kind = [0] * (N + 1)

    # おいしさの合計
    sum = 0

    # 選んだ寿司のネタの種類数
    k = 0

    # おいしさの合計が最大になるように選ぶ
    for i in range(K):
        sum += d[idx[i]]
        if kind[t[idx[i]]] == 0:
            k += 1
        kind[t[idx[i]]] += 1

    ans = sum + k * k

    # おいしさの合計が最大になるように選んだ寿司のネタを一つ減らす
    for i in range(K):
        if kind[t[idx[i]]] == 1:
            # 選んだ寿司のネタが一つしかない場合は、他の選んでいない寿司を選ぶ
            for j in range(N):
                if kind[t[j]] == 0:
                    sum -= d[idx[i]]
                    sum += d[j]
                    kind[t[idx[i]]] -= 1
                    kind[t[j]] += 1
                    ans = max(ans, sum + k * k)
                    break
        else:
            # 選んだ寿司のネタが二つ以上ある場合は、一番おいしさが低い寿司を選ぶ
            for j in range(i + 1, K):
                if t[idx[i]] == t[idx[j]]:
                    sum -= d[idx[i]]
                    sum += d[idx[j]]
                    kind[t[idx[i]]] -= 1

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    satsufy = 0
    kind = 0
    kind_list = []
    for i in range(K):
        satsufy += sushi[i][1]
        if sushi[i][0] not in kind_list:
            kind += 1
            kind_list.append(sushi[i][0])
    satsufy += kind * kind
    #print(satsufy)
    #print(kind)
    #print(kind_list)
    for i in range(K, N):
        if sushi[i][0] in kind_list:
            continue
        if sushi[i][1] < sushi[K-1][1]:
            break
        satsufy -= sushi[K-1][1]
        satsufy += sushi[i][1]
        satsufy -= kind * kind
        kind += 1
        kind_list.append(sushi[i][0])
        satsufy += kind * kind
        #print(satsufy)
        #print(kind)
        #print(kind_list)
    print(satsufy)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    sushi = sushi[:K]
    #print(sushi)
    t_set = set()
    t_list = []
    for t, d in sushi:
        if t not in t_set:
            t_set.add(t)
            t_list.append(t)
    #print(t_list)
    t_list.sort()
    #print(t_list)
    t_set = set(t_list)
    #print(t_set)
    #print(sushi)
    ans = 0
    for t, d in sushi:
        if t in t_set:
            ans += d
            t_set.remove(t)
    #print(ans)
    ans += len(t_list) * len(t_list)
    #print(ans)
    temp = ans
    #print(temp)
    for i in range(K-len(t_list)):
        #print(i)
        t, d = sushi[len(t_list)+i]
        #print(t, d)
        temp -= d
        #print(temp)
        temp -= len(t_list) * len(t_list)
        #print(temp)
        for j in range(len(t_list)-1, -1, -1):
            #print(j)
            t2, d2 = sushi[j]
            #print(t2, d2)
            if t2 != t:
                temp += d2
                #print(temp)
                temp += (len(t_list)-1) * (len(t_list)-1)
                #print(temp)
                temp -= (len(t_list)) * (len(t_list))
                #print(temp)
                if temp > ans:
                    ans = temp
                break
        else:
            break
    print(ans)

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

    # 種類数を数える
    kind = set()
    for i in range(K):
        kind.add(sushi[i][0])
    #print(kind)

    # 種類数とおいしさの合計を計算
    ans = 0
    for i in range(K):
        ans += sushi[i][1]
    ans += len(kind) ** 2
    #print(ans)

    # おいしい寿司から順に種類数を増やしていく
    for i in range(K, N):
        if sushi[i][0] in kind:
            continue
        kind.add(sushi[i][0])
        #print(kind)
        tmp = ans
        tmp -= sushi[i-K][1]
        tmp += sushi[i][1]
        tmp += 2 * len(kind) - 1
        ans = max(ans, tmp)
        #print(ans)

    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    Sushi = []
    for i in range(N):
        t_i, d_i = map(int, input().split())
        Sushi.append([t_i, d_i])
    Sushi.sort(key=lambda x: x[1], reverse=True)

    kind = set()
    kind.add(Sushi[0][0])
    point = Sushi[0][1]
    for i in range(1, K):
        if Sushi[i][0] in kind:
            point += Sushi[i][1]
        else:
            kind.add(Sushi[i][0])
            point += Sushi[i][1] + len(kind) ** 2 - (len(kind) - 1) ** 2
    ans = point

    for i in range(K, N):
        if len(kind) == K:
            break
        if Sushi[i][0] in kind:
            continue
        point += Sushi[i][1] - Sushi[K - 1][1]
        point += len(kind) ** 2 - (len(kind) - 1) ** 2
        kind.add(Sushi[i][0])
        ans = max(ans, point)
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    T = [None] * N
    D = [None] * N
    for i in range(N):
        t, d = map(int, input().split())
        T[i] = t
        D[i] = d

    # 種類数が多い順にソート
    order = sorted(range(N), key=lambda i: D[i], reverse=True)
    T = [T[i] for i in order]
    D = [D[i] for i in order]

    # 種類数が多い順に K 個を選ぶ
    selected = set()
    selected_d = []
    for i in range(K):
        selected.add(T[i])
        selected_d.append(D[i])
    ans = sum(selected_d) + len(selected) ** 2

    # 種類数が少ない順に残りを選ぶ
    for i in range(K, N):
        if T[i] in selected:
            continue
        else:
            # 一番おいしさが低い寿司を選ぶ
            min_d = min(selected_d)
            if D[i] <= min_d:
                continue
            else:
                selected.remove(T[selected_d.index(min_d)])
                selected.add(T[i])
                selected_d[selected_d.index(min_d)] = D[i]
                ans = max(ans, sum(selected_d) + len(selected) ** 2)

    print(ans)

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    sushi = []
    for i in range(N):
        t_i,d_i = map(int,input().split())
        sushi.append([t_i,d_i])
    sushi.sort(key=lambda x:x[1],reverse=True)
    #print(sushi)

    #種類数
    kind = set([sushi[i][0] for i in range(K)])
    #print(kind)
    #種類数のボーナス
    bonus = len(kind)*len(kind)
    #print(bonus)
    #おいしさの合計
    taste = sum([sushi[i][1] for i in range(K)])
    #print(taste)
    #満足度
    satisfaction = bonus + taste
    #print(satisfaction)
    #種類数がK個になるまで、おいしさの低い寿司を交換する
    for i in range(K,N):
        if len(kind) == K:
            break
        if sushi[i][0] in kind:
            continue
        else:
            kind.add(sushi[i][0])
            bonus = len(kind)*len(kind)
            taste -= sushi[i-K][1]
            taste += sushi[i][1]
            satisfaction = max(satisfaction,bonus+taste)
    print(satisfaction)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]

    # おいしさの大きい順にソート
    sushi.sort(key=lambda x: x[1], reverse=True)

    # おいしさの大きい順に K 個の寿司を食べる
    # そのときの種類数を求める
    kind = set()
    satis = 0
    for i in range(K):
        satis += sushi[i][1]
        kind.add(sushi[i][0])

    # 種類数の種類数を求める
    kind_num = len(kind)

    # おいしさの大きい順に K 個の寿司を食べたときの種類数の種類数の最大値を求める
    # おいしさの小さい順に食べていく
    for i in range(K):
        # おいしさの大きい順に K 個の寿司を食べたときの種類数の種類数を更新
        if sushi[i][0] in kind:
            kind_num -= 1
            kind.remove(sushi[i][0])
        # おいしさの小さい順に食べていく
        for j in range(K, N):
            # おいしさの小さい順に食べていく寿司が種類数に含まれていない場合
            if sushi[j][0] not in kind:
                # おいしさの大きい順に K 個の寿司を食べたときの種類数の種類数を更新
                kind_num += 1
                kind.add(sushi[j][0])
                # おいしさの大きい順に K 個の寿司を食べたときの種

=======
Suggestion 10

def main():
    N,K=map(int,input().split())
    sushi=[list(map(int,input().split())) for _ in range(N)]
    sushi.sort(key=lambda x:x[1],reverse=True)#おいしさで降順ソート
    sushi_kind=[0]*(N+1)
    sushi_kind[0]=1
    ans=0
    sum_=0
    kind=0
    for i in range(K):
        sum_+=sushi[i][1]
        kind+=sushi_kind[sushi[i][0]]
        sushi_kind[sushi[i][0]]+=1
    ans=sum_+kind**2
    for i in range(K,N):
        if sushi_kind[sushi[i][0]]==0:
            kind+=1
        sushi_kind[sushi[i][0]]+=1
        sum_+=sushi[i][1]
        sum_-=sushi[i-K][1]
        sushi_kind[sushi[i-K][0]]-=1
        if sushi_kind[sushi[i-K][0]]==0:
            kind-=1
        ans=max(ans,sum_+kind**2)
    print(ans)
