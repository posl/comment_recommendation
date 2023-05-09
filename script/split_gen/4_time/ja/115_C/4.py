def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = h[K-1] - h[0]
    for i in range(1, N-K+1):
        ans = min(ans, h[K-1+i] - h[i])
    print(ans)
