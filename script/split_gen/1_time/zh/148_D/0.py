def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
        return
    if n == 2:
        if a[0] == 1 and a[1] == 2:
            print(0)
        else:
            print(-1)
        return
    if a[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(1, n):
        if a[i] != a[i - 1] + 1:
            ans += 1
    print(ans)
