def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1/N
        else:
            cnt = 0
            while i < K:
                i *= 2
                cnt += 1
            ans += (1/N) * (1/2)**cnt
    print(ans)

if __name__ == '__main__':
    main()