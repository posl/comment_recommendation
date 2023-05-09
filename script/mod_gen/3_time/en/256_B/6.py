def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    P = 0
    squares = [0 for _ in range(4)]
    squares[0] = 1
    for a in A:
        for i in range(4):
            if squares[i] == 1:
                if i + a < 4:
                    squares[i + a] = 1
                else:
                    P += 1
        squares[0] = 1
    print(P)

if __name__ == '__main__':
    main()