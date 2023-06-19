def printGrid(N, A, B, P, Q, R, S):
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (A+i<=N and B+j<=N) or (A+i<=N and B-j>=1) or (A-i>=1 and B+j<=N) or (A-i>=1 and B-j>=1):
                print("#", end="")
            else:
                print(".", end="")
        print("")
