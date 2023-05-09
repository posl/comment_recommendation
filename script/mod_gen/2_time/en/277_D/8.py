def solve(N, M, A):
    # write your code here
    B = [0]*M
    for a in A:
        B[a] += 1
    if M == 2:
        return 1 if B[1] > 0 else 0
    if M % 2 == 0:
        B[M//2] = min(B[M//2], 1)
    ans = 0
    for i in range(1, M//2+1):
        ans += min(B[i], B[M-i])*i
    return ans

if __name__ == '__main__':
    solve()