def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        ans += (N // a) * max(0, (a - K))
        ans += max(0, (N % a) - max(0, (K - 1)))
    print(ans)
