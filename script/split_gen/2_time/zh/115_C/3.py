def main():
    N,K = map(int,input().split())
    h = [int(input()) for i in range(N)]
    h.sort()
    ans = h[K-1]-h[0]
    for i in range(1,N-K+1):
        if ans > h[i+K-1]-h[i]:
            ans = h[i+K-1]-h[i]
    print(ans)
