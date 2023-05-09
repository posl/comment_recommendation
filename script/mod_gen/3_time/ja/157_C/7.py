def main():
    N, M = map(int, input().split())
    c = [0] * N
    for i in range(M):
        s, cc = map(int, input().split())
        if c[s-1] == 0:
            c[s-1] = cc
        elif c[s-1] != cc:
            print(-1)
            return
    if c[0] == 0:
        if N == 1:
            print(0)
        else:
            print(1, end='')
            for i in range(N-1):
                print(0, end='')
            print()
    else:
        if c[0] == 1 and N > 1:
            print(1, end='')
            for i in range(N-1):
                print(0, end='')
            print()
        elif c[0] == 1 and N == 1:
            print(1)
        else:
            print(c[0], end='')
            for i in range(1, N):
                print(c[i], end='')
            print()

if __name__ == '__main__':
    main()