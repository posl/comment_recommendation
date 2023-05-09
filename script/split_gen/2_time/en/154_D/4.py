def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [i * (i + 1) / 2 / i for i in p]
    ans = sum(p[:K])
    tmp = ans
    for i in range(K, N):
        tmp += p[i] - p[i - K]
        ans = max(ans, tmp)
    print(ans)
