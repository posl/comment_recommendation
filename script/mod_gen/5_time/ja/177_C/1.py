def main():
    N = int(input())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N-1):
        for j in range(i+1, N):
            total += A[i] * A[j]
    print(total % (10**9+7))

if __name__ == '__main__':
    main()