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
    from collections import defaultdict
    from heapq import heappush, heappop
    kinds = defaultdict(list)
    for t, d in sushi:
        kinds[t].append(d)
    kinds = sorted(kinds.items(), key=lambda x: -x[1][0])
    kinds = [(t, d[0]) for t, d in kinds]
    kind = 0
    heap = []
    for i in range(K):
        t, d = sushi[i]
        if kinds[kind][0] == t:
            pass
        else:
            heappush(heap, -d)
    ans = sum([d for t, d in sushi[:K]]) + len(kinds)**2
    for i in range(K, N):
        t, d = sushi[i]
        if kinds[kind][0] == t:
            continue
        else:
            if heap:
                min_d = -heappop(heap)
                ans = max(ans, sum([d for t, d in sushi[:K]]) + len(kinds)**2 - min_d + d)
                kind += 1
            else:
                break
    return ans

print(solve())

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    sushi = []
    for _ in range(n):
        sushi.append(list(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    print(sushi)

main()

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    sushi = []
    for i in range(n):
        sushi.append(list(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    used = []
    ans = 0
    for i in range(k):
        t, d = sushi.pop()
        ans += d
        if t not in used:
            used.append(t)
    ans += len(used) ** 2
    while len(used) < k and len(sushi) > 0:
        t, d = sushi.pop()
        if t not in used:
            ans += d
            used.append(t)
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        sushi.append(tuple(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    kinds = set()
    base = 0
    for i in range(K):
        base += sushi[i][1]
        kinds.add(sushi[i][0])
    ans = base + len(kinds)**2
    for i in range(K, N):
        if sushi[i][0] in kinds:
            continue
        base += sushi[i][1] - sushi[K-1][1]
        kinds.add(sushi[i][0])
        ans = max(ans, base + len(kinds)**2)
    print(ans)

main()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        sushi.append(tuple(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)

    kind = {}
    for i in range(K):
        if sushi[i][0] in kind:
            kind[sushi[i][0]] += 1
        else:
            kind[sushi[i][0]] = 1
    #print(kind)

    variety = len(kind.keys())
    #print(variety)

    base = sum([x[1] for x in sushi[:K]])
    #print(base)

    ans = base + variety**2
    #print(ans)

    for i in range(K, N):
        if sushi[i][0] in kind:
            continue
        else:
            if variety == 1:
                continue
            else:
                base = base - sushi[i-K][1] + sushi[i][1]
                variety += 1
                ans = max(ans, base + variety**2)
    print(ans)

=======
Suggestion 6

def problem():
    N, K = map(int, input().split())
    T = []
    D = []
    for i in range(N):
        t, d = map(int, input().split())
        T.append(t)
        D.append(d)
    #print(N, K)
    #print(T)
    #print(D)
    T2 = []
    D2 = []
    for i in range(K):
        t = T[i]
        d = D[i]
        T2.append(t)
        D2.append(d)
    #print(T2)
    #print(D2)
    S = 0
    for i in range(K):
        S += D2[i]
    #print(S)
    V = len(set(T2))
    #print(V)
    ans = S + V*V
    #print(ans)
    for i in range(K, N):
        t = T[i]
        d = D[i]
        if t in T2:
            continue
        for j in range(K):
            t2 = T2[j]
            d2 = D2[j]
            if d2 <= d:
                T2[j] = t
                D2[j] = d
                S = S - d2 + d
                V = len(set(T2))
                ans = max(ans, S + V*V)
                break
    print(ans)

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    sushi = [tuple(map(int, input().split())) for _ in range(N)]

    sushi.sort(key=lambda x: x[1], reverse=True)

    from collections import defaultdict
    kind = defaultdict(int)
    kind_list = []
    for t, d in sushi[:K]:
        kind[t] += 1
        if kind[t] == 1:
            kind_list.append(t)

    kind_list.sort()
    kind_list.reverse()

    ans = sum([d for t, d in sushi[:K]]) + len(kind_list)**2

    for i in range(K, N):
        t, d = sushi[i]
        if t in kind:
            continue
        if not kind_list:
            break
        kind[t] += 1
        kind_list.append(t)
        kind_list.sort()
        kind_list.reverse()
        kind_list.pop()
        ans = max(ans, sum([d for t, d in sushi[:i+1]]) + len(kind_list)**2)

    print(ans)

=======
Suggestion 8

def solve(N, K, sushi):
    # sort by deliciousness
    sushi.sort(key=lambda x: x[1], reverse=True)
    # sort by type
    sushi.sort(key=lambda x: x[0])
    # print(sushi)

    # pick up the top K sushi
    picked = sushi[:K]
    # print(picked)

    # count the number of types
    types = {}
    for t, d in picked:
        if t in types:
            types[t] += 1
        else:
            types[t] = 1
    # print(types)

    # calculate the satisfaction
    satisfaction = 0
    for t, d in picked:
        satisfaction += d
    satisfaction += len(types) ** 2
    # print(satisfaction)

    # calculate the maximum satisfaction
    max_satisfaction = satisfaction
    for i in range(K, N):
        # print("i:", i)
        # print("picked:", picked)
        # print("types:", types)

        # pick up the next sushi
        t, d = sushi[i]
        # print("next sushi:", t, d)

        # remove the last sushi
        t_last, d_last = picked.pop()
        # print("last sushi:", t_last, d_last)
        satisfaction -= d_last
        types[t_last] -= 1
        if types[t_last] == 0:
            types.pop(t_last)
        satisfaction -= len(types) ** 2
        # print("satisfaction:", satisfaction)

        # add the next sushi
        picked.append((t, d))
        satisfaction += d
        if t in types:
            types[t] += 1
        else:
            types[t] = 1
        satisfaction += len(types) ** 2
        # print("satisfaction:", satisfaction)

        # update the maximum satisfaction
        max_satisfaction = max(max_satisfaction, satisfaction)
        # print("max_satisfaction:", max_satisfaction)

    return max_satisfaction

=======
Suggestion 9

def solve(N, K, sushi):
    sushi.sort(key=lambda x: x[1], reverse=True)
    eaten = []
    eaten_type = set()
    for i in range(K):
        eaten.append(sushi[i])
        eaten_type.add(sushi[i][0])
    eaten.sort(key=lambda x: x[0])
    result = sum([x[1] for x in eaten]) + len(eaten_type)**2
    for i in range(K, N):
        if sushi[i][0] not in eaten_type:
            eaten.append(sushi[i])
            eaten_type.add(sushi[i][0])
            eaten.sort(key=lambda x: x[0])
            result = max(result, sum([x[1] for x in eaten]) + len(eaten_type)**2)
    return result

=======
Suggestion 10

def get_max_satisfaction(N, K, sushi):
    # sort sushi by deliciousness
    sushi.sort(key=lambda x: x[1], reverse=True)

    # get the number of each type of sushi
    sushi_count = {}
    for i in range(N):
        if sushi[i][0] not in sushi_count:
            sushi_count[sushi[i][0]] = 1
        else:
            sushi_count[sushi[i][0]] += 1

    # get the number of each type of sushi in the top K sushi
    sushi_count_top = {}
    for i in range(K):
        if sushi[i][0] not in sushi_count_top:
            sushi_count_top[sushi[i][0]] = 1
        else:
            sushi_count_top[sushi[i][0]] += 1

    # get the number of each type of sushi in the top K sushi
    # and not in the top K sushi
    sushi_count_top_and_not = {}
    sushi_count_not_top = {}
    for i in range(N):
        if i < K:
            if sushi[i][0] not in sushi_count_top_and_not:
                sushi_count_top_and_not[sushi[i][0]] = 1
            else:
                sushi_count_top_and_not[sushi[i][0]] += 1
        else:
            if sushi[i][0] not in sushi_count_not_top:
                sushi_count_not_top[sushi[i][0]] = 1
            else:
                sushi_count_not_top[sushi[i][0]] += 1

    # get the number of each type of sushi in the top K sushi
    # and not in the top K sushi
    # and in the top K sushi and not in the top K sushi
    sushi_count_top_and_not_and_not_top = {}
    for i in range(N):
        if i < K:
            if sushi[i][0] not in sushi_count_top_and_not_and_not_top:
                sushi_count_top_and_not_and_not_top[sushi[i][0]] = 1
            else:
                sushi_count_top_and_not_and_not_top[sushi[i][0]] += 1
        else:
            if sushi[i][0] not in sushi_count_top_and_not_and_not_top:
                sushi_count_top_and_not_and_not_top[sushi[i][0]] = 0

    # get the number of each type of sushi in the
