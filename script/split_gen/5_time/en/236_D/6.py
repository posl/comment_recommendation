def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int,input().split())))
    B = []
    for i in range(N):
        tmp = []
        for j in range(i+1,N):
            tmp.append(A[i][j])
        B.append(tmp)
    #print(B)
    #print(B[0][0]^B[1][0]^B[2][0]^B[3][0])
    #print(B[0][1]^B[1][1]^B[2][1]^B[3][1])
    #print(B[0][0]^B[1][0]^B[2][0]^B[3][0] ^ B[0][1]^B[1][1]^B[2][1]^B[3][1])
    #print(B[0][0]^B[1][0]^B[2][0]^B[3][0] ^ B[0][1]^B[1][1]^B[2][1]^B[3][1] ^ B[0][2]^B[1][2]^B[2][2]^B[3][2])
    #print(B[0][0]^B[1][0]^B[2][0]^B[3][0] ^ B[0][1]^B[1][1]^B[2][1]^B[3][1] ^ B[0][2]^B[1][2]^B[2][2]^B[3][2] ^ B[0][3]^B[1][3]^B[2][3]^B[3][3])
    #print(B[0][0]^B[1][0]^B[2][0]^B[3][0] ^ B[0][1]^B[1][1]^B[2][1]^B[3][1] ^ B[0][2]^B[1][2]^B[2][2]^B[3][2] ^ B[0][3]^B[1][3]^B[2][3]^B[3][3] ^ B[0][4]^B[1][4]^B[2][4]^B[3][4])
    #print(B[0][0]^B[1][0]^B
