def main():
    N, K = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A, B = zip(*sorted(zip(A, B)))
    A = list(A)
    B = list(B)
    # print(A)
    # print(B)
    ans = 0
    for i in range(N):
        if K >= A[i] - ans:
            K += B[i]
            ans = A[i]
        else:
            ans += K
            break
    if ans == A[N - 1]:
        ans += K
    print(ans)

if __name__ == '__main__':
    main()