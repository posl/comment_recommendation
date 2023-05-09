def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        S[i] = ''.join(sorted(S[i]))
        T[i] = ''.join(sorted(T[i]))
    S.sort()
    T.sort()
    if S == T:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()