def main():
    # Get the number of integers
    N = int(input())
    
    # Get the integers
    A = [int(x) for x in input().split()]
    
    # Print the sum of the integers
    print(sum(A))

if __name__ == '__main__':
    main()