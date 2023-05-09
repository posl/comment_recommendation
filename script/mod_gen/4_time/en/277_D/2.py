def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    ans = 0
    for i in range(N):
        l = i
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if A[m] - A[i] < M:
                l = m
            else:
                r = m
        ans = max(ans, B[l+1] - B[i])
    print(ans)

if __name__ == '__main__':
    main()