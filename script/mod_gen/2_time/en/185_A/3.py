def main():
    # Get input here
    A = list(map(int, input().strip().split()))
    # Calculate result here
    result = 0
    for i in range(4):
        if A[i] == 1:
            result += 1
    # Print output here
    print(result)
main()

if __name__ == '__main__':
    main()