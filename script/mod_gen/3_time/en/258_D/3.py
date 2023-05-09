def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    a = 0
    b = 0
    ans = 0
    while X > 0:
        if a == N:
            ans += B[b] * X
            b += 1
            X = 0
        elif b == N:
            ans += A[a] * X
            a += 1
            X = 0
        elif A[a] < B[b]:
            ans += A[a]
            a += 1
            X -= 1
        else:
            ans += B[b]
            b += 1
            X -= 1
    print(ans)

if __name__ == '__main__':
    main()