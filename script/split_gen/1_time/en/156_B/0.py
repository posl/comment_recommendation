def main():
    # input
    N, K = map(int, input().split())
    # compute
    ans = 0
    while N > 0:
        N //= K
        ans += 1
    # output
    print(ans)
