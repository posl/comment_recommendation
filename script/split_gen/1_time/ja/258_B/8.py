def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append( [ int(x) for x in input()] )
    ans = 0
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N-1):
                tmp = tmp * 10 + A[(i+k)%N][j]
                tmp = tmp * 10 + A[i][(j+k)%N]
                tmp = tmp * 10 + A[(i+k)%N][(j+k)%N]
                tmp = tmp * 10 + A[(i+k)%N][(j-k+N)%N]
            ans = max(ans, tmp)
    print(ans)
