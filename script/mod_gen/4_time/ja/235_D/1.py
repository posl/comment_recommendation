def solve():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
            ans += 1
        elif n % 10 == 1:
            n //= 10
            ans += 1
        else:
            print(-1)
            return
    print(ans+1)

if __name__ == '__main__':
    solve()