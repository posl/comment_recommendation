def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_num = min(map(min, A))
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_num
    print(ans)

if __name__ == '__main__':
    main()