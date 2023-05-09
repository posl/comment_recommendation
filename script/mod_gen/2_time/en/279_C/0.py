def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        S[i] = S[i] + S[i]
    for i in range(H):
        T[i] = T[i] + T[i]
    for i in range(H):
        if S[i] not in T:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()