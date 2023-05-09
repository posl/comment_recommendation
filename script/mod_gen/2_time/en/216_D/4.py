def main():
    N, M = map(int, input().split())
    k = [int(input()) for _ in range(M)]
    a = [[int(x) for x in input().split()] for _ in range(M)]
    balls = [0] * (N + 1)
    for i in range(M):
        for j in range(k[i]):
            balls[a[i][j]] += 1
    for i in range(1, N + 1):
        if balls[i] != 2:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()