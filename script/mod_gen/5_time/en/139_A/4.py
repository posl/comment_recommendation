def main():
    # Read from standard input
    s = input()
    t = input()
    # Initialize the counter
    count = 0
    # Loop through the strings
    for i in range(len(s)):
        if s[i] == t[i]:
            count += 1
    # Print the result
    print(count)

if __name__ == '__main__':
    main()