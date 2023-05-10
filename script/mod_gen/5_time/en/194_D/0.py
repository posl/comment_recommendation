def solve(n):
    ans = 0
    for i in range(1,n):
        ans += n/i
    return ans
n = int(input())
print(solve(n))

if __name__ == '__main__':
    solve()