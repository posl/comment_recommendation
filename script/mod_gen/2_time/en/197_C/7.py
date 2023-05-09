def solve(n, a):
    a = sorted(a)
    ans = 0
    for i in range(n-1):
        ans |= a[i]
        if a[i+1] > ans:
            return ans
    return ans | a[-1]
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

if __name__ == '__main__':
    solve()