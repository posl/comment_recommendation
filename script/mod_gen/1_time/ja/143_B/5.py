def main():
    # input
    N = int(input())
    ds = list(map(int, input().split()))
    # compute
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += ds[i] * ds[j]
    # output
    print(ans)

if __name__ == '__main__':
    main()