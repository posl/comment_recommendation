def main():
    # input
    N, M = map(int, input().split())
    # compute
    ans = N * (N - 1) // 2
    ans += M * (M - 1) // 2
    # output
    print(ans)
