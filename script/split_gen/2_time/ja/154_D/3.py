def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(N):
        tmp += (p[i]+1)/2
        if i >= K:
            tmp -= (p[i-K]+1)/2
        ans = max(ans, tmp)
    print(ans)
