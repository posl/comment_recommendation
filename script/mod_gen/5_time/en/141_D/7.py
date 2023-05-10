def main():
    # Get input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Sort the list
    A.sort(reverse = True)
    # Calculate the sum
    sum = 0
    for i in range(N):
        sum += A[i]
    # Calculate the minimum amount of money required
    for i in range(M):
        sum -= A[i] / 2**(i+1)
    # Output the answer
    print(int(sum))

if __name__ == '__main__':
    main()