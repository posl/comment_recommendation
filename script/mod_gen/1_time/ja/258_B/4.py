def main():
    N = int(input())
    A = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, int(A[i][j]) + int(A[i][(j+1)%N]) + int(A[i][(j+2)%N]) + int(A[i][(j+3)%N]) + int(A[(i+1)%N][j]) + int(A[(i+2)%N][j]) + int(A[(i+3)%N][j]))
    print(ans)

if __name__ == '__main__':
    main()