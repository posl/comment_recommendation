def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        current = i
        p = 1/N
        if current >= K:
            ans += p
        else:
            while current < K:
                p /= 2
                current *= 2
            ans += p
    print(ans)

if __name__ == '__main__':
    main()