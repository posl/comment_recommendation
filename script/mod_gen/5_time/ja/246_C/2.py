def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] < X:
                ans += A[i]
                K -= 1
            else:
                ans += X
        else:
            ans += A[i]
    print(ans)
    return 0

if __name__ == '__main__':
    solve()