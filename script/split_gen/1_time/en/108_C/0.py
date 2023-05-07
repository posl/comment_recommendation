def main():
    N, K = map(int, input().split())
    ans = 0
    if K % 2 == 0:
        for i in range(1, N+1):
            if i % K == 0:
                ans += 1
        ans = ans ** 3
    else:
        for i in range(1, N+1):
            if i % K == 0:
                ans += 1
        ans = ans ** 3
        for i in range(1, N+1):
            if (i + K // 2) % K == 0:
                ans += 1
        ans = ans ** 3
    print(ans)
