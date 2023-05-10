def main():
    N,K = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(N-K+1):
        if x[i] <= 0 and x[i+K-1] <= 0:
            tmp = abs(x[i])
        elif x[i] <= 0 and x[i+K-1] > 0:
            tmp = abs(x[i])*2 + x[i+K-1]
        else:
            tmp = x[i+K-1]
        ans = min(ans,tmp)
    print(ans)
