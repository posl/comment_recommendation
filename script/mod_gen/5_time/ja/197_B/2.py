def main():
    H, W, X, Y = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    result = 1
    for i in range(1, H):
        if S[X-1-i][Y-1] == '#':
            break
        else:
            result += 1
    for i in range(1, H):
        if S[X-1+i][Y-1] == '#':
            break
        else:
            result += 1
    for i in range(1, W):
        if S[X-1][Y-1-i] == '#':
            break
        else:
            result += 1
    for i in range(1, W):
        if S[X-1][Y-1+i] == '#':
            break
        else:
            result += 1
    print(result)

if __name__ == '__main__':
    main()