def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, K, T))

if __name__ == '__main__':
    main()