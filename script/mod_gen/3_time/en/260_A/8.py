def main():
    # Get the string from the user
    string = input()
    # Create a dictionary to hold the count of each character
    charCount = {}
    # Loop through the string and count the characters
    for char in string:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
    # Loop through the dictionary and print the first character that
    # only occurs once
    for char in charCount:
        if charCount[char] == 1:
            print(char)
            return
    # If we get here, then no character occurs once
    print(-1)

if __name__ == '__main__':
    main()