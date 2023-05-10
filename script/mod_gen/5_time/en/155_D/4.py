def solve(N, K, A):
    A.sort()
    l = -10**18
    r = 10**18
    while r - l > 1:
        m = (l + r) // 2
        cnt = 0
        for i in range(N):
            if A[i] > 0:
                cnt += bisect.bisect_right(A, m // A[i])
            elif A[i] < 0:
                cnt += N - bisect.bisect_right(A, m // A[i])
            else:
                if m >= 0:
                    cnt += N
                else:
                    cnt += N - i - 1
        cnt //= 2
        if cnt < K:
            l = m
        else:
            r = m
    return l
import bisect
N, K = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, K, A))

if __name__ == '__main__':
    solve()