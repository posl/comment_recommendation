def main():
    # input
    N, K = map(int, input().split())
    # compute
    ans = 0
    for a in range(1, N+1):
        if a % K == 0:
            ans += N
        else:
            tmp = N // K
            if (a + K//2) % K == 0:
                ans += tmp**3
            else:
                ans += tmp**3 * 2
    # output
    print(ans)
