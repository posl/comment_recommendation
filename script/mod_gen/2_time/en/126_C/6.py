def main():
    N, K = map(int, input().split())
    result = 0
    for i in range(1, N+1):
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        result += (1 / N) * (1 / 2) ** cnt
    print(result)

if __name__ == '__main__':
    main()