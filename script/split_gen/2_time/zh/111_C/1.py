def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            if a[i] == a[0]:
                ans += 1
        else:
            if a[i] == a[1]:
                ans += 1
    print(ans)
