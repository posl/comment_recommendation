def main():
    # Read input
    A, B = map(int, input().split())
    # Calculate mean arterial pressure
    C = ((A - B) / 3) + B
    # Print output
    print(C)

if __name__ == '__main__':
    main()