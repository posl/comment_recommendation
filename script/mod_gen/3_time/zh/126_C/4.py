def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1
        else:
            point = 1
            while i * point < K:
                point *= 2
            ans += 1 / point
    print(ans / N)

if __name__ == '__main__':
    main()