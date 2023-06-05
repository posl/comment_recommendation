def solve(n, A):
    n = 2*n + 1
    B = [0]*n
    B[0] = 0
    for i in range(n-1):
        B[i+1] = B[(i+1)//2] + 1
    ans = []
    for i in range(n):
        ans.append(B[A[i]])
    return ans
n = int(input())
A = list(map(int, input().split()))
ans = solve(n, A)
for i in range(len(ans)):
    print(ans[i])
