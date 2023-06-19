def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N,A)
    B = sorted(A)
    #print(B)
    #print(B[0],B[1],B[2],B[3])
    #print(B[4],B[5],B[6],B[7])
    #print(B[8],B[9],B[10],B[11])
    #print(B[12],B[13],B[14],B[15])
    for i in range(2**N):
        if A[i] == B[1]:
            print(i+1)
            break
main()
