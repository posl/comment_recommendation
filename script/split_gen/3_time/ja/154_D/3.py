def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        if i == 0:
            tmp = sum([(p[j]+1)/2 for j in range(K)])
        else:
            tmp = tmp - (p[i-1]+1)/2 + (p[i+K-1]+1)/2
        ans = max(ans, tmp)
    print(ans)
