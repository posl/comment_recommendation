def main():
    #input
    N, K = map(int, input().split())
    #compute
    ans = 0
    for i in range(K, N+2):
        ans += i*(N-i+1)+1
    #output
    print(ans%(10**9+7))
