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
