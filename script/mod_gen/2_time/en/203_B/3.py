def main():
    # input
    N, K = map(int, input().split())
    # compute
    ans = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            ans += 100*i + j
    # output
    print(ans)

if __name__ == '__main__':
    main()