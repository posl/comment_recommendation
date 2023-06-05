def main():
    #N = int(input())
    #A = input().split()
    N = 10
    A = "2 2 4 1 1 1 4 2 2 1".split()
    P = 0
    squares = [0,0,0,0]
    for i in range(N):
        squares[0] += 1
        for j in range(4):
            if squares[j] > 0:
                squares[j] -= 1
                if j + int(A[i]) < 4:
                    squares[j + int(A[i])] += 1
                else:
                    P += 1
    print(P)

if __name__ == '__main__':
    main()