def main():
    # Get the number of test cases from the first line
    num_test_cases = int(input())
    # Loop through each test case
    for i in range(num_test_cases):
        # Get the number of integers in the test case
        num_integers = int(input())
        # Get the integers from the next line
        integers = input().split()
        # Initialize the number of odd integers
        num_odd_integers = 0
        # Loop through each integer
        for j in range(num_integers):
            # If the integer is odd, increment the number of odd integers
            if int(integers[j]) % 2 == 1:
                num_odd_integers += 1
        # Print the number of odd integers
        print(num_odd_integers)

if __name__ == '__main__':
    main()