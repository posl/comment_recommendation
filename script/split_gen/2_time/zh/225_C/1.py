def main():
    N, M = map(int, input().split())
    B = [input().split() for i in range(N)]
    B = [[int(B[i][j]) for j in range(M)] for i in range(N)]
    A = [[(i-1)*7+j+1 for j in range(7)] for i in range(1, 10**100+1)]
    #print(A)
    #print(B)
    for i in range(10**100):
        for j in range(7):
            if A[i][j] == B[0][0]:
                for k in range(N):
                    for l in range(M):
                        if i+k >= 10**100 or j+l >= 7:
                            print("No")
                            return
                        if A[i+k][j+l] != B[k][l]:
                            print("No")
                            return
                print("Yes")
                return
