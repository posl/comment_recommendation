def main():
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for i2 in range(i, H):
                for j2 in range(j, W):
                    if i == i2 and j == j2:
                        continue
                    ans = min(ans, A[i][j] + A[i2][j2] + C * (abs(i - i2) + abs(j - j2)))
    print(ans)

if __name__ == '__main__':
    main()