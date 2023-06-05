def solve(n, a):
    # print(n, a)
    ans = [0] * 10
    for i in range(10):
        ans[i] = a.count(i)
    # print(ans)
    for i in range(n - 1):
        tmp = [0] * 10
        for j in range(10):
            tmp[(j + a[i]) % 10] += ans[j]
            tmp[(j * a[i]) % 10] += ans[j]
        ans = tmp
        # print(ans)
    return ans

if __name__ == '__main__':
    solve()