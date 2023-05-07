def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p = [i * (i + 1) / 2 / i for i in p]
    print(max(sum(p[i: i + K]) for i in range(N - K + 1)))

if __name__ == '__main__':
    main()