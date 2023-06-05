def main():
    H,W = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                count += 1
    print(count)

if __name__ == '__main__':
    main()