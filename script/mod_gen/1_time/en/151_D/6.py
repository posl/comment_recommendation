def main():
    H,W = map(int, input().split())
    S = [ input() for i in range(H) ]
    result = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                result = max(result, solve(H, W, S, i, j))
    print(result)

if __name__ == '__main__':
    main()