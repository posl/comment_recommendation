def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if A[i+1] < A[i]:
            ans += (A[i] - A[i+1]) * L
        else:
            ans += (A[i+1] - A[i]) * R
    print(ans)

if __name__ == '__main__':
    solve()