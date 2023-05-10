def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    s = 0
    d = {0:1}
    for i in range(N):
        s += A[i]
        if s - K in d:
            ans += d[s - K]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print(ans)
