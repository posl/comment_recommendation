def main():
    # N,K = map(int,input().split())
    # H = list(map(int,input().split()))
    # H.sort()
    # H.reverse()
    # print(sum(H[K:]))
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort()
    H.reverse()
    ans = 0
    for i in range(K,N):
        ans += H[i]
    print(ans)
main()
