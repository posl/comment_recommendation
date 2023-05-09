def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        p = 1/N
        j = i
        while j < K:
            p = p/2
            j *= 2
        ans += p
    print(ans)

if __name__ == '__main__':
    main()