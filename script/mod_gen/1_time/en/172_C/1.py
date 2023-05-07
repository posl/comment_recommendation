def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(1, N):
        A[i] += A[i - 1]
    for i in range(1, M):
        B[i] += B[i - 1]
    ans = 0
    j = M
    for i in range(-1, N):
        if i == -1:
            a = 0
        else:
            a = A[i]
        if a > K:
            break
        while B[j - 1] > K - a:
            j -= 1
            if j == 0:
                break
        ans = max(ans, i + j)
    print(ans)

if __name__ == '__main__':
    main()