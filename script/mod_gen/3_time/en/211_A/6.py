def main():
    # Read the input
    A, B = [int(x) for x in input().split()]
    # Calculate the mean arterial pressure
    C = ((A-B)/(3)) +B
    # Print the output
    print(C)

if __name__ == '__main__':
    main()