Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append([t, d])
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    ans = 0
    t = set()
    s = 0
    for i in range(K):
        s += sushi[i][1]
        t.add(sushi[i][0])
        ans = max(ans, s + len(t) ** 2)
    #print(s, len(t), ans)
    for i in range(K, N):
        if sushi[i][0] in t:
            continue
        t.add(sushi[i][0])
        t.remove(sushi[i - len(t) + 1][0])
        s += sushi[i][1] - sushi[i - len(t) + 1][1]
        ans = max(ans, s + len(t) ** 2)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))

    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi = sushi[:K]

    ans = 0
    ans += sum([s[1] for s in sushi])
    ans += len(set([s[0] for s in sushi])) ** 2

    types = [s[0] for s in sushi]
    for s in sushi:
        if types.count(s[0]) > 1:
            types.remove(s[0])
            continue
        for s2 in sushi:
            if s[0] == s2[0]:
                continue
            if len(types) == K:
                break
            if types.count(s2[0]) == 0:
                types.append(s2[0])
                ans += s2[1]
                break

    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    D = []
    for _ in range(N):
        t, d = map(int, input().split())
        D.append((d, t))
    D.sort(reverse=True)
    #print(D)

    ans = 0
    cnt = 0
    S = set()
    for d, t in D[:K]:
        ans += d
        if t not in S:
            cnt += 1
            S.add(t)
    ans += cnt * cnt
    #print(ans)

    for d, t in D[K:]:
        if t in S:
            continue
        S.add(t)
        cnt += 1
        ans += d
        ans += 2 * cnt - 1
        #print(d, cnt, ans)

    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    types = set()
    types.add(sushi[0][0])
    s = sushi[0][1]
    l = 0
    r = 0
    ans = s + len(types) ** 2
    while r < N - 1:
        r += 1
        types.add(sushi[r][0])
        s += sushi[r][1]
        while len(types) > K:
            types.remove(sushi[l][0])
            s -= sushi[l][1]
            l += 1
        ans = max(ans, s + len(types) ** 2)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    sushi = [tuple(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    kind = set()
    point = 0
    for i in range(K):
        kind.add(sushi[i][0])
        point += sushi[i][1]
    ans = point + len(kind) ** 2
    for i in range(K, N):
        if sushi[i][0] in kind:
            continue
        kind.add(sushi[i][0])
        point += sushi[i][1]
        point -= sushi[i-K][1]
        ans = max(ans, point + len(kind) ** 2)
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    t = set()
    t_add = t.add
    t_discard = t.discard
    t_len = len
    t_clear = t.clear
    ans = 0
    for i in range(N):
        t_add(sushi[i][0])
        if t_len(t) >= K:
            ans = max(ans, sum([sushi[j][1] for j in range(i-K+1, i+1)]) + t_len(t)**2)
            t_clear()
            for j in range(i-K+1, i+1):
                t_add(sushi[j][0])
            if t_len(t) >= K:
                ans = max(ans, sum([sushi[j][1] for j in range(i-K+1, i+1)]) + t_len(t)**2)
            t_discard(sushi[i-K+1][0])
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for i in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    t = [0] * (N + 1)
    ans = 0
    for i in range(K):
        t[sushi[i][0]] += 1
        ans += sushi[i][1]
    cnt = 0
    for i in range(1, N + 1):
        if t[i] > 0:
            cnt += 1
    ans += cnt * cnt
    for i in range(K, N):
        if t[sushi[i][0]] == 0:
            for j in range(1, N + 1):
                if t[j] > 0:
                    t[j] -= 1
                    break
            t[sushi[i][0]] += 1
            cnt += 1
            ans = ans - cnt * cnt + (cnt + 1) * (cnt + 1)
    print(ans)

=======
Suggestion 8

def main():
    from sys import stdin
    input = stdin.readline
    N, K = map(int, input().split())
    td = [list(map(int, input().split())) for _ in range(N)]
    td.sort(key=lambda x:x[1], reverse=True)
    ans = 0
    cnt = [0]*(N+1)
    kind = 0
    for i in range(K):
        t, d = td[i]
        ans += d
        cnt[t] += 1
        if cnt[t] == 1:
            kind += 1
    ans += kind**2
    for i in range(K, N):
        t, d = td[i]
        if cnt[t] == 0:
            if kind == K:
                break
            ans += d
            cnt[t] += 1
            kind += 1
            ans += 2*kind-1
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    data.sort(key=lambda x: x[1], reverse=True)

    kinds = set()
    kinds.add(data[0][0])
    ret = data[0][1]
    for i in range(1, K):
        if data[i][0] in kinds:
            ret += data[i][1]
        else:
            kinds.add(data[i][0])
            ret += data[i][1] + len(kinds) * len(kinds)

    for i in range(K, N):
        if data[i][0] in kinds:
            ret = max(ret, data[i][1] + sum(map(lambda x: x[1], filter(lambda x: x[0] in kinds, data[:i]))) + len(kinds) * len(kinds))
        else:
            ret = max(ret, data[i][1] + sum(map(lambda x: x[1], filter(lambda x: x[0] in kinds, data[:i]))) + (len(kinds) + 1) * (len(kinds) + 1))

    print(ret)
