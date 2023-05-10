def solve(n, s, t):
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[i] = t[i]
            continue
        ans[i] = min((ans[i-1] + s[i-1]) % t[i], t[i])
    return ans
n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = solve(n, s, t)
print(*ans, sep='\n')

if __name__ == '__main__':
    solve()