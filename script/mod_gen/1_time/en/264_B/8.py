def main():
    # Read the input
    r, c = map(int, input().split())
    # Print the output
    if (r + c) % 2 == 0:
        print("black")
    else:
        print("white")

if __name__ == '__main__':
    main()