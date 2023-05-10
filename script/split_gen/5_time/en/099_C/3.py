def solve():
    N = int(input())
    ans = N
    for i in range(N+1):
        cnt = 0
        tmp = i
        while tmp > 0:
            cnt += tmp % 6
            tmp //= 6
        tmp = N - i
        while tmp > 0:
            cnt += tmp % 9
            tmp //= 9
        ans = min(ans, cnt)
    print(ans)
