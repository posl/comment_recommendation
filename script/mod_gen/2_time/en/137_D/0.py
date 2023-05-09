def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    B, A = zip(*sorted(zip(B, A), reverse=True))
    B = list(B)
    A = list(A)
    ans = 0
    for i in range(N):
        if A[i] <= M:
            ans += B[i]
            M -= A[i]
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()