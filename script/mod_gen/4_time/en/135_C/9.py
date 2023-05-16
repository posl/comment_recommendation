def solve(N,A,B):
    ans = 0
    for i in range(N):
        if A[i] >= B[i]:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
        else:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
            if A[i+1] >= B[i]:
                ans += B[i]
                A[i+1] -= B[i]
                B[i] = 0
            else:
                ans += A[i+1]
                B[i] -= A[i+1]
                A[i+1] = 0
    return ans
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(solve(N,A,B))

if __name__ == '__main__':
    solve()