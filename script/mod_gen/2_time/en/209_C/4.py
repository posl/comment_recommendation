def main():
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10**9 + 7
    A = [0] * (N+1)
    A[0] = 1
    for i in range(N):
        A[i+1] = A[i] * (C[i] - i)
        A[i+1] %= MOD
    print(A[N])
main()

if __name__ == '__main__':
    main()