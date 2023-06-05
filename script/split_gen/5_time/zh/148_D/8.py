def solve():
    N = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(1, N):
        if a[i] == a[i - 1] + 1:
            ans += 1
        elif a[i] <= a[i - 1]:
            ans += a[i]
        else:
            print(-1)
            return
    print(ans)
