def solve(n):
    ans = 0
    for i in range(1, len(str(n))):
        a = int(str(n)[:i])
        b = int(str(n)[i:])
        ans = max(ans, a * b)
    return ans
n = int(input())
print(solve(n))

if __name__ == '__main__':
    solve()