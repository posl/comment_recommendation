def main():
    # Read input
    N = int(input())
    # Define variables
    # Calculate
    ans = 0
    for i in range(1,N):
        ans += N/(N-i)
    # Output
    print(ans)

if __name__ == '__main__':
    main()