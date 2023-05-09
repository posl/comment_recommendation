def main():
    N, M = map(int, input().split())
    D = M**0.5
    d = int(D)
    if D == d:
        d = d - 1
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                print(0, end='')
            elif i == 0:
                print(1, end='')
            elif j == 0:
                print(1, end='')
            else:
                print(d*2, end='')
            if j != N-1:
                print(' ', end='')
        print()

if __name__ == '__main__':
    main()