def readInput():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int,input())))
    return N,A
