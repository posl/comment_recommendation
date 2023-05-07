def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    max_count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                for k in range(H):
                    for l in range(W):
                        if S[k][l] == '.':
                            dist = abs(k - i) + abs(l - j)
                            max_count = max(max_count, dist)
    print(max_count)

if __name__ == '__main__':
    main()