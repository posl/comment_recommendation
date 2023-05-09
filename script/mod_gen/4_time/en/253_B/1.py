def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                count += 1
    if count == 2:
        print(2)
    else:
        print(3)

if __name__ == '__main__':
    main()