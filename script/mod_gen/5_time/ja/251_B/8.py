def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, W, A))

if __name__ == '__main__':
    main()