def solve():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 1:
                print(ans)
                return
            else:
                a[i] //= 2
        ans += 1
