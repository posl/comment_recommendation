def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    for i in range(1, N):
        if A[i] % 2 == 0:
            print(B[N] - B[i])
            return
    print(-1)

if __name__ == '__main__':
    main()