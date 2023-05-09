def main():
    H, W, X, Y = map(int, input().split())
    S = [input() for i in range(H)]
    count = 1
    for i in range(1, H+1):
        if X-i >= 0:
            if S[X-i][Y-1] == '#':
                break
            else:
                count += 1
        if X+i <= H:
            if S[X+i-1][Y-1] == '#':
                break
            else:
                count += 1
    for i in range(1, W+1):
        if Y-i >= 0:
            if S[X-1][Y-i] == '#':
                break
            else:
                count += 1
        if Y+i <= W:
            if S[X-1][Y+i-1] == '#':
                break
            else:
                count += 1
    print(count)

if __name__ == '__main__':
    main()