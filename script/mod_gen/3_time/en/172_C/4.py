def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a, b, ans = 0, 0, 0
    while a < N and A[a] <= K:
        K -= A[a]
        a += 1
    ans = a
    for i in range(M):
        if K < B[i]:
            break
        K -= B[i]
        b += 1
        while a > 0 and K < A[a - 1]:
            K += A[a - 1]
            a -= 1
        ans = max(ans, a + b)
    print(ans)

if __name__ == '__main__':
    main()