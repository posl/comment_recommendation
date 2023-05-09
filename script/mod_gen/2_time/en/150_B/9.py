def main():
    # Read the data
    n = int(input())
    s = input()
    # Count the number of occurrences of ABC
    count = 0
    for i in range(n-2):
        if s[i:i+3] == 'ABC':
            count += 1
    # Print the result
    print(count)

if __name__ == '__main__':
    main()