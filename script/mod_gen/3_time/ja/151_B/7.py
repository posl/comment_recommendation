def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    target = N * M
    if target - total > K:
        print(-1)
    else:
        print(max(target - total, 0))

if __name__ == '__main__':
    main()