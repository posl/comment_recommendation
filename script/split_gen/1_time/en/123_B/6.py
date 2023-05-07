def solve():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = 0
    ans += ((a + 9) // 10) * 10
    ans += ((b + 9) // 10) * 10
    ans += ((c + 9) // 10) * 10
    ans += ((d + 9) // 10) * 10
    ans += ((e + 9) // 10) * 10
    ans -= max(a % 10, b % 10, c % 10, d % 10, e % 10)
    print(ans)
solve()
