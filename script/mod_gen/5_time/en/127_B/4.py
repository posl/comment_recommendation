def main():
    # Get input here
    r, D, x = map(int, input().strip().split())
    # Calculate result
    for i in range(10):
        x = r * x - D
        print(x)
    # Print result here
main()
