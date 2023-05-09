def solve(n):
    ans = 0
    for i in range(1,n+1):
        ans += (n-1)//i
    return ans
n = int(input())
print(solve(n))

if __name__ == '__main__':
    solve()