def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        ans += (N // a) * max(0, (a - K + 1))
        if a >= K:
            ans += max(0, (N % a) - K + 1)
    print(ans)
