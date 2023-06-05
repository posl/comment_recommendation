def dfs(a,b,k):
    if a == 0:
        return 'b'*b
    if b == 0:
        return 'a'*a
    #计算以a开头的字符串的数量
    cnt = 0
    for i in range(a+1):
        cnt += comb(a+b-i-1, b)
        if cnt >= k:
            return 'a'*i + 'b' + dfs(a-i, b-1, k-cnt+comb(a+b-i-1, b))
