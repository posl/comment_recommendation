def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    for _ in range(4):
        if S == T:
            print('Yes')
            break
        S = [list(s) for s in S]
        S = list(zip(*S[::-1]))
        S = [''.join(s) for s in S]
    else:
        print('No')

if __name__ == '__main__':
    main()