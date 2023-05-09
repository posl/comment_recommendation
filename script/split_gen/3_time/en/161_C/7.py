def main():
    N, K = map(int, input().split())
    ans = min(N % K, K - N % K)
    print(ans)
