def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input())))
    
    ans = 0
    for i in range(N):
        for j in range(N):
            #print(i, j)
            tmp = 0
            for k in range(4):
                tmp += A[i][(j+k)%N]
                #print(tmp)
            ans = max(ans, tmp)
            tmp = 0
            for k in range(4):
                tmp += A[(i+k)%N][j]
                #print(tmp)
            ans = max(ans, tmp)
            tmp = 0
            for k in range(4):
                tmp += A[(i+k)%N][(j+k)%N]
                #print(tmp)
            ans = max(ans, tmp)
            tmp = 0
            for k in range(4):
                tmp += A[(i+k)%N][(j-k)%N]
                #print(tmp)
            ans = max(ans, tmp)
    print(ans)
