def main():
    N, K = map(int, input().split())
    if N < K:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1/N
            continue
        else:
            ans += 1/(N*(2**((K-i-1).bit_length())))
    print(ans)

if __name__ == '__main__':
    main()