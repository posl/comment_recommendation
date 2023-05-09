def main():
    N = int(input())
    A = [input() for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, int(A[i][j]) + sum([int(A[i][(j+1)%N]), int(A[i][(j-1)%N]), int(A[(i+1)%N][j]), int(A[(i-1)%N][j]), int(A[(i+1)%N][(j+1)%N]), int(A[(i+1)%N][(j-1)%N]), int(A[(i-1)%N][(j+1)%N]), int(A[(i-1)%N][(j-1)%N])]))
    print(ans)
