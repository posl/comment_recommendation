def main():
    # Take input from stdin
    S = input()
    # Create a list from the input
    S = list(S)
    # Initialize counter
    counter = 0
    # Initialize max counter
    max_counter = 0
    # Iterate over the list
    for i in S:
        # If the character is R
        if i == 'R':
            # Increment the counter
            counter += 1
            # If the counter is greater than the max counter
            if counter > max_counter:
                # Set the max counter to the counter
                max_counter = counter
        # If the character is S
        else:
            # Reset the counter
            counter = 0
    # Print the max counter
    print(max_counter)
