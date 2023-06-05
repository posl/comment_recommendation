def solve():
    n = int(input())
    ans = 0
    for i in range(n):
        if (n-i) % 2 == 0:
            ans += 1
    print(ans)
