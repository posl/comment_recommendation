def solve():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 1:
                return ans
        for i in range(N):
            a[i] //= 2
        ans += 1
