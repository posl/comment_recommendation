def main():
    # Read data
    N = int(input())
    A = [int(x) for x in input().split()]
    # Solve problem
    P = 0
    squares = [0]*4
    squares[0] = 1
    for i in range(N):
        squares[0] += 1
        for j in range(4):
            if squares[j] > 0:
                if j + A[i] >= 4:
                    P += squares[j]
                    squares[j] = 0
                else:
                    squares[j + A[i]] += squares[j]
                    squares[j] = 0
    print(P)
