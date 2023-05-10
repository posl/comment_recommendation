def main():
    N, K = map(int, input().split())
    #print(N, K)
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1/N
        else:
            cnt = 0
            while i < K:
                i = i * 2
                cnt += 1
            ans += (1/N) * (1/(2**cnt))
    print(ans)
