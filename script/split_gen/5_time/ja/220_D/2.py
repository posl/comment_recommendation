def calc(n):
    ans = []
    for i in range(10):
        ans.append(0)
    ans[n%10] = 1
    return ans
