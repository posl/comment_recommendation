def dfs(n, m, x, c, a, i, money, sum):
    if i == n:
        if sum >= x:
            return money
        else:
            return -1
    money1 = dfs(n, m, x, c, a, i + 1, money, sum)
    money2 = dfs(n, m, x, c, a, i + 1, money + c[i], sum + a[i])
    if money1 == -1:
        return money2
    elif money2 == -1:
        return money1
    else:
        return min(money1, money2)
