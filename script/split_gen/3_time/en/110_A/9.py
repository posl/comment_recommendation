def main():
    # Read input
    input = raw_input()
    # Split input into a list
    input = input.split()
    # Convert the list into integers
    input = map(int, input)
    # Sort the list
    input.sort()
    # Convert the list into a string
    input = map(str, input)
    # Add the + sign to the middle of the list
    input.insert(1, '+')
    # Convert the list into a string
    input = ''.join(input)
    # Print the result
    print input
