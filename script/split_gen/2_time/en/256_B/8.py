def main():
    #Read input
    N = int(input())
    A = list(map(int,input().split()))
    
    #Initialize variables
    P = 0
    squares = [0,0,0,0]
    
    #Perform operations
    for i in range(N):
        squares[0] += 1
        for j in range(1,4):
            squares[j] += squares[j-1]
            squares[j-1] = 0
        squares[3] += squares[2]
        squares[2] = 0
        P += squares[3]
        squares[3] = 0
        squares[A[i]-1] += 1
    print(P)
