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
