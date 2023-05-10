def solve():
    n = int(input())
    ans = 0
    while n > 0:
        ans += 1
        n //= 2
    print(ans)

if __name__ == '__main__':
    solve()