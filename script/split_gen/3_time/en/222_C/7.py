def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    #print(N, M)
    #print(A)
    #ID = [i for i in range(1, 2*N+1)]
    #print(ID)
    #print()
    #print("===== start =====")
    for i in range(M):
        #print("===== round {} =====".format(i+1))
        #print(ID)
        #print()
        ID = [i for i in range(1, 2*N+1)]
        for j in range(N):
            #print("===== match {} =====".format(j+1))
            #print(ID)
            #print()
            if A[ID[2*j]-1][i] == A[ID[2*j+1]-1][i]:
                continue
            elif A[ID[2*j]-1][i] == "G":
                if A[ID[2*j+1]-1][i] == "C":
                    ID[2*j], ID[2*j+1] = ID[2*j+1], ID[2*j]
                else:
                    pass
            elif A[ID[2*j]-1][i] == "C":
                if A[ID[2*j+1]-1][i] == "P":
                    ID[2*j], ID[2*j+1] = ID[2*j+1], ID[2*j]
                else:
                    pass
            elif A[ID[2*j]-1][i] == "P":
                if A[ID[2*j+1]-1][i] == "G":
                    ID[2*j], ID[2*j+1] = ID[2*j+1], ID[2*j]
                else:
                    pass
            else:
                pass
        #print("===== end =====")
        #print(ID)
        #print()
    #print("===== finish =====")
    #print(ID)
    #print()
    for i in range(2*N):
        print(ID[i])
