def solve():
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    ans = S
    s = 0
    for i in range(N-1):
        s += A[i]
        ans = min(ans, abs(S - s - s))
    print(ans)

if __name__ == '__main__':
    solve()