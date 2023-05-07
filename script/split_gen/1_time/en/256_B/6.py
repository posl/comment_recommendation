def main():
    # read input
    N = int(input())
    A = [int(x) for x in input().split()]
    # initialize variables
    P = 0
    squares = [0,0,0,0]
    # process
    for i in range(N):
        squares[0] += 1
        for j in range(4):
            if squares[j] > 0:
                if j+A[i] < 4:
                    squares[j+A[i]] += squares[j]
                    squares[j] = 0
                else:
                    P += squares[j]
                    squares[j] = 0
    # output
    print(P)
