def solve():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += h[i]
        elif h[i] > h[i-1]:
            ans += h[i] - h[i-1]
    print(ans)
