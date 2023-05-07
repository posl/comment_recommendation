def main():
    N, K = map(int, input().split())
    h = [int(input()) for i in range(N)]
    h.sort()
    ans = h[N-1] - h[0]
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1]-h[i])
    print(ans)
