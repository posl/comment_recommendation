def solution():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(n * (n - 1) // 2 - ans)
