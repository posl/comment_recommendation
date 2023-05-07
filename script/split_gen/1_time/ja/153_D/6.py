def solve():
    H = int(input())
    ans = 0
    while H > 0:
        ans += H
        H //= 2
    print(ans)
    return 0
