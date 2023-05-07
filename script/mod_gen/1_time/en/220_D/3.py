def solve(n, a):
    ans = [0] * 10
    ans[a[0]] = 1
    for i in range(1, n):
        nxt = [0] * 10
        for j in range(10):
            nxt[(j + a[i]) % 10] += ans[j]
            nxt[(j * a[i]) % 10] += ans[j]
        ans = nxt
    return ans
n = int(input())
a = list(map(int, input().split()))
ans = solve(n, a)
print(*ans, sep='\n')

if __name__ == '__main__':
    solve()