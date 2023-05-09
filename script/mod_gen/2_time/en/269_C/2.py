def solve(n):
    if n == 0:
        print(0)
        return
    ans = []
    for i in range(60):
        if n >> i & 1:
            ans.append(i)
    for i in range(2**len(ans)):
        tmp = 0
        for j in range(len(ans)):
            if i >> j & 1:
                tmp += 1 << ans[j]
        print(tmp)

if __name__ == '__main__':
    solve()