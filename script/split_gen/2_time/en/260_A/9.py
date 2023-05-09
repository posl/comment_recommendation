def main():
    # Read the string from the standard input
    s = input()
    # Create a dictionary to count the number of occurrences
    # of each character
    dict = {}
    for c in s:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    # Look for a character that occurs only once
    for c in s:
        if dict[c] == 1:
            print(c)
            return
    # If we get here, no character occurs only once
    print(-1)
