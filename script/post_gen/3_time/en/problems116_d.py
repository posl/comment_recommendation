Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    t_set = set()
    d_sum = 0
    for i in range(K):
        t, d = sushi[i]
        t_set.add(t)
        d_sum += d
        ans = max(ans, d_sum + len(t_set)**2)
    for i in range(K, N):
        t, d = sushi[i]
        if t in t_set:
            continue
        t_set.add(t)
        d_sum += d
        d_sum -= sushi[K-1][1]
        K -= 1
        ans = max(ans, d_sum + len(t_set)**2)
    print(ans)

main()

The following code is the solution for the problem "D - Grid Components" on AtCoder.

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    Sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        Sushi.append([t, d])
    Sushi.sort(key = lambda x: x[1], reverse = True)
    #print(Sushi)
    Sushi_t = [x[0] for x in Sushi]
    Sushi_d = [x[1] for x in Sushi]
    #print(Sushi_t)
    #print(Sushi_d)
    Sushi_t_unique = list(set(Sushi_t))
    #print(Sushi_t_unique)
    Sushi_t_unique.sort()
    #print(Sushi_t_unique)
    Sushi_t_unique_count = [0] * len(Sushi_t_unique)
    #print(Sushi_t_unique_count)
    for i in range(len(Sushi_t_unique)):
        Sushi_t_unique_count[i] = Sushi_t.count(Sushi_t_unique[i])
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.sort(reverse = True)
    #print(Sushi_t_unique_count)
    if K >= len(Sushi_t_unique):
        print(sum(Sushi_d))
        return
    if K == 1:
        print(max(Sushi_d))
        return
    Sushi_t_unique_count = Sushi_t_unique_count[:K]
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.sort(reverse = True)
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count = Sushi_t_unique_count[1:]
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.append(K - len(Sushi_t_unique_count))
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.sort(reverse = True)
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count = Sushi_t_unique_count[:K]
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.sort(reverse = True)
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count = Sushi_t_unique_count[1:]
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.append(K - len(Sushi_t_unique_count))
    #print(Sushi_t_unique_count)
    Sushi_t_unique_count.sort(reverse = True)
    #print(Sushi_t_unique_count)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((d, t))
    sushi.sort(reverse=True)
    sushi_set = set()
    ans = 0
    for i in range(K):
        ans += sushi[i][0]
        sushi_set.add(sushi[i][1])
    ans += len(sushi_set)**2
    for i in range(K, N):
        if sushi[i][1] in sushi_set:
            continue
        for j in range(K):
            if sushi[j][1] not in sushi_set:
                continue
            sushi_set.remove(sushi[j][1])
            sushi_set.add(sushi[i][1])
            ans = max(ans, ans - sushi[j][0] + sushi[i][0] + len(sushi_set)**2)
            break
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    T = []
    for i in range(N):
        t, d = map(int, input().split())
        T.append((d, t))
    T.sort(reverse=True)
    S = set()
    S.add(T[0][1])
    ans = T[0][0]
    for i in range(1, K):
        ans += T[i][0]
        S.add(T[i][1])
    ans += len(S) * len(S)
    for i in range(K, N):
        if T[i][1] in S:
            continue
        tmp = ans
        tmp -= T[K-1][0]
        tmp += T[i][0]
        tmp -= len(S) * len(S)
        tmp += (len(S) + 1) * (len(S) + 1)
        if tmp > ans:
            ans = tmp
            S.add(T[i][1])
        else:
            break
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    Sushi = []
    for i in range(N):
        Sushi.append(list(map(int, input().split())))
    Sushi.sort(key=lambda x:x[1], reverse=True)
    Topping = [0]*(N+1)
    Topping[Sushi[0][0]] += 1
    ToppingNum = 1
    ToppingSum = Sushi[0][1]
    SushiEat = [Sushi[0][1]]
    for i in range(1, N):
        if Topping[Sushi[i][0]] == 0:
            Topping[Sushi[i][0]] += 1
            ToppingNum += 1
            ToppingSum += Sushi[i][1]
            SushiEat.append(Sushi[i][1])
        else:
            Topping[Sushi[i][0]] += 1
            ToppingSum += Sushi[i][1]
            SushiEat.append(Sushi[i][1])
        if ToppingNum == K:
            break
    ans = ToppingSum + ToppingNum**2
    for i in range(K, N):
        if Topping[Sushi[i][0]] == 0:
            Topping[Sushi[i][0]] += 1
            ToppingNum += 1
            ToppingSum += Sushi[i][1]
            SushiEat.append(Sushi[i][1])
            ToppingSum -= SushiEat[0]
            SushiEat.pop(0)
            while Topping[SushiEat[0]] > 1:
                ToppingSum -= SushiEat[0]
                Topping[SushiEat[0]] -= 1
                SushiEat.pop(0)
            ans = max(ans, ToppingSum + ToppingNum**2)
        else:
            Topping[Sushi[i][0]] += 1
            ToppingSum += Sushi[i][1]
            SushiEat.append(Sushi[i][1])
            ToppingSum -= SushiEat[0]
            SushiEat.pop(0)
            while Topping[SushiEat[0]] > 1:
                ToppingSum -= SushiEat[0]
                Topping[SushiEat[0]] -= 1
                SushiEat.pop(0)
            ans = max(ans, ToppingSum + T

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    Sushi = [tuple(map(int, input().split())) for _ in range(N)]
    Sushi.sort(key=lambda x: x[1], reverse=True)
    T = set([s[0] for s in Sushi[:K]])
    S = sum([s[1] for s in Sushi[:K]])
    ans = S + len(T) ** 2
    for i in range(K, N):
        if len(T) == K:
            break
        if Sushi[i][0] in T:
            continue
        T.add(Sushi[i][0])
        S -= Sushi[i-K][1]
        S += Sushi[i][1]
        ans = max(ans, S + len(T) ** 2)
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(N)]
    S.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(K):
        ans += S[i][1]
    ans += K**2
    cnt = K
    kind = set()
    for i in range(K):
        kind.add(S[i][0])
    for i in range(K, N):
        if S[i][0] not in kind:
            if cnt >= K:
                continue
            cnt += 1
            kind.add(S[i][0])
            ans += S[i][1] - S[K - 1][1]
            ans += 2 * cnt - K - 1
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(n)]
    sushi.sort(key=lambda x: x[1], reverse=True)

    kind = set()
    ans = 0
    tmp = 0
    for i in range(k):
        ans += sushi[i][1]
        kind.add(sushi[i][0])
        tmp += 1
    ans += tmp * tmp

    for i in range(k, n):
        if sushi[i][0] not in kind:
            for j in range(k):
                if sushi[j][0] not in kind:
                    if sushi[j][1] < sushi[i][1]:
                        kind.remove(sushi[j][0])
                        kind.add(sushi[i][0])
                        ans = ans - sushi[j][1] + sushi[i][1] + 2 * tmp - 1
                        sushi[j][1] = sushi[i][1]
                        break

    print(ans)

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    sushi = [tuple(map(int,input().split())) for _ in range(N)]
    sushi.sort(key=lambda x:x[1],reverse=True)
    #print(sushi)
    ans = 0
    for i in range(K):
        ans += sushi[i][1]
    #print(ans)
    kinds = set()
    for i in range(K):
        kinds.add(sushi[i][0])
    #print(kinds)
    if len(kinds) == K:
        print(ans + len(kinds)**2)
    else:
        for i in range(K,N):
            if len(kinds) == K:
                break
            if sushi[i][0] not in kinds:
                kinds.add(sushi[i][0])
                ans += sushi[i][1]
        print(ans + len(kinds)**2)

=======
Suggestion 10

def main():
    #read input
    n,k = map(int,input().split())
    td = [list(map(int,input().split())) for i in range(n)]
    #sort by deliciousness
    td.sort(key=lambda x:x[1],reverse=True)
    #use set to count variety
    kind = set()
    #use heap to store the "deliciousness" of pieces you eat
    h = []
    #base total deliciousness
    total = 0
    for i in range(k):
        total += td[i][1]
        kind.add(td[i][0])
        heapq.heappush(h,td[i][1])
    #calculate satisfaction
    ans = total + len(kind)*len(kind)
    for i in range(k,n):
        #if the kind of topping is new
        if td[i][0] not in kind:
            #update total deliciousness
            total += td[i][1] - heapq.heappop(h)
            #update variety
            kind.add(td[i][0])
            #update satisfaction
            ans = max(ans,total+len(kind)*len(kind))
    print(ans)
