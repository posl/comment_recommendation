def main():
    import sys
    read = sys.stdin.buffer.read
    N, K = map(int, read().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        p = 1/N
        k = i
        while k < K:
            k *= 2
            p /= 2
        ans += p
    print(ans)

if __name__ == '__main__':
    main()