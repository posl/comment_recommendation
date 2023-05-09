def solve():
    A, B = map(int, input().split())
    ans = 0
    while B > 1:
        B -= A - 1
        ans += 1
    print(ans)
