def main():
    # Get input here
    a = [int(x) for x in input().strip().split()]
    
    # Calculate result here
    result = 0
    for i in range(3):
        result = a[result]
    
    # Print result here
    print(result)

if __name__ == '__main__':
    main()