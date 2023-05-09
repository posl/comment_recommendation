def main():
    # Get the number of test cases
    T = int(input())
    # Loop through the test cases
    for i in range(T):
        # Get the number of numbers in the list
        N = int(input())
        # Get the list of numbers
        numbers = input().split()
        # Convert the list of strings to a list of integers
        numbers = [int(x) for x in numbers]
        # Count the number of odd numbers
        count = 0
        for number in numbers:
            if number % 2 == 1:
                count += 1
        # Print the result
        print(count)
main()
