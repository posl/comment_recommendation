def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    print(solve(H, W, S))

if __name__ == '__main__':
    main()