def main():
    # Get the input
    N = int(input())
    # Find the next ABC number
    while True:
        if N % 111 == 0:
            break
        N += 1
    # Print the output
    print(N)

if __name__ == '__main__':
    main()