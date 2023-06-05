def solve():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * N
    B[0] = 0
    for i in range(1, N):
        if A[i - 1] < A[i]:
            B[i] = B[i - 1] + 1
        else:
            B[i] = 0
    #print(B)
    ans = 0
    for i in range(N):
        ans += B[i]
    print(ans)

if __name__ == '__main__':
    solve()