def main():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(N-K+1):
        tmp = sum(p[i:i+K])
        if ans < tmp:
            ans = tmp
    print(ans+(K-1)/2)

if __name__ == '__main__':
    main()