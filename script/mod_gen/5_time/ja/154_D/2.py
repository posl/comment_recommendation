def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        ans += (p[i]+1)*K/2
    tmp = ans
    for i in range(N-K):
        tmp -= (p[i]+1)*K/2
        tmp += (p[i+K]+1)*K/2
        ans = max(ans, tmp)
    print(ans)
main()
