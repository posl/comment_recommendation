def solve():
    N = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        exit()
    ans = 0
    for i in range(N - 1):
        if a[i + 1] - a[i] > 1:
            print(-1)
            exit()
        if a[i + 1] - a[i] == 1:
            ans += 1
        else:
            ans += a[i + 1]
    print(ans)
