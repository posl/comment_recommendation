def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    for i in range(H):
        if S[i].count('#') != T[i].count('#'):
            print('No')
            exit()
    print('Yes')
main()

if __name__ == '__main__':
    main()