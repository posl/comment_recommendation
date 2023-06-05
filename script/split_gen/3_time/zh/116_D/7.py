def solve():
    n, k = map(int, input().split())
    td = [list(map(int, input().split())) for _ in range(n)]
    td.sort(key=lambda x: x[1], reverse=True)
    t = [0] * n
    d = [0] * n
    for i in range(n):
        t[i] = td[i][0]
        d[i] = td[i][1]
    from collections import defaultdict
    dic = defaultdict(list)
    for i in range(n):
        dic[t[i]].append(d[i])
    dic = sorted(dic.items(), key=lambda x: x[0])
    # print(dic)
    ans = 0
    for i in range(k):
        ans += d[i]
    # print(ans)
    cnt = 0
    for i in range(k):
        if len(dic[t[i]]) > 1:
            cnt += 1
    # print(cnt)
    if cnt == 0:
        print(ans)
        exit()
    for i in range(k, n):
        if len(dic[t[i]]) > 1:
            for j in range(len(dic[t[i]]) - 1):
                if cnt == 0:
                    print(ans)
                    exit()
                ans += dic[t[i]][j]
                cnt -= 1
    print(ans)
