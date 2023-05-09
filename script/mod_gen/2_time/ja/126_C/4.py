def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        j = i
        c = 0
        while j < K:
            j *= 2
            c += 1
        ans += (1/N) * (1/2)**c
    print(ans)

if __name__ == '__main__':
    main()