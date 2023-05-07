def main():
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            #print(A[i][j])
            #print(A[i][(j+1)%N])
            #print(A[(i+1)%N][j])
            #print(A[(i+1)%N][(j+1)%N])
            tmp = A[i][j] + A[i][(j+1)%N] + A[(i+1)%N][j] + A[(i+1)%N][(j+1)%N]
            #print(tmp)
            if tmp > ans:
                ans = tmp
    print(ans)

if __name__ == '__main__':
    main()