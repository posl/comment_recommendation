def solve():
    #a, n = map(int, input().split())
    a, n = 3, 72
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
        else:
            n -= 1
        ans += 1
    print(ans)
