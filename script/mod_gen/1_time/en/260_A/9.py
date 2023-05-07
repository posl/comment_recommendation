def main():
    # Read in the input
    s = input()
    # Create a dictionary to store the character counts
    char_counts = {}
    # Loop through the characters in the string
    for c in s:
        # If the character is already in the dictionary
        if c in char_counts:
            # Increment the count
            char_counts[c] += 1
        # Otherwise, add it to the dictionary
        else:
            char_counts[c] = 1
    # Loop through the dictionary
    for c in char_counts:
        # If the count is 1, print the character
        if char_counts[c] == 1:
            print(c)
            # Exit the function
            return
    # If we get here, no character occurred only once
    print(-1)

if __name__ == '__main__':
    main()