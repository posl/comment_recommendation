def main():
    N = int(input())
    C = list(map(int, input().split()))
    A = [0] * N
    A[0] = 1
    for i in range(1, N):
        if C[i-1] < C[i]:
            A[i] = A[i-1] + 1
        else:
            A[i] = 1
    print(A)
    ans = 1
    for i in range(N):
        ans *= A[i] ** A[i]
    print(ans % (10**9 + 7))
main()

if __name__ == '__main__':
    main()