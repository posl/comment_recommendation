def solve():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        if a[i] <= ans + 1:
            ans += a[i]
        else:
            break
    print(ans + 1)
