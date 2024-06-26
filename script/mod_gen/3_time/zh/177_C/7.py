def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += A[i] * A[j]
            sum %= MOD
    print(sum)

if __name__ == '__main__':
    main()