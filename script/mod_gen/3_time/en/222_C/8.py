def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    #print(A)
    #print(N,M)
    R = [i for i in range(1,2*N+1)]
    #print(R)
    for i in range(M):
        #print("Round",i+1)
        for j in range(N):
            #print("Match",j+1)
            #print(R)
            p1 = R[2*j]
            p2 = R[2*j+1]
            if A[p1-1][i] == "G":
                if A[p2-1][i] == "C":
                    R[2*j] = p1
                    R[2*j+1] = p2
                elif A[p2-1][i] == "P":
                    R[2*j] = p2
                    R[2*j+1] = p1
                else:
                    R[2*j] = p1
                    R[2*j+1] = p2
            elif A[p1-1][i] == "C":
                if A[p2-1][i] == "P":
                    R[2*j] = p1
                    R[2*j+1] = p2
                elif A[p2-1][i] == "G":
                    R[2*j] = p2
                    R[2*j+1] = p1
                else:
                    R[2*j] = p1
                    R[2*j+1] = p2
            elif A[p1-1][i] == "P":
                if A[p2-1][i] == "G":
                    R[2*j] = p1
                    R[2*j+1] = p2
                elif A[p2-1][i] == "C":
                    R[2*j] = p2
                    R[2*j+1] = p1
                else:
                    R[2*j] = p1
                    R[2*j+1] = p2
        #print(R)
    for k in range(2*N):
        print(R[k])

if __name__ == '__main__':
    main()