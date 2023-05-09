def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int,list(input()))))
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans,A[i][j]+A[i][(j+1)%N]+A[i][(j+2)%N]+A[i][(j+3)%N]+A[(i+1)%N][j]+A[(i+2)%N][j]+A[(i+3)%N][j]+A[(i+1)%N][(j+1)%N]+A[(i+2)%N][(j+2)%N]+A[(i+3)%N][(j+3)%N])
    print(ans)
