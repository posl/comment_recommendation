def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    ans = 0
    tmp = 0
    for i in range(2*N-1):
        tmp += A[i]
        if i >= N:
            tmp -= A[i-N]
        if i >= N-1:
            ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    solve()