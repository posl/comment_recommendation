def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    A = [0] + A
    B = [0] * (N+1)
    for i in range(1, N+1):
        B[i] = B[i-1] + A[i]
    ans = 0
    for i in range(1, N+1):
        ans += A[i]
    for i in range(1, N+1):
        if A[i] == A[i-1]:
            continue
        else:
            if i-1 <= M:
                M -= (i-1)
                ans -= B[i-1]
            else:
                ans -= B[M]
                break
    print(ans)

if __name__ == '__main__':
    main()