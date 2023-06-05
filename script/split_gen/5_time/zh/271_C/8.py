def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        if a[0] == 1:
            print(0)
        else:
            print(1)
        return
    ans = 0
    if a[0] == 1:
        ans += 1
        for i in range(1, n):
            if a[i] == a[i - 1] + 1:
                ans += 1
            else:
                break
        print(n - ans)
    else:
        print(n - 1)
solve()
