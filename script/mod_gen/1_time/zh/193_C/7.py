def solve():
    n = int(input())
    ans = n
    i = 2
    while i * i <= n:
        j = 2
        while i ** j <= n:
            ans -= 1
            j += 1
        i += 1
    print(ans)
solve()
