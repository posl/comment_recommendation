def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] >= 0:
            if i > 0:
                ans += A[i] * min(i, L)
            if N - i > 0:
                ans += A[i] * min(N - i, R)
        else:
            if i > 0:
                ans += A[i] * min(i, R)
            if N - i > 0:
                ans += A[i] * min(N - i, L)
    print(ans)
main()
