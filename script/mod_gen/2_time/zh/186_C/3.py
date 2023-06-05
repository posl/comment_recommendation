def main():
    H, W = map(int, input().split())
    a = [[int(i) for i in input().split()] for i in range(H)]
    min_a = 100
    for i in range(H):
        for j in range(W):
            if a[i][j] < min_a:
                min_a = a[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += a[i][j] - min_a
    print(ans)

if __name__ == '__main__':
    main()