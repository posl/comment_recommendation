def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(N-K+1):
        if x[i]*x[i+K-1] > 0:
            ans = min(ans, max(abs(x[i]), abs(x[i+K-1])))
        else:
            ans = min(ans, abs(x[i])+abs(x[i+K-1])+min(abs(x[i]), abs(x[i+K-1])))
    print(ans)
