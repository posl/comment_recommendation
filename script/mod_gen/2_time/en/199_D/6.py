def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    print(solve(N, M, AB))

if __name__ == '__main__':
    main()