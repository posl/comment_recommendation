def main():
    N, S, D = map(int, input().split())
    XY = [map(int, input().split()) for _ in range(N)]
    X, Y = [list(i) for i in zip(*XY)]
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print('Yes')
            exit()
    print('No')
main()

if __name__ == '__main__':
    main()