def main():
    # Read the input
    S, T = map(int, input().split())
    # Initialize the counter
    counter = 0
    # Loop through all possible values of a
    for a in range(S + 1):
        # Loop through all possible values of b
        for b in range(S + 1):
            # Loop through all possible values of c
            for c in range(S + 1):
                # Check if the conditions are satisfied
                if a + b + c <= S and a * b * c <= T:
                    # If so, increment the counter
                    counter += 1
    # Print the result
    print(counter)
