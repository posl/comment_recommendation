def solve(N, A):
    A.sort()
    ans = [0] * N
    for i in range(N):
        if i > 0 and A[i] == A[i-1]:
            ans[i] = ans[i-1]
            continue
        l = 0
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if A[m] > A[i]:
                r = m
            else:
                l = m
        ans[i] = l
    return ans
N = int(input())
A = list(map(int, input().split()))
ans = solve(N, A)
for i in range(N):
    print(ans[i])

if __name__ == '__main__':
    solve()