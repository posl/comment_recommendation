def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_a = min(A)
    C = []
    for i in range(N):
        C.append(A[i] - min_a)
    D = []
    for i in range(min_a + 1):
        D.append(0)
    for i in range(N):
        D[C[i]] += B[i]
    for i in range(min_a):
        D[i + 1] += D[i]
    ans = 0
    for i in range(min_a + 1):
        if D[i] <= W:
            ans = max(ans, i * D[i] + D[i])
        else:
            ans = max(ans, i * W + W)
    print(ans)

if __name__ == '__main__':
    main()