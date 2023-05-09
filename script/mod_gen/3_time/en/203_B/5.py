def main():
    # Get N and K
    N, K = map(int, input().split())
    # Calculate the sum of the room numbers
    sum = 0
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            sum += 100 * i + j
    # Print the answer
    print(sum)

if __name__ == '__main__':
    main()