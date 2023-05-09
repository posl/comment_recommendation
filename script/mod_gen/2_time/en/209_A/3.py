def main():
    # Read the first line of input
    line1 = input()
    # Split the line into two numbers
    a, b = line1.split()
    # Convert the numbers from strings to integers
    a = int(a)
    b = int(b)
    # Print the result
    print(b - a + 1)

if __name__ == '__main__':
    main()