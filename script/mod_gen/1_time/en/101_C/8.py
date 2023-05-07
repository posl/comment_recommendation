def main():
    # Get input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # Initialize variables
    ans = 0
    tmp = 0
    # Count the number of operations required
    for i in range(N - K):
        if A[i] < A[i + K]:
            tmp += 1
        else:
            ans += (tmp + 1)
            tmp = 0
    # Output the answer
    print(ans + 1)

if __name__ == '__main__':
    main()