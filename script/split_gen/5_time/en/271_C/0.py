def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(n):
        if a[i] <= ans:
            ans += a[i]
        else:
            break
    print(ans)
