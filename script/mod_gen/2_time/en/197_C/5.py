def solve(N, A):
    ans = 0
    for i in range(N):
        ans |= A[i]
    return ans
N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))

if __name__ == '__main__':
    solve()