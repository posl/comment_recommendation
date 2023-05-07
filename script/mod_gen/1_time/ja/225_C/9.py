def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    print('Yes' if any((all(B[i][j] == 7 * (i + a) + j + b for a in range(N) for b in range(M))) for i in range(10 ** 100 - N) for j in range(7 - M)) else 'No')

if __name__ == '__main__':
    main()