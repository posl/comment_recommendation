def main():
    # Get the input
    input = raw_input()
    # Split the input into a list
    input_list = input.split()
    # Convert the list of strings to a list of integers
    input_list = map(int, input_list)
    # Get the distinct integers in the list
    distinct_integers = set(input_list)
    # Print the number of distinct integers
    print len(distinct_integers)

if __name__ == '__main__':
    main()