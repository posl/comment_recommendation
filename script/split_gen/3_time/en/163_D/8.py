def main():
    #input
    N, K = map(int, input().split())
    #compute
    ans = 0
    for i in range(K, N+2):
        ans += (N+1)*i - i*(i-1)//2
    #output
    print(ans%(10**9+7))
