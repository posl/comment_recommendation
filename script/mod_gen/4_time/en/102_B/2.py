def main():
    # Get input here
    N = int(input())
    A = list(map(int, input().split()))
    # Calculate result here
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, abs(A[i] - A[j]))
    # Print result here
    print(ans)
main()

if __name__ == '__main__':
    main()