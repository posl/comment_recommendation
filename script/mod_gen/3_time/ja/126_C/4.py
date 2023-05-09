def main():
    N, K = map(int, input().split())
    if N >= K:
        print(1)
    else:
        ans = 0
        for i in range(1, N+1):
            tmp = 1/N
            tmp *= (1/2)**((i-1).bit_length())
            ans += tmp
        print(ans)

if __name__ == '__main__':
    main()