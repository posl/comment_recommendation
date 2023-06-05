def solve(n, m, a):
    ans = 0
    for i in range(1, m + 1):
        flag = True
        for j in range(n):
            if i not in a[j]:
                flag = False
        if flag:
            ans += 1
    return ans
