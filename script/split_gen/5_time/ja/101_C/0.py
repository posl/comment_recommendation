def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    while N > K:
        N -= (K - 1)
        ans += 1
    print(ans + 1)
