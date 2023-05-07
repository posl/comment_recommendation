def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    for j in range(W):
        print(sum([1 for i in range(H) if C[i][j] == '#']), end=' ')
    print()
    return

if __name__ == '__main__':
    main()