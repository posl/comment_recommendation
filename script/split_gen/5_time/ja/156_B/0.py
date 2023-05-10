def main():
    N, K = map(int, input().split())
    ans = 0
    while N >= K:
        ans += 1
        N = N // K
    ans += 1
    print(ans)
