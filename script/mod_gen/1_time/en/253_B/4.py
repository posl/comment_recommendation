def main():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                a = i
                b = j
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                c = i
                d = j
    print(max(abs(a - c), abs(b - d)))

if __name__ == '__main__':
    main()