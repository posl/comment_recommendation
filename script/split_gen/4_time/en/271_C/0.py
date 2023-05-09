def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        if a[0] == 1:
            print(1)
        else:
            print(0)
        return
    a.sort()
    if a[0] != 1:
        print(0)
        return
    ans = 1
    for i in range(1, n):
        ans *= a[i]
        if ans > 10 ** 18:
            print(-1)
            return
    print(ans)
