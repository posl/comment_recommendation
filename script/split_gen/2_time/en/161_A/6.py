def main():
    # Read a line from stdin
    line = input()
    # Split the line into a list of strings
    line = line.split()
    # Convert the list of strings to a list of integers
    line = [int(i) for i in line]
    # Store the three integers in variables
    a, b, c = line
    # Swap the contents of the boxes A and B
    a, b = b, a
    # Swap the contents of the boxes A and C
    a, c = c, a
    # Print the integers contained in the boxes A, B, and C
    print(a, b, c)
