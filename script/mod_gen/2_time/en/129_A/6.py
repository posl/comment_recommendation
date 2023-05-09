def main():
    # Read data
    data = input()
    # Split data
    data = data.split(" ")
    # Convert to integers
    data = [int(i) for i in data]
    # Sort
    data.sort()
    # Print result
    print(data[0] + data[1])

if __name__ == '__main__':
    main()