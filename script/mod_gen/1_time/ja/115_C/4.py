def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    min_diff = float('inf')
    for i in range(N - K + 1):
        diff = h[i + K - 1] - h[i]
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()