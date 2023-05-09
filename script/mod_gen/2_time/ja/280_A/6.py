def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()