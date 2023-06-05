def problem210_c():
    #输入
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    #解法
    ans = 0
    dic = {}
    for i in range(n):
        dic[c[i]] = dic.get(c[i], 0) + 1
        if i >= k:
            dic[c[i - k]] -= 1
            if dic[c[i - k]] == 0:
                del dic[c[i - k]]
        ans = max(ans, len(dic))
    #输出
    print(ans)
