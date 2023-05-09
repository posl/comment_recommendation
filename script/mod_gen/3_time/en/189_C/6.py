def main():
    # Read input
    N = int(input())
    A = list(map(int, input().split()))
    
    # Initialize variables
    ans = 0
    
    # Solve
    for i in range(N):
        x = A[i]
        for j in range(i, N):
            x = min(x, A[j])
            ans = max(ans, x * (j - i + 1))
    
    # Output
    print(ans)

if __name__ == '__main__':
    main()