def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S = [''.join(sorted(s)) for s in S]
    T = [''.join(sorted(t)) for t in T]
    S.sort()
    T.sort()
    if S == T:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()