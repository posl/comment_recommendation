def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**18
    for i in range(N-K+1):
        ans = min(ans, x[i+K-1] - x[i] + min(abs(x[i]), abs(x[i+K-1])))
    print(ans)
