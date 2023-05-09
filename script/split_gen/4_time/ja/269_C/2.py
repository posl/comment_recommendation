def solve(n):
    if n == 0:
        print(0)
        return
    ans = []
    for i in range(60):
        if n & (1 << i):
            ans.append(i)
    for i in range(len(ans)):
        print(1 << ans[i])
    return
