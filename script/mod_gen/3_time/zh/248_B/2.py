def solve(a, b, k):
    ans = 0
    while a < b:
        a *= k
        ans += 1
    return ans

if __name__ == '__main__':
    solve()