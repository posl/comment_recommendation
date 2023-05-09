def main():
    # Get input here
    a, b = map(int, input().strip().split())
    # Calculate result here
    result = max(a+b, a-b, a*b)
    # Print output here
    print(result)
