def main():
    N = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(N - 1)]
    print(solve(N, edges))

if __name__ == '__main__':
    main()