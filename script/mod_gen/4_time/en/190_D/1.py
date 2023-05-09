def solve(n):
    if n == 1:
        return 2
    ans = 1
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 1:
                ans += 1
            if i != n // i and (n // i) % 2 == 1:
                ans += 1
    return ans
n = int(input())
print(solve(n))

if __name__ == '__main__':
    solve()