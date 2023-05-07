def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    P = 0
    squares = [0, 0, 0, 0]
    for i in range(N):
        squares[0] += 1
        for j in range(4):
            if squares[j] > 0:
                if j + A[i] >= 4:
                    squares[j] -= 1
                    P += 1
                else:
                    squares[j + A[i]] += 1
                    squares[j] -= 1
    print(P)

if __name__ == '__main__':
    main()