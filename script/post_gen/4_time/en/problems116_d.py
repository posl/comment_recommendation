Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    T = [0] * N
    D = [0] * N
    for i in range(N):
        T[i], D[i] = map(int, input().split())
    T = [t-1 for t in T]
    ans = 0
    for s in range(2**N):
        if bin(s).count('1') != K:
            continue
        t = [0] * N
        for i in range(N):
            if s & (1 << i):
                t[T[i]] += 1
        t = sorted(t, reverse=True)
        x = 0
        for i in range(N):
            if t[i] > 0:
                x += 1
            else:
                break
        total = 0
        for i in range(N):
            if s & (1 << i):
                total += D[i]
        ans = max(ans, total + x*x)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    T = []
    D = []
    for i in range(N):
        t, d = map(int, input().split())
        T.append(t)
        D.append(d)

    T = list(set(T))
    T = sorted(T, key=lambda x: T.index(x))
    T = [0] + T

    D = sorted(D, reverse=True)
    D = [0] + D

    ans = 0
    for i in range(1, K + 1):
        for j in range(1, N + 1):
            if T.index(T[j]) < i:
                continue
            ans = max(ans, sum(D[1:i]) + i * i + sum(D[i + 1:j]))
            break

    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((d, t))
    sushi.sort(reverse=True)
    kinds = set()
    kinds.add(sushi[0][1])
    base = sushi[0][0]
    bonus = len(kinds)**2
    ans = base+bonus
    for i in range(1, K):
        base += sushi[i][0]
        kinds.add(sushi[i][1])
        bonus = len(kinds)**2
        ans = max(ans, base+bonus)
    if K == N:
        print(ans)
        return
    for i in range(K, N):
        if sushi[i][1] in kinds:
            continue
        base += sushi[i][0]
        kinds.add(sushi[i][1])
        bonus = len(kinds)**2
        base -= sushi[K-1][0]
        kinds.remove(sushi[K-1][1])
        bonus -= len(kinds)**2
        ans = max(ans, base+bonus)
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    Sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        Sushi.append((t, d))
    Sushi.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    t_set = set()
    t_list = []
    for t, d in Sushi[:K]:
        ans += d
        if t not in t_set:
            t_list.append(t)
            t_set.add(t)
    ans += len(t_list)**2
    c = len(t_list)
    for i in range(K, N):
        if Sushi[i][0] in t_set:
            continue
        t, d = Sushi[i]
        t_set.add(t)
        t_list.append(t)
        ans += d - Sushi[c][1]
        c += 1
        ans += 2*len(t_list) - 1
        if ans > 10**18:
            ans = 10**18
    print(ans)

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    T = [0]*N
    D = [0]*N
    for i in range(N):
        t,d = map(int,input().split())
        T[i] = t
        D[i] = d
    D,T = zip(*sorted(zip(D,T),reverse=True))
    D = list(D)
    T = list(T)
    D = D[:K]
    T = T[:K]
    D.sort(reverse=True)
    T.sort()
    T.append(0)
    s = sum(D)
    x = len(set(T))
    ans = s + x*x
    for i in range(K):
        if T[i] != T[i+1]:
            s -= D[i]
            x -= 1
            if x == 0:
                break
            ans = max(ans,s+x*x)
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    T = []
    for _ in range(N):
        t, d = map(int, input().split())
        T.append((t, d))
    T.sort(key=lambda x: x[1], reverse=True)
    T = T[:K]

    T.sort()
    t = [0] * (N + 1)
    for i in range(K):
        t[T[i][0]] += 1

    ans = 0
    for i in range(K):
        ans += T[i][1]
    ans += t.count(1) * t.count(1)
    tmp = ans
    for i in range(K):
        if t[T[i][0]] == 1:
            continue
        t[T[i][0]] -= 1
        tmp -= T[i][1]
        tmp -= t.count(1) * t.count(1)
        tmp += t.count(1) * t.count(1)
        ans = max(ans, tmp)

    print(ans)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    sushis = []
    for i in range(N):
        t,d = map(int,input().split())
        sushis.append((d,t))
    sushis.sort(reverse=True)
    kinds = set()
    kinds.add(sushis[0][1])
    base = sushis[0][0]
    bonus = 1
    ans = base + bonus**2
    for i in range(1,N):
        if len(kinds) == K:
            if sushis[i][1] in kinds:
                base += sushis[i][0]
                if base + bonus**2 > ans:
                    ans = base + bonus**2
            else:
                break
        else:
            base += sushis[i][0]
            kinds.add(sushis[i][1])
            bonus += 1
            if base + bonus**2 > ans:
                ans = base + bonus**2
    print(ans)

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    kind = set()
    ans = 0
    s = 0
    for i in range(N):
        s += sushi[i][1]
        kind.add(sushi[i][0])
        if len(kind) == K:
            ans = max(ans, s + K * K)
        elif len(kind) > K:
            for j in range(i - 1, -1, -1):
                if sushi[i][0] == sushi[j][0]:
                    s -= sushi[j][1]
                    kind.remove(sushi[j][0])
                    break
            ans = max(ans, s + len(kind) * len(kind))
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    sushi = [tuple(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    topping = set()
    topping.add(sushi[0][0])
    ans = sushi[0][1] + len(topping) ** 2
    left = 0
    right = 1
    while len(topping) < K and right < N:
        if sushi[right][0] not in topping:
            topping.add(sushi[right][0])
        right += 1
        while len(topping) > K:
            if sushi[left][0] in topping:
                topping.remove(sushi[left][0])
            left += 1
        ans = max(ans, sum(map(lambda x: x[1], sushi[left:right])) + len(topping) ** 2)
    print(ans)

=======
Suggestion 10

def main():
    #input
    N,K = map(int,input().split())
    TD = [list(map(int,input().split())) for _ in range(N)]
    #solve
    TD.sort(key=lambda x:x[1],reverse=True)
    tset = set()
    tlist = []
    i = 0
    while len(tlist) < K:
        if TD[i][0] not in tset:
            tset.add(TD[i][0])
            tlist.append(TD[i][0])
        i += 1
    ans = sum([TD[j][1] for j in range(K)])
    ans += len(tlist)**2
    for j in range(K,N):
        if TD[j][0] not in tset:
            tset.add(TD[j][0])
            tlist.append(TD[j][0])
            ans += TD[j][1] - TD[i][1]
            ans += 2*len(tlist) - 1
            i += 1
    #output
    print(ans)
