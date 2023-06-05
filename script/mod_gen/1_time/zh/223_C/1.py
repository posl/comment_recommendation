def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    left = 0
    right = 0
    for i in range(N):
        left += A[i]/B[i]
        right += A[N-1-i]/B[N-1-i]
    ans = 0
    for i in range(N):
        ans += A[i]*(left-right)/2
        left -= A[i]/B[i]
        right += A[N-1-i]/B[N-1-i]
    print(ans)

if __name__ == '__main__':
    solve()