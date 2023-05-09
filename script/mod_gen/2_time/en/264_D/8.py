def main():
    # Read the input
    S = input()
    # Define the target string
    target = "atcoder"
    # Define the counter
    counter = 0
    # Loop through the string
    for i in range(len(S)):
        # Check if the current character is not the same as the target character
        if S[i] != target[i]:
            # Increment the counter
            counter += 1
    # Print the answer
    print(counter)

if __name__ == '__main__':
    main()