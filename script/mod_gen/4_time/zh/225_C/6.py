def main():
    #input
    N,M = map(int,input().split())
    B = []
    for i in range(N):
        B.append(list(map(int,input().split())))
    #print(B)
    #print(N,M)
    #print(B[0][0])
    #print(B[0][1])
    #print(B[0][2])
    #print(B[1][0])
    #print(B[1][1])
    #print(B[1][2])
    #print(B[2][0])
    #print(B[2][1])
    #print(B[2][2])
    #check
    for i in range(10**100):
        for j in range(1,8):
            #print(i,j)
            if i*7+j == B[0][0]:
                #print("ok")
                if i+N-1 < 10**100:
                    #print("ok")
                    if j+M-1 < 8:
                        #print("ok")
                        #print(B[0][0])
                        #print(B[0][1])
                        #print(B[0][2])
                        #print(B[1][0])
                        #print(B[1][1])
                        #print(B[1][2])
                        #print(B[2][0])
                        #print(B[2][1])
                        #print(B[2][2])
                        #print(i,j)
                        #print(i+N-1,j+M-1)
                        #print(B[0][0] == i*7+j)
                        #print(B[0][1] == i*7+j+1)
                        #print(B[0][2] == i*7+j+2)
                        #print(B[1][0] == (i+1)*7+j)
                        #print(B[1][1] == (i+1)*7+j+1)
                        #print(B[1][2] == (i+1)*7+j+2)
                        #print(B[2][0] == (i+2)*7+j)
                        #print(B[2][1] == (i+2)*7+j+1)
                        #print(B[2][2] == (i+2)*7+j+2)
                        if B[0][0] == i*7+j and B[0][1] == i

if __name__ == '__main__':
    main()