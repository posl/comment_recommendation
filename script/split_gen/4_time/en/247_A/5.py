def main():
    # Take input
    s = input()
    # Initialize the result string
    result = ""
    # Loop through the input string
    for i in range(len(s)):
        # If the character is 1, add 0 to the result string
        if s[i] == "1":
            result += "0"
        # If the character is 0, add 1 to the result string
        else:
            result += "1"
    # Print the result string
    print(result)
