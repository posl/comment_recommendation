def solve():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    B = [0]*(m+1)
    for i in range(m+1):
        B[m-i] = C[n+m-i]
        for j in range(n+1):
            B[m-i] -= A[n-j]*B[m-i+j]
    print(*B)

if __name__ == '__main__':
    solve()