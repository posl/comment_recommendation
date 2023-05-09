def main():
    H, W = map(int, input().split())
    CH, CW = map(int, input().split())
    DH, DW = map(int, input().split())
    S = [[c for c in input()] for _ in range(H)]
    print(solve(H, W, CH - 1, CW - 1, DH - 1, DW - 1, S))

if __name__ == '__main__':
    main()