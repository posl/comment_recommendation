def get_min_error():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    C = [list(map(int, input().split())) for _ in range(N)]
    #print("N = %d, C = %d" % (N, C))
    #print("D = ", D)
    #print("C = ", C)
    #print("C[0][0] = ", C[0][0])
    #print("D[0][C[0][0]-1] = ", D[0][C[0][0]-1])
    #print("D[1][C[0][0]-1] = ", D[1][C[0][0]-1])
    #print("D[2][C[0][0]-1] = ", D[2][C[0][0]-1])
    #print("D[0][C[0][1]-1] = ", D[0][C[0][1]-1])
    #print("D[1][C[0][1]-1] = ", D[1][C[0][1]-1])
    #print("D[2][C[0][1]-1] = ", D[2][C[0][1]-1])
    #print("D[0][C[0][2]-1] = ", D[0][C[0][2]-1])
    #print("D[1][C[0][2]-1] = ", D[1][C[0][2]-1])
    #print("D[2][C[0][2]-1] = ", D[2][C[0][2]-1])
    
    #print("C[1][0] = ", C[1][0])
    #print("D[0][C[1][0]-1] = ", D[0][C[1][0]-1])
    #print("D[1][C[1][0]-1] = ", D[1][C[1][0]-1])
    #print("D[2][C[1][0]-1] = ", D[2][C[1][0]-1])
    #print("D[0][C[1][1
