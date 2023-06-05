def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N+1):
        if a % K == 0:
            ans += N // K
        else:
            ans += N // K + 1
    if K % 2 == 0:
        for a in range(1, N+1):
            if a % K == K // 2:
                ans += N // K
    print(ans)
