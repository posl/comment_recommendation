def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    C = [0] * (N + 1)
    for i in range(N):
        C[i + 1] = C[i] + B[i + 1]
    ans = 0
    for i in range(N):
        ans += (B[i + 1] - B[i]) * (C[N] - C[i + 1])
    print(ans)
    return

if __name__ == '__main__':
    main()