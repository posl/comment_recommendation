def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int,input())))
    #print(A)
    ans = 0
    for i in range(N):
        for j in range(N):
            #print(A[i][j])
            ans = max(ans, A[i][j] + A[(i+1)%N][j] + A[(i-1)%N][j] + A[i][(j+1)%N] + A[i][(j-1)%N] + A[(i+1)%N][(j+1)%N] + A[(i-1)%N][(j-1)%N] + A[(i+1)%N][(j-1)%N] + A[(i-1)%N][(j+1)%N])
    print(ans)
