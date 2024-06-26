def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    def rotate(S):
        return [''.join(x) for x in zip(*S[::-1])]
    for _ in range(4):
        S = rotate(S)
        if S == T:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()