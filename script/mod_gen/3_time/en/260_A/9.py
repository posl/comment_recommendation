def main():
    # Get the input
    s = input()
    # Get a list of characters
    chars = list(s)
    # Get a set of characters
    char_set = set(s)
    # Check if there is only one character
    if len(char_set) == 1:
        print("-1")
    else:
        # Loop through the characters
        for char in chars:
            # Check if the character is only in the string once
            if chars.count(char) == 1:
                print(char)
                break

if __name__ == '__main__':
    main()