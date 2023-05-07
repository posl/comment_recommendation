def main():
    # Read the number of test cases.
    T = int(input())
    # Read the data for each test case.
    for t in range(T):
        # Read the number of integers.
        N = int(input())
        # Read the integers.
        A = list(map(int, input().split()))
        # Count the number of odd numbers.
        count = 0
        for a in A:
            if a % 2 == 1:
                count += 1
        # Print the answer.
        print(count)
main()

if __name__ == '__main__':
    main()