def main():
    H,W = map(int,input().split())
    X = [0 for i in range(W)]
    for i in range(H):
        S = input()
        for j in range(W):
            if S[j] == '#':
                X[j] += 1
    print(*X)

if __name__ == '__main__':
    main()