def main():
    # Get the number of test cases
    test_cases = int(input())
    # Loop over the test cases
    for test_case in range(test_cases):
        # Get the number of integers
        num_ints = int(input())
        # Get the integers
        integers = input().split()
        # Count the number of odd integers
        num_odd = 0
        for integer in integers:
            if int(integer) % 2 == 1:
                num_odd += 1
        # Print the number of odd integers
        print(num_odd)
main()

if __name__ == '__main__':
    main()