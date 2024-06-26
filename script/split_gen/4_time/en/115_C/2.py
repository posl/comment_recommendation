def main():
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    H.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, H[i+K-1] - H[i])
    print(ans)
