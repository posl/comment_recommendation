def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for i2 in range(H):
                for j2 in range(W):
                    if i == i2 and j == j2:
                        continue
                    ans = min(ans, A[i][j] + A[i2][j2] + C * (abs(i - i2) + abs(j - j2)))
    print(ans)
    return

if __name__ == '__main__':
    main()