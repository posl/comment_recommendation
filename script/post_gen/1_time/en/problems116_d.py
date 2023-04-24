Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    T = []
    D = []
    for i in range(N):
        t, d = map(int, input().split())
        T.append(t)
        D.append(d)
    T = [t-1 for t in T]
    D = [(d, i) for i, d in enumerate(D)]
    D.sort(reverse=True)
    Kinds = set()
    S = 0
    for i in range(K):
        t = T[D[i][1]]
        d = D[i][0]
        Kinds.add(t)
        S += d
    if len(Kinds) == K:
        print(S + K*K)
    else:
        Kinds = list(Kinds)
        Kinds.sort()
        Score = [0]*(K+1)
        for i in range(K):
            Score[i+1] = Score[i] + D[i][0]
        Max = 0
        for i in range(K):
            n = len(Kinds)
            for j in range(n):
                if T[D[i][1]] == Kinds[j]:
                    break
            k = i - j
            s = Score[i+1] + Score[K] - Score[K-k] + (n+1)*(n+1)
            Max = max(Max, s)
        print(Max)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    T = [0] * N
    D = [0] * N
    for i in range(N):
        t, d = map(int, input().split())
        T[i] = t - 1
        D[i] = d
    D.sort(reverse=True)
    T.sort(reverse=True)
    T = list(set(T))
    T.sort()
    if len(T) <= K:
        print(sum(D))
        return
    ans = 0
    for i in range(K + 1):
        if i == 0:
            for j in range(K):
                ans += D[j]
            continue
        if i == K:
            for j in range(i):
                ans += D[j]
            continue
        if i == len(T):
            for j in range(i):
                ans += D[j]
            continue
        tmp = 0
        for j in range(i):
            tmp += D[j]
        for j in range(i):
            if T[j] == T[i]:
                for k in range(i, K):
                    tmp += D[k]
                break
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    T = [0] * N
    D = [0] * N
    for i in range(N):
        t, d = map(int, input().split())
        T[i] = t - 1
        D[i] = d
    D.sort(reverse=True)
    T.sort()
    T.append(N)
    cnt = [0] * N
    for i in range(N):
        cnt[T[i]] += 1
    cnt.sort(reverse=True)
    K = min(K, N - cnt.count(0))
    ans = 0
    tmp = 0
    for i in range(N):
        tmp += D[i]
        if cnt[T[i]] > 0:
            cnt[T[i]] -= 1
            K -= 1
        if K == 0:
            ans = max(ans, tmp + K * K)
        else:
            ans = max(ans, tmp + K * K)
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    Sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        Sushi.append((d, t))
    Sushi.sort(reverse=True)
    #print(Sushi)
    #print(K)
    #print(N)
    #print(Sushi[0][0])
    #print(Sushi[0][1])
    #print(Sushi[1][0])
    #print(Sushi[1][1])
    #print(Sushi[2][0])
    #print(Sushi[2][1])
    #print(Sushi[3][0])
    #print(Sushi[3][1])
    #print(Sushi[4][0])
    #print(Sushi[4][1])
    #print(Sushi[5][0])
    #print(Sushi[5][1])
    #print(Sushi[6][0])
    #print(Sushi[6][1])
    #print(Sushi[7][0])
    #print(Sushi[7][1])
    #print(Sushi[8][0])
    #print(Sushi[8][1])
    #print(Sushi[9][0])
    #print(Sushi[9][1])
    #print(Sushi[10][0])
    #print(Sushi[10][1])
    #print(Sushi[11][0])
    #print(Sushi[11][1])
    #print(Sushi[12][0])
    #print(Sushi[12][1])
    #print(Sushi[13][0])
    #print(Sushi[13][1])
    #print(Sushi[14][0])
    #print(Sushi[14][1])
    #print(Sushi[15][0])
    #print(Sushi[15][1])
    #print(Sushi[16][0])
    #print(Sushi[16][1])
    #print(Sushi[17][0])
    #print(Sushi[17][1])
    #print(Sushi[18][0])
    #print(Sushi[18][1])
    #print(Sushi[19][0])
    #print(Sushi[19][1])
    #print(Sushi[20][0])
    #print(Sushi[20][1])
    #print(Sushi[21][0])

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    Sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        Sushi.append((t, d))
    Sushi.sort(key=lambda x: x[1], reverse=True)
    Sushi = Sushi[:K]
    Sushi.sort(key=lambda x: x[0])
    kind = {}
    for i in range(K):
        if Sushi[i][0] in kind:
            kind[Sushi[i][0]] += 1
        else:
            kind[Sushi[i][0]] = 1
    kind = list(kind.values())
    kind.sort()
    ans = 0
    for i in range(len(kind)):
        ans += kind[i] * kind[i]
    ans += sum([Sushi[i][1] for i in range(len(kind))])
    for i in range(len(kind)):
        tmp = ans
        tmp -= kind[i] * kind[i]
        tmp += (kind[i] + 1) * (kind[i] + 1)
        tmp -= sum([Sushi[j][1] for j in range(kind[i])])
        tmp += sum([Sushi[j][1] for j in range(kind[i], len(kind))])
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)

    ans = 0
    kind = set()
    for i in range(K):
        kind.add(sushi[i][0])
        ans += sushi[i][1]
    ans += len(kind) ** 2
    for i in range(K, N):
        if sushi[i][0] in kind:
            continue
        kind.add(sushi[i][0])
        for j in range(K):
            if sushi[j][0] not in kind:
                continue
            kind.remove(sushi[j][0])
            ans = max(ans, ans - sushi[j][1] + sushi[i][1] + len(kind) ** 2)
            kind.add(sushi[j][0])
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    Sushi = [tuple(map(int, input().split())) for _ in range(N)]
    Sushi.sort(key=lambda x: x[1], reverse=True)
    types = set()
    ans = 0
    base = 0
    for i in range(K):
        base += Sushi[i][1]
        types.add(Sushi[i][0])
    ans = base + len(types)**2
    for i in range(K, N):
        if len(types) == K:
            break
        if Sushi[i][0] in types:
            continue
        types.add(Sushi[i][0])
        for j in range(K-1, -1, -1):
            if Sushi[j][0] in types:
                continue
            base += Sushi[i][1] - Sushi[j][1]
            types.add(Sushi[j][0])
            break
        ans = max(ans, base + len(types)**2)
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)

    # 種類ごとの食べた回数を保存する配列
    kinds = [0] * (N + 1)
    # 食べた回数の最大値を保存する変数
    kinds_max = 0
    # 今回食べた種類の数を保存する変数
    kinds_cnt = 0
    # 種類ごとの食べた回数を保存する配列
    kinds = [0] * (N + 1)

    # 種類ごとに食べた回数を記録する
    for i in range(K):
        kinds[sushi[i][0]] += 1
        # 種類が増えたらカウント
        if kinds[sushi[i][0]] == 1:
            kinds_cnt += 1

    # 最大値を更新
    kinds_max = max(kinds_max, kinds_cnt)

    # 今回食べた種類の数を保存する変数
    kinds_cnt = 0
    # 種類ごとの食べた回数を保存する配列
    kinds = [0] * (N + 1)

    # 一番美味しいものを食べる
    kinds[sushi[0][0]] += 1
    kinds_cnt += 1

    # 一番美味しいもの以外を食べる
    for i in range(1, K):
        kinds[sushi[i][0]] += 1
        # 種類が増えたらカウント
        if kinds[sushi[i][0]] == 1:
            kinds_cnt += 1

        # 一番美味しいものと同じ種類のものを食べる
        if sushi[i][0] == sushi

=======
Suggestion 9

def solve(N,K,topping,deliciousness):
    #print(N,K,topping,deliciousness)
    ans = 0
    for i in range(2**N):
        #print(i)
        #print(bin(i))
        #print(bin(i)[2:].zfill(N))
        #print(bin(i)[2:].zfill(N)[::-1])
        #print(bin(i)[2:].zfill(N)[::-1][:K])
        #print(bin(i)[2:].zfill(N)[::-1][K:])
        #print(bin(i)[2:].zfill(N)[::-1][:K].count('1'))
        #print(bin(i)[2:].zfill(N)[::-1][K:].count('1'))
        #print('---')
        if bin(i)[2:].zfill(N)[::-1][:K].count('1') == K:
            top = []
            deli = 0
            for j in range(N):
                if bin(i)[2:].zfill(N)[::-1][j]=='1':
                    top.append(topping[j])
                    deli += deliciousness[j]
            #print(top)
            #print(deli)
            #print(len(set(top)))
            #print(len(set(top))*len(set(top)))
            #print('---')
            if ans < deli + len(set(top))*len(set(top)):
                ans = deli + len(set(top))*len(set(top))
    return ans

=======
Suggestion 10

def read_int():
    return int(input())
