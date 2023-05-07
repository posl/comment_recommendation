def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    s = 0
    for i in range(K):
        s += (p[i] + 1) / 2
    ans = s
    for i in range(K, N):
        s += (p[i] + 1) / 2 - (p[i - K] + 1) / 2
        ans = max(ans, s)
    print(ans)
