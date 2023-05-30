def main():
    # Get input here
    a, b = map(int, input().strip().split())
    # Calculate result here
    if a > b:
        print(0)
    else:
        print(b-a+1)
    # Print output here
main()
