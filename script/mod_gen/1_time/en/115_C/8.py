def main():
    # Write your code here
    N, K = map(int, input().split())
    h = sorted([int(input()) for _ in range(N)])
    print(min(h[i + K - 1] - h[i] for i in range(N - K + 1)))

if __name__ == '__main__':
    main()