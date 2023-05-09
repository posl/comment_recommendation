def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        ans += (N//i)*(i//K)
        if i%K == 0:
            ans += 1
        ans += max(0, N%i-K+1)
    print(ans)
