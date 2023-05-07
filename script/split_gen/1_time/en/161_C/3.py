def main():
    N, K = map(int, input().split())
    ans = N % K
    print(min(ans, K - ans))
