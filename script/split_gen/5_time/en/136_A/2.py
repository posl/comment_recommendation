def main():
    # Get input here
    a, b, c = map(int, input().strip().split())
    
    # Calculate result here
    result = max(c - (a - b), 0)
    
    # Print output here
    print(result)
main()
